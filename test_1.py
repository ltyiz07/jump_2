global_var = 51

def myfunc():
    global_var = global_var + 1
    print(global_var)


myfunc()
print(global_var)