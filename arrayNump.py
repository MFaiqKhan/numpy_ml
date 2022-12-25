import numpy as np; """ import numpy as np """

"""-----------------------------------------------------------------------------"""

a = np.array([1,2,3,4,5,6,7,8,9,10]); " this is a array of 10 elements "
print(a); " print the array "

y = np.array(a); """" this is a copy of array a """

print(y); " print the copy of array a "
print(a[0]); " print the first element of array a "
print(type(y)); " print the type of array y "
print(y.ndim); " print the dimension of array y "

"""-----------------------------------------------------------------------------"""
" print the array from input"

l = [] # intializing the empty list

for i in range(1,5) : # for loop from 1 to 5, 5 is not included
    int_1 = int(input("Enter :"))   # input by default is string, so we need to convert it to int
    l.append(int_1) # append the input to list l

print(l) # print the list l


"""-----------------------------------------------------------------------------"""

ar3 = np.array([[[2,3,1,4],[5,6,7,8],[9,10,11,12]]]) # 3D array
print(ar3) # print the 3D array
print(ar3.ndim) # print the dimension of 3D array

"""-----------------------------------------------------------------------------"""

arn = np.array([1,2,3,4],ndmin=10) # 10D array, can create any dimension using ndmin
print(arn) # print the 10D array
print(arn.ndim) # print the dimension of 10D array

"""-----------------------------------------------------------------------------"""	
#########Special Types of arrays ###########

# Zeros

ar_zero = np.zeros(7) # create an array of 7 zeros
print(ar_zero) # print the array of zeros
ar_zero1 = np.zeros((3,4)) # create an array of 3*4  , 2D array of zeros
print(ar_zero1) # print the array of zeros

# Ones

ar_ones = np.ones(7) # create an array of 7 ones
print(ar_ones) # print the array of ones
ar_ones1 = np.ones((3,4)) # create an array of 3*4  , 2D array of ones
print(ar_ones1) # print the array of ones

# Empty

ar_empty = np.empty(7) # create an array of 7 empty
print(ar_empty) # print the array of empty, // empty array is not zero, it is previous value of that memory location

# arrange 

ar_arrange = np.arange(1,10,2) # create an array of 1 to 10 with step 2
print(ar_arrange) # print the array of arange

# diagonal

ar_diagonal = np.diag([1,2,3,4]) # create an array of diagonal
# why the diagonal array is 2D array, because it is a matrix
print(ar_diagonal) # print the array of diagonal

# linspace

ar_linspace = np.linspace(1,20,3) # create an array of 1 to 10 with 5 elements showing the difference
print(ar_linspace) # print the array of linspace

# constant 

ar_constant = np.full((3,4),5) # create an array of 3*4 with constant value 5
print(ar_constant) # print the array of constant

"-----------------------------------------------------------------------------"

######## Random valued arrays ########

# rand() # function is used to generate random value between 0 to 1

var = np.random.rand(5) # create an array of 5 random values
print(var) # print the array of random values
var = np.random.rand(2,3) # create an array of 2*3 random values
print(var) # print the array of random values


# randn() # function is used to generate random value between close to 0  , both positive and negative

var = np.random.randn(5) # create an array of 5 random values
print(var) # print the array of random values


# randf() # Returns random floats in the half-open interval [0.0, 1.0) ,  1.0 is not included

var = np.random.ranf(5) # create an array of 5 random values
print(var) # print the array of random values

# randint() # Returns random integers from low (inclusive) to high (exclusive), 
# this function takes range as input argument

total_values = 5
min_1 = 1
max_20 = 10

var = np.random.randint(min_1,max_20,total_values) # create an array of 5 random values
print(var) # print the array of random values



"""-----------------------------------------------------------------------------"""

## Datatype

var = np.array([1,2,3,4]) # create an array of 4 elements
print("Data type : ", var.dtype) # print the data type of the array

var = np.array([1.0,2.0,3.0]) 
print("Data type : ", var.dtype)

var = np.array(["A", "B", "C"])
print("Data type : ", var.dtype)



# converting list to ndarray

l = [1,2,3,4,5,6,7,8,9,10]
a = np.asarray(l); # convert list to ndarray , asarray() function is used to convert list to ndarray
print(a) # print the array

