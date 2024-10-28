ece=int(input("enter the number of students placed in ece:"))
cse=int(input("enter the number of students placed in cse:"))
mech=int(input("enter the number of students placed in mech:"))

if(ece<0 or cse<0 or mech<0):
    print("input is invalid")
elif(ece==cse and ece==mech):
    print("None of the department has got the highest placement")
else:
    print("Highest placement:")
    m=max(ece,cse,mech)
    if(ece==m):
        print('ece')
    if(cse==m):
        print("cse")
    if(mech==m):
        print('mech')