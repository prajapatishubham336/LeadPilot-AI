# LeadPilot-AI
AI-powered lead scoring and qualification system that analyzes customer conversations, identifies buying intent, scores leads, recommends sales actions, and generates follow-up emails.

# 🚀 LeadPilot AI

### AI-Powered Lead Scoring & Sales Intelligence Platform

LeadPilot AI is an intelligent lead analysis platform that helps sales teams understand customer conversations, identify buying intent, score leads, determine their sales stage, and recommend the next sales action.

Instead of manually reading every customer inquiry or conversation, LeadPilot AI analyzes the text and converts it into actionable sales intelligence.

---

## 📌 Overview

Sales teams receive leads from different sources such as emails, websites, inquiry forms, chat conversations, and customer messages.

Manually analyzing these leads can take time and may result in inconsistent lead prioritization.

LeadPilot AI solves this problem by analyzing customer conversations and providing:

- Lead Score
- Buying Intent
- Customer Requirements
- Sales Stage
- AI Recommendation
- Lead Summary
- Follow-up Email

The system helps sales teams quickly identify which leads require immediate attention and which leads should be nurtured for later.

---

## 🎯 Problem Statement

Sales teams often receive a large number of leads but do not know which leads are most likely to convert.

Traditional lead management requires sales representatives to manually:

- Read customer conversations
- Understand customer requirements
- Identify purchase intent
- Prioritize leads
- Decide the next action
- Write follow-up emails

This can be time-consuming and inconsistent.

LeadPilot AI automates this initial lead intelligence process.

---

## 💡 Solution

LeadPilot AI analyzes customer conversations using a lead scoring engine.

The system identifies important buying signals such as:

- Budget
- Pricing
- Purchase intent
- Proposal requests
- Contract discussions
- Demo requests
- Urgency
- Timeline
- Interest
- Product comparison
- Evaluation

Based on these signals, the system calculates a lead score and determines the appropriate sales stage and recommendation.

---

## ✨ Key Features

### 1. AI Lead Scoring

Each lead receives a score between 10 and 98 based on customer conversation signals.

Example:

```text
Score: 94
Intent: High
Stage: Proposal
```
---

<img width="1352" height="643" alt="image" src="https://github.com/user-attachments/assets/5a838ca1-be01-4770-85d5-4982613d30b3" />

### 2. Buying Intent Detection

Leads are categorized into three levels:

- **High**
- **Medium**
- **Low**

High-intent leads generally contain stronger purchasing signals such as budget confirmation, pricing requests, proposal requests, demos, or purchase timelines.

---

### 3. Customer Requirement Extraction

The system identifies important requirements from conversations.

Supported requirement keywords include:

- CRM
- Automation
- Analytics
- Integration
- AI
- Dashboard
- Pricing
- Security
- Support
- API
- Reporting
- Demo
- Implementation

---

### 4. Lead Qualification

Based on the calculated score, leads are automatically assigned to different stages.

| Score | Stage |
|---|---|
| 82+ | Proposal |
| 65–81 | Qualified |
| 45–64 | Nurture |
| Below 45 | New |

---

### 5. Sales Recommendations

LeadPilot AI recommends the next action automatically.

Examples:

```text
Send Proposal Now
Schedule Demo
Follow Up in 2 Weeks
Add to Nurture
```

---
### 6. Lead Summary

The system generates a short summary describing the customer's buying intent and requirements.

#### Example

```text
ABC Technologies shows high buying intent.
The conversation indicates interest in CRM,
pricing, demo and implementation.
```

### 7. Follow-up Email Generation

The system automatically generates a follow-up email based on the analyzed lead.

#### Example

```text
Subject: Next steps for ABC Technologies

Hi,

Thank you for discussing your requirements with us.
I would be happy to arrange the next step and answer
any questions.

Please share a suitable time for a follow-up.

Best regards,
Sales Team
```

---

### 8. CSV Bulk Lead Upload

LeadPilot AI supports CSV-based bulk lead processing.

#### Supported Text Columns

```text
conversation
text
message
inquiry
```

#### Optional Columns

```text
company
contact
source
```

---

### 9. Lead Dashboard

The dashboard provides a centralized view of analyzed leads.

It displays:

- **Lead name/company**
- **AI score**
- **Buying intent**
- **Requirements**
- **Sales stage**
- **AI recommendation**
- **Lead overview**

---

### 10. Lead History

Analyzed leads are stored in a SQLite database so previous lead records can be accessed later.

---

## 🧠 Lead Scoring Logic

LeadPilot AI currently uses a rule-based scoring engine.

### Hot Buying Signals

```text
ready to buy
budget
pricing
purchase
proposal
contract
demo
urgent
timeline
```

### Warm Signals

```text
interested
compare
meeting
explore
evaluation
next month
```

### Cold Signals

```text
research
not sure
maybe
later
information
```

The scoring engine combines these signals with conversation length to calculate the final lead score.

---

## 🔄 Application Workflow

```text
Customer Conversation
        ↓
Lead Input
        ↓
Text Analysis
        ↓
Buying Signal Detection
        ↓
Lead Score Calculation
        ↓
Intent Detection
        ↓
Requirement Extraction
        ↓
Sales Stage Classification
        ↓
Recommendation Generation
        ↓
Follow-up Email
        ↓
SQLite Database
        ↓
Dashboard
```

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │   Customer Inquiry   │
                    │ Email / Chat / Form  │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │  Lead Analysis       │
                    │  & Scoring Engine    │
                    └──────────┬───────────┘
                               ↓
              ┌────────────────┼────────────────┐
              ↓                ↓                ↓
        Intent Detection   Requirements     Score
              ↓                ↓                ↓
              └────────────────┼────────────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Sales Stage        │
                    │   Recommendation     │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    SQLite Database   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │    Web Dashboard     │
                    └──────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Database

- SQLite

### Data Processing

- Python CSV module
- Rule-based text analysis
- Keyword-based lead scoring

### Visualization

- Chart.js

---

## 📁 Project Structure

```text
LeadPilot-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── leads.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── app.js
│
└── templates/
    └── dashboard.html
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/prajapatishubham336/LeadPilot-AI.git
```

```bash
cd LeadPilot-AI
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m uvicorn app:app --reload
```

### 5. Open in Browser

```text
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

### Home Dashboard

```text
GET /
```

Displays the LeadPilot AI dashboard.

### Analyze Lead

```text
POST /api/analyze
```

Analyzes a customer conversation and returns:

```text
Score
Intent
Stage
Requirements
Recommendation
Summary
Follow-up Email
```

### Get Leads

```text
GET /api/leads
```

Returns previously analyzed leads.

### Bulk CSV Upload

```text
POST /api/bulk
```

Uploads and analyzes multiple leads from a CSV file.

---

## 🧪 Example

### Input

```text
Company:
ABC Technologies

Contact:
rahul@abctech.com

Source:
Email

Conversation:

We are looking for a CRM solution for our sales team
of 100 employees. Our budget has already been approved
and we are ready to purchase. We would like to see a
demo, compare pricing and features, and receive a
detailed proposal. We are planning to implement the CRM
next month. Please contact us to schedule a meeting.
```

### Output

```text
Score: High

Intent: High

Stage: Proposal

Requirements:
CRM, pricing, demo, implementation

Recommendation:
Send Proposal Now
```

---

## 📊 Lead Qualification Example

### High Intent Lead

```text
Score: 90+
Intent: High
Stage: Proposal
Action: Send Proposal Now
```

### Medium Intent Lead

```text
Score: 50–74
Intent: Medium
Stage: Nurture
Action: Follow Up in 2 Weeks
```

### Low Intent Lead

```text
Score: Below 50
Intent: Low
Stage: New / Nurture
Action: Add to Nurture
```

---

## 🔐 Data Storage

LeadPilot AI stores analyzed lead information in a local SQLite database.

### Stored Information

```text
Company
Contact
Source
Conversation
Summary
Requirements
Intent
Score
Stage
Recommendation
Follow-up Email
Created Date
```

---

## 🚀 Future Scope

The current version uses a rule-based lead scoring engine. Future versions can introduce more advanced AI capabilities.

### Planned Improvements

- LLM-based conversation analysis
- Semantic similarity search
- Sentence embeddings
- Vector database integration
- Advanced lead qualification
- BANT-based scoring
- Predictive lead conversion scoring
- CRM integrations
- Email integration
- WhatsApp integration
- Automated follow-up
- Sales pipeline analytics
- Lead clustering
- Duplicate lead detection
- Real-time lead monitoring
- Advanced reporting
- AI sales assistant

---

## 🎯 Use Cases

LeadPilot AI can be useful for:

- SaaS companies
- B2B sales teams
- CRM companies
- Startups
- Marketing teams
- Sales development teams
- Customer acquisition teams
- Business development teams

---

## 🔮 Vision

The goal of LeadPilot AI is to transform raw customer conversations into actionable sales intelligence.

Instead of asking:

> "Which lead should I contact first?"

Sales teams can use LeadPilot AI to quickly understand:

```text
Who is interested?
        ↓
How strong is the buying intent?
        ↓
What does the customer need?
        ↓
Which sales stage is the lead in?
        ↓
What should the salesperson do next?
```

---

## 👨‍💻 Author

**Shubham Prajapati**

AI/ML and Generative AI

- GitHub: [prajapatishubham336](https://github.com/prajapatishubham336)
- Project: [LeadPilot AI](https://github.com/prajapatishubham336/LeadPilot-AI)
- LinkedIn: [Shubham Prajapati](https://www.linkedin.com/in/shubham-prajapati-103b38393/)

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for personal and commercial purposes, subject to the terms of the MIT License.

