import graphene
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette_graphene3.applications import Starlette
from graphene import ObjectType , String , Int, List 

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