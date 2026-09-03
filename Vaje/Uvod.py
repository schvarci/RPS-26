def hello():
    oddelek=input("Kateri oddelek si? ")
    if oddelek.lower() == "1.ri":
        print(f"Hello <3")
    else:
        print(f"Hello {oddelek}")
if __name__=="__main__":
    hello()