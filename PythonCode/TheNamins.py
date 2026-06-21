from typing import TypedDict

from pydantic import BaseModel

#defining list with a specific type
names: list[str] =["David","rahul","Vinod","Raju"]

print(names[3])

#defining dict with a specific type
checks:dict[str,str] ={"Name1":"David","Name2":"rahul","Name3":"Raju"}

print(checks["Name1"])


class Movie(TypedDict):
    name: str
    age: int

Burgundy:Movie ={
    "name":"Burgundy","age":56 }

print(Burgundy["name"])
print(type(Burgundy))

class Movie(BaseModel):
    name: str
    age: int

u = Movie(name="David",age=56)
print(type(u))
