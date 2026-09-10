x = 5
y = 15
z = -10

#operacije nad intom
print(x+y)
print(x-z)
print(x*z)
print(x/z)


# Deljenej z ostankom
print(10 % 2)
print(11 % 2)

# Celo številsko deljenje
print(10//3)


# Potenca
print(10**3)


# decimalna ali float števila

x = 3.14
y = 10.0


print(0.5 + 0.5 == 1)
print(0.1 + 0.3 == 0.4)

#string - niz znakov
ime = "Luka"
print(len(ime))
#print(st + st)
#print(int(st)+ 100)


naslov = "Kidričeva 55"
print(naslov.upper())
print(naslov.lower())


ime = "patrik Cvetan" #P.C.
ime = ime.upper() #PATRIK CVETAN
splitime = ime.split()
print(type(splitime))
print(splitime)

ime = splitime[0]
pri = splitime[1]
print(ime[0],pri[0])
print(f"{ime[0]}.{pri[0]}.")