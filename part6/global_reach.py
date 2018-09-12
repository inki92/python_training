def read_global():
    print("read_global = ", value)
def shadow_global():
    value = -10
    print("shadow_global = ", value)
def change_global():
    global value
    value = -5
    print(value)
value = 10
read_global()
shadow_global()
change_global()
print(value)
