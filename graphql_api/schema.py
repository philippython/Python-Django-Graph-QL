from graphene import ObjectType, String , Int, List, Schema
from models import data

class PersonType(ObjectType):
    email = String()
    age = Int()
    first_name = String()
    last_name = String()

    def resolve_email(person, info):
        return person.email

    def resolve_age(person, info):
        return person.age

    def resolve_first_name(person, info):
        return person.first_name
    
    def resolve_last_name(person, info):
        return person.last_name

class Query(ObjectType):
    all_people = List(PersonType)

    def resolve_all_people(root, info):
        return  data.values()


schema = Schema(query=Query)

print(schema.execute("{allPeople{email lastName}}"))
