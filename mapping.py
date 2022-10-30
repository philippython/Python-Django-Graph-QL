from ast import Str
from graphene import ObjectType, String

class Employee(ObjectType):
    name=String()
    city=String()
    designation=String()
    experience_in_years=String()