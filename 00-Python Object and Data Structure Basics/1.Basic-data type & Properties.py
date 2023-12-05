# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
#    Data Types In Python    ----->>>
#    1. Integers         2. Floating Points      3. STrings          4. Lists
#    5. Dictonaries      6. Tuples               7. Sets             8. Booleans
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\n-->Types of Objects/Data in Python")
a = 1234                                    
b = 1234.12                                 
c = 'Atul Patel'                            
d = ", Welcome to the world of Python!!"    
e = [10, "It's me", 120.01]                 
f = {"mykey":"Value","name":"Mr. Patel"}    
g = (10, "It's me", 120.01)        
h = {"a","b"}
i = True

print("type of a : ", type(a), "\ntype of b : ", type(b), "\ntype of c : ", type(c), "\ntype of d : ", type(d))
print("type of e : ", type(e), "\ntype of f : ", type(f), "\ntype of g : ", type(g), "\ntype of h : ", type(h), "\ntype of i : ", type(i))

#    Response:
#    type of a :  <class 'int'> 
#    type of b :  <class 'float'> 
#    type of c :  <class 'str'> 
#    type of d :  <class 'str'>
#    type of e :  <class 'list'> 
#    type of f :  <class 'dict'> 
#    type of g :  <class 'tuple'> 
#    type of h :  <class 'set'> 
#    type of i :  <class 'bool'> '''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#    Arithmetic Computation
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("\n-->Arithmetic Computation")
a=25/4; print("25/4 Division  - ", a) # 25/4 Division  -  6.25
b=25%4; print("25%4 Remainder - ", b) # 25%4 Remainder -  1
c=24%4; print("24%4 Remainder - ", c) # 24%4 Remainder -  0
d=2**3; print("2**3 Power     - ", d) # 2**3 Power     -  8

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#    String Handling - An Ordered, Immutable Sequence of data. Hence allows Indexing, Slicing.
#
#        Basics
#            1. Immutable - Cannot assign a new value using Indexes
#            2. Concatenation
#            3. Repetition of String or characters
#            
#               String Attributes -> string_variable. using dot(.)
#            4. String Attributes - Upper Case
#            5. String Attributes - Lower Case
#            6. String Attributes - Split
#            7. String Attributes - Split at any specific character but character gets excluded
#
#        Index is used inside [] bracket & starts with 0(zero). 
#            Eg: my_string[0] displays the very first letter of thye string.
#            Character: Hi!, Welcome to the world of Python
#            Index    : 0123456789....
#            Rev Index: 0.........................987654321 -> in negative
#        
#        Slicing:Allows to get a part of the STring
#            Eg:  [start:stop:step] where start, stop are the indexes & step is a jump
#
#                1. Slicing to get string starting from a position thru the end
#                2. Slicing to get string from begining till a certain position
#                3. Slicing to get a pa strt of string
#                4. Slicing to get a part ofring with STEP=2
#                5. Slicing to get a part of string with STEP=2 from the whole string
#                6. Slicing to Reverse String
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_first_string = "Hi!, Welcome to the world of Python."

print("\n-->String Handling - Basics")
mySecondString = "This year-"
MyThirdString = " we will learn all about Python."
concatenated_String = my_first_string + mySecondString + '20' + str(23) + "," + MyThirdString
#my_first_string[0] = 'N'           # 1. Immutable - Cannot assign a new value using Indexes
print(concatenated_String)          # 2. Concatenation
print("W" + "o"*3 + 'w!')           # 3. Repetition of String or characters
print(my_first_string.upper())      # 4. String Attributes - Upper Case
print(my_first_string.lower())      # 5. String Attributes - Lower Case
print(my_first_string.split())      # 6. String Attributes - Split
print(my_first_string.split('t'))   # 7. String Attributes - Split at any specific character but character gets excluded

#    Response: String Handling - Basics
#    Hi!, Welcome to the world of Python.This year-2023, we will learn all about Python.
#    Wooow!
#    HI!, WELCOME TO THE WORLD OF PYTHON.
#    hi!, welcome to the world of python.
#    ['Hi!,', 'Welcome', 'to', 'the', 'world', 'of', 'Python.']
#    ['Hi!, Welcome ', 'o ', 'he world of Py', 'hon.'] '''

print("\n-->String Handling - Indexing")
print('ind=0:',my_first_string[0], "ind=1:",my_first_string[1], "ind=2:",my_first_string[2])       # 1. Forward Indexing
print('ind=0:',my_first_string[0], "ind=-1:", my_first_string[-1], "ind=-2:", my_first_string[-2]) # 2. Reverse Indexing

#    Response: Indexing
#    ind=0: H ind=1: i ind=2: !
#    ind=0: H ind=-1: . ind=-2: n '''

print("\n-->String Handling - Slicing")
print(my_first_string[8])
print(my_first_string[8:])          # 1. Slicing to get string starting from a position thru the end
print(my_first_string[11])      
print(my_first_string[:11])         # 2. Slicing to get string from begining till a certain position, 
                                    #    It doesn't include STOP Index (upto but don't include) !!! <IMPORTANT>> !!!!!!
print(my_first_string[24])
print(my_first_string[8:24])        # 3. Slicing to get a part of string
print(my_first_string[8:24:2])      # 4. Slicing to get a part of string with STEP=2
print(my_first_string[::2])         # 5. Slicing to get a part of string with STEP=2 from the whole string
print(my_first_string[::-1])        # 6. Slicing to Reverse String
#print(my_first_string[::0])        # Slice STep can't be Zero

#    Response: String Handling - Slicing
#    c
#    come to the world of Python.
#    e
#    Hi!, Welcom
#    d
#    come to the worl
#    cm otewr
#    H! ecm otewrdo yhn
#    .nohtyP fo dlrow eht ot emocleW ,!iH '''