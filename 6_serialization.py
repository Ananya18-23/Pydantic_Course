from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin_code: str

class Patient(BaseModel):
    
    name: str
    email: str
    age: int
    address: Address
    
address_dict={'city': 'gurgaon', 'state': 'haryana', 'pin_code': '122001'}    

address1 = Address(**address_dict)


patient_dict = {'name': 'ananya', 'email': 'ananya@example.com', 'age': 25, 'address': address1}

patient1 = Patient(**patient_dict)   

temp = patient1.model_dump()  # This will return a dictionary representation of the patient1 object 

print(temp)
print(type(temp))

temp = patient1.model_dump(include=['name'])



tem1 = patient1.model_dump_json()  # This will return a JSON string representation of the patient1 object

print(tem1)
print(type(tem1))