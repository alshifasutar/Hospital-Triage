document.getElementById('patientForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const severity = document.getElementById('severity').value;

    const response = await fetch('/add_patient', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, severity })
    });

    const result = await response.json();
    alert(result.message || result.error);
    loadWaitingList();
});

async function getNextPatient() {
    const response = await fetch('/next_patient');
    const data = await response.json();
    const div = document.getElementById('nextPatient');
    div.innerText = data.name ? `${data.name} (Severity: ${data.severity})` : data.message;
}

async function loadWaitingList() {
    const response = await fetch('/waiting_list');
    const data = await response.json();
    const list = document.getElementById('waitingList');
    list.innerHTML = '';
    data.forEach(p => {
        const li = document.createElement('li');
        li.innerText = `${p.name} - Severity: ${p.severity}`;
        list.appendChild(li);
    });
}