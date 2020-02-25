# zadacha5
vyr = int(input("Vvedyte vyruchku: "))
izd = int(input("Vvedyte izderzhki: "))
if vyr > izd:
    prib = vyr - izd
    rent = prib/vyr
    print(f"Good job! Your profit: {prib}")
    rab = int(input("Kolichestvo rabochih: "))
    print(f"{prib/rab} na rabochego" )
elif vyr == izd:
    print("V 0")
else:
    print("V ubytok")

