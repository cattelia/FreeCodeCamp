name = 0
age = "Sara"

def test_type(name: str, age: int):
    print(name, age)
    name = name
    print(name, age)
    age = age
    print(name, age)
   
test_type(name, age)         