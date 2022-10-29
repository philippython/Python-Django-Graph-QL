from graphene import ObjectType, Int, String

class Employee(ObjectType):
    name=String()
    city=String()
    designation=String()
    experience_in_years=Int()