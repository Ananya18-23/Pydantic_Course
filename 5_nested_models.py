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

print(patient1)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.name)