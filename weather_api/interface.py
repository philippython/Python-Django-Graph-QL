import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette

class player(graphene.Interface):
    name = graphene.String()
    country = graphene.String()

class footballplayer(graphene.ObjectType):
    class Meta:
        interface = (player, )
    position = graphene.Int()


class Cricketplayer(graphene.ObjectType):
    class Meta:
        interface = (player, )
    battlingorder = graphene.Int()