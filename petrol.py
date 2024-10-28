ltt=int(input("enter the no of litres to fill the tank"))
lt=int(input('Enter the distance covered'))
if(lt<1):
    print(lt," is a Invalid input")
hundred = (ltt/lt)*100
print(round(hundred,2),"Litres/100km")
miles=lt*0.6214
galoons=ltt*0.2642
mg=miles/galoons
print(round(mg,2),"miles/galoons")
