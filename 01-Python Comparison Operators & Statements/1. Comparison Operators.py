# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. Comparison Operators
#   1. Equal to                 '=='
#   2. Not Equal to             '!='
#   3. Greater than             '>'
#   4. Less Than                '<'
#   5. Greater than or equal to '>='
#   6. Less than or equal to    '<='
#
# B. Chained Comparison Operators
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("A. Comparison Operators")
a = b = 20; c = 15
print(a==b, b==c, sep=(','))
print(a!=b, b!=c)
print(a>b, b>c)
print(a<b, b<c)
print(a>=b, b>=c)
print(a<=b, b<=c)

print("B. Chained Comparison Operators")
print("Operation - 'OR'")
print(a==b or b==c)
print(a!=b or b!=c)
print(a>b or b>c)
print(a<b or b<c)
print(a>=b or b>=c)
print(a<=b or b<=c)

print("Operation - 'AND'")
print(a==b & b==c, a==b==c) # Both are same expressions
print(a!=b & b!=c, a!=b!=c)
print(a>b & b>c, a>b>c)
print(a<b & b<c, a<b<c)
print(a>=b & b>=c, a>=b>=c)
print(a<=b & b<=c, a<=b<=c)