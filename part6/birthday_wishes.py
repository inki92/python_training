def birthday1(name, age):
    print("Hello, ", name, ". Your age is ", age)
def birthday2(name = "Alex", age = "26"):
    print("Hello ", name, ". Your age is ", age)
birthday1("Kate", 5)
birthday1(5, "Kate")
birthday1(name = "Kate", age = 5)
birthday1(age = 5, name = "Kate")
birthday2()
birthday2(age = 5)
birthday2(name = "Kate")
birthday2(name = "Kate", age = 5)
birthday2("Kate", 5)
