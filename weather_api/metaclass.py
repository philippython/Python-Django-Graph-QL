from graphene import ObjectType, String, Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette


class myQuery(ObjectType):
    hello=String()

    def resolve_hello(self, info):
        return "Hello world!!!"

app = Starlette()
app.mount("/graphql", GraphQLApp(schema=Schema(query=myQuery), on_get=make_graphiql_handler()))