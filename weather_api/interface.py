import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette

class player(graphene.Interface):
    name = graphene.String()
    country = graphene.String()

class Footballplayer(graphene.ObjectType):
    class Meta:
        interfaces = (player, )
    position = graphene.Int()


class Cricketplayer(graphene.ObjectType):
    class Meta:
        interfaces = (player, )
    battlingorder = graphene.Int()

class query(graphene.ObjectType):
    fplayer = graphene.Field(Footballplayer)
    cplayer = graphene.Field(Cricketplayer)

    def resolve_fplayer(self, info):
        return {
            "name" : "messi",
            "country" : "argentina",
            "position": 9
        }

    def resolve_cplayer(self, info):
        return {
            "name" : "Shubham",
            "country" : "india",
            "battlingorder" : 10
        }


app = Starlette()
schema = graphene.Schema(query=query)
app.mount("/interface", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))