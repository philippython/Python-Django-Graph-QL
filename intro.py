# from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette
import graphene

class Calculator(graphene.ObjectType):
    concat = graphene.String(a=graphene.String(), b=graphene.String())
    add = graphene.String(a=graphene.Int(), b=graphene.Int())

    def resolve_concat(self, info, a, b):
        return a + "" + b

    def resolve_add(self, info, a, b):
        return a + b

app = Starlette()
schema=graphene.Schema(query=Calculator)
app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE
