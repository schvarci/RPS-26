def hello():
    oddelek=input("Kateri oddelek si? ")
    if oddelek.lower() == "1.ri":
        print(f"Hello <3")
    else:
        print(f"Hello {oddelek}")


def postevanka():
    x = int(input("Izberi število: "))
#While ponavlajl dokler while___: ni resničen
    št = 1
    while št<=10:
        print(f"{št}*{x}={št*x}")
        št += 1     

if __name__=="__main__":
    postevanka()