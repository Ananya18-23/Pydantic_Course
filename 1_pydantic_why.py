from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact_details: Dict[str, str]
    
def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')    
    
patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'email': 'abc@gmail.com', 'phone': "123-456-78900"}}

patient1 = Patient(**patient_info)       

update_patient_data(patient1)