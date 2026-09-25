import csv
import io
import sqlite3
from datetime import datetime
from collections import Counter
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title='LeadPilot AI')

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')
DB = 'data/leads.db'

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row

    c.execute('''
        CREATE TABLE IF NOT EXISTS leads(
            id INTEGER PRIMARY KEY,
            company TEXT,
            contact TEXT,
            source TEXT,
            conversation TEXT,
            summary TEXT,
            requirements TEXT,
            intent TEXT,
            score INTEGER,
            stage TEXT,
            recommendation TEXT,
            followup TEXT,
            created_at TEXT)''')
    c.commit()
    return c

def analyze(text, company='Unknown'):
    t = text.lower()
    hot = [
        'ready to buy',
        'budget',
        'pricing',
        'purchase',
        'proposal',
        'contract',
        'demo',
        'urgent',
        'timeline'
    ]

    warm = [
        'interested',
        'compare',
        'meeting',
        'explore',
        'evaluation',
        'next month'
    ]

    cold = [
        'research',
        'not sure',
        'maybe',
        'later',
        'information'
    ]

    score = max(
        10,
        min( 98, 42
            + sum(x in t for x in hot) * 9
            + sum(x in t for x in warm) * 5
            - sum(x in t for x in cold) * 6
            + len(t) // 180
        ))
    intent = 'High' if score >= 75 else 'Medium' if score >= 50 else 'Low'
    stage = (
        'Proposal'
        if score >= 82
        else 'Qualified'
        if score >= 65
        else 'Nurture'
        if score >= 45
        else 'New'
    )

    terms = [
        'CRM',
        'automation',
        'analytics',
        'integration',
        'AI',
        'dashboard',
        'pricing',
        'security',
        'support',
        'API',
        'reporting',
        'demo',
        'implementation'
    ]

    req = ', '.join(
        x for x in terms if x.lower() in t
    ) or 'Requirements need further discovery'
    summary = (
        f'{company} shows {intent.lower()} buying intent. '
        f'The conversation indicates interest in {req.lower()}.')
    rec = (
        'Send Proposal Now'
        if score >= 82
        else 'Schedule Demo'
        if score >= 65
        else 'Follow Up in 2 Weeks'
        if score >= 45
        else 'Add to Nurture'
    )

    follow = (
        f'Subject: Next steps for {company}\n\n'
        'Hi,\n'
        'Thank you for discussing your requirements with us. '
        'I would be happy to arrange the next step and answer any questions. '
        'Please share a suitable time for a follow-up.\n\n'
        'Best regards,\n'
        'Sales Team'
    )

    return dict(
        summary=summary,
        requirements=req,
        intent=intent,
        score=score,
        stage=stage,
        recommendation=rec,
        followup=follow
    )


def save(company, contact, source, text, r):
    c = db()

    c.execute(
        'INSERT INTO leads(company,contact,source,conversation,summary,'
        'requirements,intent,score,stage,recommendation,followup,created_at) '
        'VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
        (
            company,
            contact,
            source,
            text,
            r['summary'],
            r['requirements'],
            r['intent'],
            r['score'],
            r['stage'],
            r['recommendation'],
            r['followup'],
            datetime.now().strftime('%Y-%m-%d %H:%M')
        )
    )
    c.commit()


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    rows = db().execute('SELECT * FROM leads ORDER BY id DESC').fetchall()
    return templates.TemplateResponse(
        request=request,
        name='dashboard.html',
        context={
            'request': request,
            'leads': rows,
            'stages': dict(
                Counter(r['stage'] for r in rows)
            )
        }
    )


@app.post('/api/analyze')
def api_analyze(
    company: str = Form('Unknown'),
    contact: str = Form(''),
    source: str = Form('Website'),
    conversation: str = Form(...)
):
    r = analyze(conversation, company)

    save(company, contact, source, conversation, r)
    return JSONResponse(r)

@app.post('/api/bulk')
async def bulk(file: UploadFile = File(...)):
    reader = csv.DictReader(
        io.StringIO(
            (await file.read()).decode('utf-8-sig'))
    )

    count = 0
    for row in reader:
        text = (
            row.get('conversation')
            or row.get('text')
            or row.get('message')
            or row.get('inquiry')
            or ''
        )

        if text.strip():
            save(
                row.get('company') or 'Unknown',
                row.get('contact', ''),
                row.get('source', 'CSV Upload'),
                text,
                analyze(
                    text,
                    row.get('company') or 'Unknown'
                )
            )
        count += 1
    return {
        'message': f'{count} leads imported successfully'
    }


@app.get('/api/leads')
def leads():
    return [
        dict(x)
        for x in db().execute(
            'SELECT * FROM leads ORDER BY id DESC'
        ).fetchall()
    ]