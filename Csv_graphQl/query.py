from Csv_graphQl.mapping import Employee
from graphene import ObjectType, List
from mapping import Employee
from data import read_file

class Query(ObjectType):
    employee= List(Employee)

    def employee_resolver(self, info):
        return read_file()

        