from graphene import ObjectType, String, Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette

class myQuery(ObjectType):
    hello =  String()

    def resolve_hello(self,info):
        return "Hello World"

app = Starlette()
schema = Schema(query=myQuery)
app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))