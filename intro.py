from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette
import graphene

class Calculator(graphene.ObjectType):
    concat = graphene.String()
    add = graphene.String()

    def resolve_concat(self, info):
        return "this is concatenation"

    def resolve_add(self, info):
        return "this is addition"

app = Starlette()
schema=graphene.Schema(query=Calculator)
app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE
