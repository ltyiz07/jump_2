from counter.timer import Timer

a = Timer()
a.start()

global_var = 51

def myfunc():
    global  global_var
    global_var = global_var + 1
    print(global_var)


myfunc()
print(global_var)

a.finish()