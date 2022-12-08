from graphene import ObjectType, String, Schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette


class myQuery(ObjectType):

    class Meta:
        name  = "typeofmetaclass"
        description = "description from metaclass"

    hello=String()
    bye=String()

    def resolve_hello(self, info):
        return "Hello world!!!"

    def resolve_bye(self, info):
        return "Bye"
app = Starlette()
app.mount("/graphql", GraphQLApp(schema=Schema(query=myQuery), on_get=make_graphiql_handler()))