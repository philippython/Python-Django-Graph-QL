from webbrowser import Grail
import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette
from graphene import ObjectType , String , Int, List , Schema 

data = [
    {
        "name": "philip",
        "city": "ontario"
    },
    {
        "name": "john",
        "city": "ottawa"
    },
    {
        "name": "blessing",
        "city": "halmiton"
    }
]

class Student(ObjectType):
    name= String()
    city = String()

class Person(ObjectType):
    student = List(Student)

    def resolve_student(self, info):
        return data


app = Starlette()
schema = Schema(query=Person)
app.mount("/students", GraphQLApp(schema, on_get=make_graphiql_handler()))