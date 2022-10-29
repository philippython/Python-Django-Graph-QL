from Csv_graphQl.mapping import Employee
from graphene import ObjectType, List,Schema, GraphQLApp
from starlette_graphene3 import Starlette, make_graphiql_handler
from mapping import Employee
from data import read_file

class Query(ObjectType):
    employee= List(Employee)

    def employee_resolver(self, info):
        return read_file()

app = Starlette()
schema = Schema(query=Query)
app.mount("/employees", GraphQLApp(schema=schema), on_get=make_graphiql_handler())