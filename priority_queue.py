import heapq
import time

class Patient:
    def __init__(self, name, severity, arrival_time=None):
        self.name = name
        self.severity = severity
        self.arrival_time = arrival_time or time.time()

    def __lt__(self, other):
        return (-self.severity, self.arrival_time) < (-other.severity, other.arrival_time)

class PriorityQueueManager:
    def __init__(self):
        self.heap = []

    def add_patient(self, patient):
        heapq.heappush(self.heap, patient)

    def get_next_patient(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def get_all_patients(self):
        return sorted(self.heap)