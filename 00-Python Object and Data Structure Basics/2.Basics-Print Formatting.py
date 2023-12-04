''' >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    Print Formatting
        1. Concatenation
        2. String Formatting - placeholders using the modulo % character.
            %s or str(); %r or repr()
           Padding and Precision of Floating Point Numbers
                Format -> %length.precisionf
        3. String Formatting - using the .format() string method.
           format-'String here {} then also {}'.format('something1','something2')     
           Advantages Of .fortmat over Placeholders
                a. Inserted objects can be called by index position
                    format - 'String here {1} then also {0}'.format('something1','something2')
                b. Inserted objects can be assigned keywords
                    Format - 'String here {b} then also {a}'.format(a = 'something1',b = 'something2')
                c. Inserted objects can be reused, avoiding duplication
                    Format - 'String here {a} then also {a}'.format(a = 'something')
                d. Alignment, padding and precision with .format()
        4. String Formatting - The newest method, introduced with Python 3.6, uses formatted string literals, called f-strings.
            # In Python 3.6, f-strings offer several benefits over the older .format() string method described above.
            # For one, you can bring outside variables immediately into to the string rather than pass them as arguments through .format(var).
            # Pass !r to get the string representation:
            # Float formatting follows "result: {value:{width}.{precision}}"
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
my_first_string = "Hi!, Welcome to the world of Python."
mySecondString = "This year-2023,"
MyThirdString = " we will learn all about Python."
concatenated_String = my_first_string + mySecondString + MyThirdString
print(concatenated_String)          # 1. Concatenation

''' Result: String Concatenation
    Hi!, Welcome to the world of Python.This year-2023, we will learn all about Python. '''

# 2. String Formatting - placeholders using the modulo % character.
    # Method_1 = using %s or str()
_string1 = "Hello %s! "
_string2 = "Its a %s weather %s."
_formattedStringWIthPlaceholder = _string1%("Everyone") + _string2%("nice", "outside")
print(_formattedStringWIthPlaceholder)

    # Method_2 = using %r or repr() -> deliver the string representation of the object, including quotation marks and any escape characters.
_string1 = "Hello %s! "
_string2 = "Its a %r weather %s."
_formattedStringWIthPlaceholder = _string1%("Everyone") + _string2%("nice", "outside")
print(_formattedStringWIthPlaceholder)

''' Result: String Formatting - %s and %r
    Hello Everyone! Its a nice weather outside.
    Hello Everyone! Its a 'nice' weather outside.'''

        # Padding and Precision of Floating Point Numbers
print("\nPadding and Precision of Floating Point Numbers")
print('Floating point numbers: %5.2f' %(13.144))
print('Floating point numbers: %1.0f' %(13.144))
print('Floating point numbers: %1.5f' %(13.144))
print('Floating point numbers: %10.2f' %(13.144))
print('Floating point numbers: %25.2f' %(13.144))

''' Result: Padding and Precision of Floating Point Numbers
    Floating point numbers: 13.14
    Floating point numbers: 13
    Floating point numbers: 13.14400
    Floating point numbers:      13.14
    Floating point numbers:                     13.14'''

# 3. String Formatting - using the .format() string method.
    # 'String here {} then also {}'.format('something1','something2')
_string1 = "Hello {}! "
_string2 = "Its a {} weather {}."
_formattedStringWIthDotFormat = "Dot Format - " + _string1.format("Everyone") + _string2.format("nice", "outside")
print(_formattedStringWIthDotFormat) 

    # Advantages Of .fortmat over Placeholders
_String = "Hello {2}!, Its a {0} weather {1}."
        # a. Inserted objects can be called by index position:
_string_index_position = _String.format("hot","outside","All")
print(_string_index_position)

        # b. Inserted objects can be assigned keywords:
_String = "Hello {c}!, Its a {b} weather {a}."
_string_assign_keyword = _String.format(a ="outside",b = "hot",c =  "All")
print(_string_assign_keyword)

        # c. Inserted objects can be reused, avoiding duplication:
_String = "A {p} saved is a {p} earned."
_string_keyword_reuse = _String.format(p ="penny")
print(_string_keyword_reuse)

''' Result
    Dot Format - Hello Everyone! Its a nice weather outside.
    Hello All!, Its a hot weather outside.
    Hello All!, Its a hot weather outside.
    A penny saved is a penny earned.'''

        # d. Alignment, padding and precision with .format()
            # Within the curly braces we can assign field lengths, left/right alignments, rounding parameters and more
print("\nAlignment, padding and precision with .format()")
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

            # By default, .format() aligns text to the left, numbers to the right. You can pass an optional <,^, or > to set a left, center or right alignment:
print("\n")
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33.1))

            # You can precede the aligment operator with a padding character

print("\nPadding Characters")
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
''' Result: 
    Alignment, padding and precision with .format()
    Fruit    | Quantity
    Apples   |       3.0
    Oranges  |        10

    Left     |  Center  |    Right
    11       |    22    |     33.1

    Padding Characters
    Left==== | -Center- | ...Right
    11====== | ---22--- | ......33'''

            # Field widths and float precision are handled in a way similar to placeholders. The following two print statements are equivalent:
            # format = "string.Length.Precisionf" => string%10.2f
print("\nField widths and float precision")
num= 13.579
_string1 = "This is my ten-character, two-decimal number:%10.2f"
_string2 = 'This is my ten-character, two-decimal number:{0:10.2f}'
print(_string1%num)
print(_string2.format(num))

''' Result: Field widths and float precision
    Field widths and float precision
    This is my ten-character, two-decimal number:     13.58
    This is my ten-character, two-decimal number:     13.58'''

# 4. String Formatting - The newest method, introduced with Python 3.6, uses formatted string literals, called f-strings.
    # Formatted String Literals (f-strings)
    # In Python 3.6, f-strings offer several benefits over the older .format() string method described above.
    # For one, you can bring outside variables immediately into to the string rather than pass them as arguments through .format(var).
    # Pass !r to get the string representation:
    # Float formatting follows "result: {value:{width}.{precision}}"
print("\nFormatted String Literals (f-strings)")
name = 'Atul Patel'
print(f"Hi!, I am {name}.")
print(f"Hi!, I am {name!r}.")

print("\nFormatted Floats Literals (f-strings)")
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

        # Note that with f-strings, precision refers to the total number of digits, not just those following the decimal. This fits more closely with scientific notation and statistical analysis. Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it:
num = 23.4500
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

        # If this becomes important, you can always use .format() method syntax inside an f-string:
num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")

''' Result: Formatted String Literals (f-strings)
    Hi!, I am Atul Patel.
    Hi!, I am 'Atul Patel'.

    Formatted Floats Literals (f-strings)
    My 10 character, four decimal number is:   23.4568
    My 10 character, four decimal number is:   23.4568
    My 10 character, four decimal number is:   23.4500
    My 10 character, four decimal number is:     23.45
    My 10 character, four decimal number is:   23.4500
    My 10 character, four decimal number is:   23.4500'''