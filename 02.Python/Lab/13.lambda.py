people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# First Way
def f(person):
    return person["name"]
    # return person["house"]

people.sort(key=f)

# Second Way
people.sort(key=lambda person: person["name"])

print(people)