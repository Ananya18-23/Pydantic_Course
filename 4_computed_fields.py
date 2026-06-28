from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float   # kg
    height: float   # mts
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
  
def update_patient_data(patient: Patient):
         print(patient.name)
         print(patient.email)
         print(patient.age)
         print('BMI:', patient.calculate_bmi)
         print(patient.allergies)
         print(patient.contact_details)
         print('updated')
         
         
patient_info = {
    'name': 'John Doe',
    'email': 'abc@hdfc.com',
    'age': 65,
    'weight': 70.5,
    'height': 1.75,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '123-456-78900', 'emergency': '987-654-3210'}
}

patient1 = Patient(**patient_info)   

update_patient_data(patient1)        