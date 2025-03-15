from patient import *

class Specialization:
    MAX_CAPACITY = 3
    PATIENT_STATUS_NUMBER = [0,1,2]

    def __init__(self, name):
        self.name = 'Specialization ' + name
        self.queue = []

    def add_new_patient(self, name, status):
        if len(self.queue) >= self.MAX_CAPACITY:
            print('Apologies, the queue is full for the specialization.')
            return
        
        if status not in self.PATIENT_STATUS_NUMBER:
            print('Invalid status. Status should be 0(normal), 1 (urgent), or 2 (super-urgent).')
            while True:
                value = input(str('Again enter status 0(normal), 1 (urgent), or 2 (super-urgent):'))
                if (value == '0') or (value == '1') or (value == '2'):
                    return value
                else:
                    print('Invalid patient status')
                    
        new_pat = Patient(name, status)
        self.queue.append(new_pat)
        self.queue.sort(key=lambda x:x.status, reverse=True)
        print(f'Patient: {new_pat.name} is {self.format_patient_status(new_pat.status)}')

    def get_next_patient(self):
        if len(self.queue) == 0:
            print('The Queue is empty')
            return
        next_patient = self.queue.pop(0)
        print(f'{next_patient.name}, Please go with the Dr')

    def remove_patient(self, name):
        patients_to_remove = [patient for patient in self.queue if patient.name == name]

        for patient in patients_to_remove:
            self.queue.remove(patient)
        return len(patients_to_remove)>0
    
    def print_patient(self):
        patients = [patient for patient in self.queue]
        for patient in patients:
            print(f'Patient: {patient.name} is {self.format_patient_status(patient.status)}')

    def is_full(self):
        return len(self.queue) >= self.MAX_CAPACITY
    
    def __str__(self):
        return f"{self.name}: There are {len(self.queue)} patients"

    
    @staticmethod
    def format_patient_status(status):
        if status == 0:
            return 'Normal'
        elif status == 1:
            return 'Urgent'
        else:
            return 'Super-Urgent'
        
# spec0 = Specialization('Cardiology')
# spec1 = Specialization('Neurology')
# spec0.add_new_patient('amna', 1)
# spec0.add_new_patient('lubna', 1)
# spec0.add_new_patient('zulikha', 0)
# spec0.add_new_patient('tania', 2)
# spec1.add_new_patient('warda',0)
# print(spec0.is_full())
# print(spec0.name)
# print(len(spec0.queue))
# spec0.get_next_patient()
# spec0.print_patient()
# spec0.__str__()