from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp
import graphene

class Calculator(graphene.ObjectType):
    concat = graphene.String()
    add = graphene.String()

    def resolve_concat(self, info):
        return "this is concatenation"

    def resolve_add(self, info):
        return "this is addition"

app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Calculator)))


# How are you doing?

# I hope you're fine, Have you started your exams 

# I wish you best of luck

# i wouldn't like to disturb with texts but i also can't help it not to check up on you :)
