def add(a,b):
    return a + b

def table_(nombre):

    for i in range(11):
        input("Vous voulez commecez ? Y/N")
        print(f"{i} X {nombre} = {i*nombre}")

table_(7)