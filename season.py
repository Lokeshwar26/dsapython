month=int(input("Enter the numb er of month:"))
if(month==12 or month==1 or month==2):
    print("Season:Autumn")
elif(month==3 or month ==4 or month==5):
    print("Season:Spring")
elif(month==6 or month == 7 or month== 8):
    print("Season:summer")
elif(month==9 or month==10 or  month ==11):
    print("Season:winter")
else:
    print("Invalid month")