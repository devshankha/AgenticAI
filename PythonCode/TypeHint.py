from typing import List, Tuple, Union

age:int = 25
print(age)

def show(name:str)->str:
    return name.upper()
print(show("my name is "))

num:List[int] = [1,2,3,4,5]
print(num)

num1:Tuple[int]=(1,2,3,4,5)
print(num1)

def get_user_rank(points: int) -> str | None:
    if points > 100:
        return "Gold"
    return None

c = get_user_rank(10)
print(c)


def divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    else:
        return a / b

m=divide(6,2)
print(m)

def convert_value(val: Union[str, float]) -> Union[int, str]:
    if isinstance(val, float):
        return int(val)
    return str(val)