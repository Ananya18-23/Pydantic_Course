from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            min_length=2,
            max_length=50,
            title='Name of the patient',
            description='This is the name of the patient',
            examples=['John Doe', 'Ananya']
        )
    ]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Optional[bool] = Field(default=None, description='Married status of the patient')
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('updated')


patient_info = {
    'name': 'John Doe',
    'email': 'abc@gmail.com',
    'linkedin_url': 'https://www.linkedin.com/in/johndoe',
    'age': 30,
    'weight': 70.5,
    'married': True,
    'contact_details': {'phone': '123-456-78900'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)