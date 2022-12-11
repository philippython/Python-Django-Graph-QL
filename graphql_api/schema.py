from graphene import ObjectType, String , Int, List, Schema
from starlette_graphene3 import GraphQLApp , make_graphiql_handler
from starlette.applications import Starlette
from fastapi import FastAPI
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
app = FastAPI()

@app.get('/')
async def index():
    return {"Message": "Hello world"}
# app = Starlette()
# app.mount("/all_people", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))
