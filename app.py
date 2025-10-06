from flask import Flask, render_template, request, jsonify
from priority_queue import Patient, PriorityQueueManager
from models import init_db, add_patient_to_db, fetch_patients # type: ignore
import time

app = Flask(__name__)
pq = PriorityQueueManager()
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['POST'])
def add_patient():
    try:
        data = request.get_json()
        name = data['name']
        severity = int(data['severity'])
        arrival_time = time.time()
        patient = Patient(name, severity, arrival_time)
        pq.add_patient(patient)
        add_patient_to_db(name, severity, arrival_time)
        return jsonify({'message': 'Patient added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/next_patient', methods=['GET'])
def next_patient():
    try:
        patient = pq.get_next_patient()
        if patient:
            return jsonify({'name': patient.name, 'severity': patient.severity}), 200
        else:
            return jsonify({'message': 'No patients in queue'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/waiting_list', methods=['GET'])
def waiting_list():
    try:
        patients = pq.get_all_patients()
        return jsonify([
            {'name': p.name, 'severity': p.severity, 'arrival_time': p.arrival_time}
            for p in patients
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)