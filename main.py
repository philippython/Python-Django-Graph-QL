from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette
import graphene

class Course(graphene.ObjectType):
    name = graphene.String(name=graphene.String())
    duration = graphene.Int(dur=graphene.Int())

    def resolve_name(self, info, name):
        return name

    def resolve_duration(self, info, dur):
        return dur

app = Starlette()
app.mount("/course", schema=graphene.Schema(GraphQLApp(query=Course)), on_get=make_graphiql_handler())