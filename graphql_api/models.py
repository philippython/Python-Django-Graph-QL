from collections import namedtuple

Person = namedtuple("Person", ["email", "age", "first_name", "last_name"])

data = {
    1 : Person("johndeo@gmail.com", 22, "john", "deo"),
    2 : Person("jerryblue", 20, "jerry", "blue"),
    3 : Person("jaradhiggins@gmail.com", 21, "juice", "anthony"),
    4 : Person("odulajaphilip@gmail.com", 18, "odulaja", "philip")
}