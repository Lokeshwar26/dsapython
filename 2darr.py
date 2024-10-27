c_num =int(input("Number of columns :"))
r_num=int(input("Number of rows:"))
twod_arr =[[0 for col in range(c_num)]for row in range(r_num)]
for row in range(r_num):
    for col in range(c_num):
        twod_arr[row][col]=row*col

print(twod_arr)