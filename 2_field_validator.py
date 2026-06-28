from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        
        valid_domains = ['hdfc.com', 'gmail.com', 'yahoo.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid_domains')
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()  
    
    
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
           return value
        else:
           raise ValueError('Age should be between 0 and 100')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')    
    
patient_info = {
    'name': 'John Doe',
    'email': 'abc@hdfc.com',
    'age': 30,
    'weight': 70.5,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '123-456-78900'}
}

patient1 = Patient(**patient_info)   # validation -> type coercion -> field validator

update_patient_data(patient1)    