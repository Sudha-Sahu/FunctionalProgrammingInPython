
# taking number of rows and column from user
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

# Initialize 2D Array
array = []
print("Enter the values in array :")

# nested for loop for entering value in 2d array
for i in range(row):
    _1d_array = []
    for j in range(col):
        _1d_array.append(int(input()))
    array.append(_1d_array)

# nested For loop for printing the 2d array
print("The matrix representation of 2D array is : ")
for i in range(row):
    for j in range(col):
        print(array[i][j], end=" ")
    print()

