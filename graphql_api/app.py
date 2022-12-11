from fastapi import FastAPI
from schema import schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

app = FastAPI()

app.add_route("/all_people", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))

@app.get('/')
async def index():
    return {"Message": "Hello world"}

    