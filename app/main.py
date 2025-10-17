class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age 
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = []
    for p in people:
        person = Person(p["name"], p["age"])
        result.append(person)
    for p in people:
        me = Person.peolpe[p["name"]]
        if "wife" in p and p["wife"] is not None:
            setattr(me, "wife", Person.people[p["wife"]])
        if "husband" in p and p["husband"] is not None:
            setattr(me, "husband", Person.people[p["husband"]])

    return result
