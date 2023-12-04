''' >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    Data Types In Python    ----->>>
    1. Integers         2. Floating Points      3. STrings          4. Lists
    5. Dictonaries      6. Tuples               7. Sets             8. Booleans

    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

a = 1234                                    
b = 1234.12                                 
c = 'Atul Patel'                            
d = ", Welcome to the world of Python!!"    
e = [10, "It's me", 120.01]                 
f = {"mykey":"Value","name":"Mr. Patel"}    
g = (10, "It's me", 120.01)        
h = {"a","b"}
i = True

print("type of a : ", type(a), "\n", "type of b : ", type(b), "\n", "type of c : ", type(c), "\n", "type of d : ", type(d))
print("type of e : ", type(e), "\n", "type of f : ", type(f), "\n", "type of g : ", type(g), "\n", "type of h : ", type(h))
print("type of i : ", type(i))

''' >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Arithmetic Computation
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
print("\n","Arithmetic Computation")
a=25/4; print("25/4 Division  - ", a)
b=25%4; print("25%4 Remainder - ", b)
c=24%4; print("24%4 Remainder - ", c)
d=2**3; print("2**3 Power     - ", d)

''' >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    String Handling - An Ordered, Immutable Sequence of data. Hence allows Indexing, Slicing.

        Basics
            1. Immutable - Cannot assign a new value using Indexes
            2. Concatenation
            3. Repetition of String or characters
            
               String Attributes -> string_variable. using dot(.)
            4. String Attributes - Upper Case
            5. String Attributes - Lower Case
            6. String Attributes - Split
            7. String Attributes - Split at any specific character but character gets excluded

        Index is used inside [] bracket & starts with 0(zero). 
            Eg: my_string[0] displays the very first letter of thye string.
            Character: Hi!, Welcome to the world of Python
            Index    : 0123456789....
            Rev Index: 0.........................987654321 -> in negative
        
        Slicing:Allows to get a part of the STring
            Eg:  [start:stop:step] where start, stop are the indexes & step is a jump

                1. Slicing to get string starting from a position thru the end
                2. Slicing to get string from begining till a certain position
                3. Slicing to get a pa strt of string
                4. Slicing to get a part ofring with STEP=2
                5. Slicing to get a part of string with STEP=2 from the whole string
                6. Slicing to Reverse String
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''

my_first_string = "Hi!, Welcome to the world of Python."

print("\n","String Handling - Basics")
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

print("\n","String Handling - Indexing")
print(my_first_string[0], "\n", my_first_string[1], "\n", my_first_string[2])   # 1. Forward Indexing
print(my_first_string[0], "\n", my_first_string[-1], "\n", my_first_string[-2]) # 2. Reverse Indexing

print("\n","String Handling - Slicing")
print(my_first_string[8])
print(my_first_string[8:])          # 1. Slicing to get string starting from a position thru the end
print(my_first_string[11])      
print(my_first_string[:11])         # 2. Slicing to get string from begining till a certain position, It doesn't include STOP Index (upto but don't include) !!! <IMPORTANT>> !!!!!!
print(my_first_string[24])
print(my_first_string[8:24])        # 3. Slicing to get a part of string
print(my_first_string[8:24:2])      # 4. Slicing to get a part of string with STEP=2
print(my_first_string[::2])         # 5. Slicing to get a part of string with STEP=2 from the whole string
print(my_first_string[::-1])        # 6. Slicing to Reverse String
#print(my_first_string[::0])        # Slice STep can't be Zero

