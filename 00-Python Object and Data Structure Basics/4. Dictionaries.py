'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    Dictionaries are Mappings In Python

        "Mappings are nothing but key value Pair"
        Eg: {"key":"value","name":"Atul Patel"}    
    
        Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. This is an important distinction, since mappings won't retain order since they have objects defined by a key.

        A Python dictionary consists of a key and then an associated value. That value can be almost any Python object.

        This section will serve as a brief introduction to dictionaries and consist of:
            1.) Constructing a Dictionary
            2.) Accessing objects from a dictionary
            3.) Nesting Dictionaries
            4.) Basic Dictionary Methods

   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
print("\nDictionaries")

# 1.) Constructing a Dictionary & 2.) Accessing objects from a dictionary
print("\n1.) Constructing a Dictionary & 2.) Accessing objects from a dictionary")
    # Make a dictionary with {} and : to signify a key and a value
my_dict1 = {'key':'value','name':'Atul Patel','Age':27}
    # Call values by their key
print('\t'+ str(my_dict1['Age']))

    # Its important to note that dictionaries are very flexible in the data types they can hold
my_dict2 = {'key':'value','name':'Atul Patel','Age':27, 'hobbies':['Poetry','Singing','Cricket']}
print(my_dict2['hobbies'])

    # Can call an index on that value
print('\t' + my_dict2['hobbies'][1])

    # Can then even call methods on that value
print('\t' + my_dict2['hobbies'][1].upper())
print(my_dict2)
my_dict2['hobbies'][1] = my_dict2['hobbies'][1].upper()
print(my_dict2)
print('\t' + str(len(my_dict2['hobbies'][1])))

    # ALter the value of a dictionary element
print(my_dict2['Age'])
my_dict2['Age']=my_dict2['Age']-1
print(my_dict2['Age'])
my_dict2['Age'] += 1
print(my_dict2['Age'])

    # create keys by assignment
my_dict2['Degree'] = 'B.Tech in EE'
print(my_dict2)
print('\t' + my_dict2['Degree'])

# 3.) Nesting Dictionaries
print("\n3.) Nesting Dictionaries")
    # Dictionary nested inside a dictionary nested inside a dictionary
_nested_dict1 = {'dept':{'IT_dept':{'emp_name':'Atul Patel'}}}
    # to get the value - Keep calling the keys
itDeptDetails = _nested_dict1['dept']['IT_dept']['emp_name']
print(itDeptDetails)

_nested_dict1 = {'dept':{'IT_dept':{'emp_name':'Atul Patel','emp_id':'emp001'},'Sales_Dept':{'emp_name':'Atul Patel','emp_id':'emp001'}}}

salesDeptDetails = _nested_dict1['dept']['Sales_Dept']
print(salesDeptDetails)
salesDeptDetails_empName = _nested_dict1['dept']['Sales_Dept']['emp_name']
salesDeptDetails_empId = _nested_dict1['dept']['Sales_Dept']['emp_id']
print(salesDeptDetails_empName)
print(salesDeptDetails_empId)

# 4.) Basic Dictionary Methods
print("\n4.) Basic Dictionary Methods")

_dict_methods = {'dept':{'IT_dept':{'emp_name':'Atul Patel','emp_id':'emp001'},'Sales_Dept':{'emp_name':'Atul Patel','emp_id':'emp001'}}}
    # Method to return a list of all keys 
print(_dict_methods.keys())

    # Method to grab all values
print(_dict_methods.values())

    # Method to return tuples of all items  (we'll learn about tuples soon)
print(_dict_methods.items())
print('\t')