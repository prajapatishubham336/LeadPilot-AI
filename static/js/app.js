const modal = document.getElementById('modal');

function openModal() {
    modal.style.display = 'flex';
}

function closeModal() {
    modal.style.display = 'none';
}

document.getElementById('leadForm').addEventListener('submit', async e => {
    e.preventDefault();

    const r = await fetch('/api/analyze', {
        method: 'POST',
        body: new FormData(e.target)
    });

    const d = await r.json();

    document.getElementById('result').textContent = `
Score: ${d.score}
Intent: ${d.intent}
Stage: ${d.stage}
Requirements: ${d.requirements}
Recommendation: ${d.recommendation}

${d.summary}

Follow-up Email:
${d.followup}
`;

    setTimeout(() => location.reload(), 5000);
});

window.onclick = e => {
    if (e.target === modal) {
        closeModal();
    }
};