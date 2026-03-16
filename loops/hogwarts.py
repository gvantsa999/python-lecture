students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"}
]

print(f"{'ID':<4} {'NAME':<12} {'HOUSE':<15} {'PATRONUS':<20}")
print("-" * 55) # გამყოფი ხაზი

for i, student in enumerate(students, start=1):

    name = student["name"]
    house = student["house"]
    patronus = student["patronus"]

    print(f"{i:<4} {name:<12} {house:<15} {patronus:<20}")