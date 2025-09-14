print("Hola nuevo trabajo")
def print_hello(*argumento):
    if isinstance(argumento,tuple):
        print(argumento)
        print("Hellowor")

a={"ever":"hola"}
print_hello(a)