# comma separated key-value pairs enclosed within {}
#{key1:value1, key2;value2, ..........}

groceries = {'milk':60, 'biscuits':80, 'rice': 90, 'bread': 40}
print(groceries)
print(type(groceries))
print(len(groceries))
# dict are mutable
print(groceries['milk'])

# To update the value of any pair
groceries['milk'] = 65
print(groceries)

groceries['eggs'] = 10 #adds new key-value pair to the dictionary groceries
groceries['bread'] = 35 #updates the value of the key
print(groceries)

student1 = {"maths": 80.5, "eng": 76.0, "phy": 89.0}
#fetch the marks 
print(student1["phy"])

#get()
print(student1.get("chem"))
print(student1.get("chem",40.0))

"""IN DIRECTLY FETCHING THE CHEM MARKS WHICH IS NOT PRESENT IN THE STUDENT1 DICTIONIONARY WE GET AN ERROR WHILE FETCHING IT WITH GET FUNCTION WE DONT GET AN ERROR

ALSO WE CAN ADD THE VALUE OF A NEW PAIR OF MARKS USING GET FUNCTION"""

emp1 = {'id': 1001, 'name': 'John','salary':10000 }
print(emp1.get('phone_no', 6789034566))
print(emp1.get('id', 6789034566))

""" In case of giving a key present in dictionary the actual value of the key will be printed instead of the given default value"""

#membership operator => in
print('1001' in emp1)
print('name' in emp1)

"""the membership in operator returns true only when the key is present and false when key is not present"""

sem1_marks = {'maths': 78.5, 'eng':89.0 ,'phy':86.5}
sem2_marks = {'chem': 81.5, 'bio':67.9}

sem1_marks.update(sem2_marks)
print(sem1_marks)

groceries_1 = {'milk':60,'rice':100,'biscuits':20}
groceries_2 = {'rice':110,'bread':80}

groceries_1.update(groceries_2)
print(groceries_1)

#pop()
groceries_1.pop('milk')
print(groceries_1)

groceries_1 = {'milk':60,'rice':100,'biscuits':20,'milk':65}
print(groceries_1)

#keys cannot be duplicated in a dictionary
#d1 ={[1,2,3]:9,[4,5,6]:8}
#print(d1)

d2 = {1: True, 0: False}
print(d2)

d3 ={1.0: True, 0.0: False}
print(d3)

d4 = {True: 1,False:0}
print(d4)

d5 ={(1,2,3):9,(4,5,6):8}
print(d5)

#d6 = {{'a':1 ,'b':2}: 6}
#print(d6)

#keys cannot be lists,dict,set => immutable datatpe
#allowed keys - str,int,float,boolean,tuple => mutable datatype
# values can be any datatype

student1 = {'id':1001 ,"name":'John',"marks": [89.5,86,76,74]}
print(student1)
print(student1['marks'][1])

student1 = {'id':1001 ,"name":'John',"marks": {'eng':89.5,'hindi':86,'maths':76,'computer':74}}
print(student1["marks"]['eng'])

# fetch the keys
# keys()
print(student1.keys(), type(student1.keys()))
# fetch the values
# values()
print(student1.values(), type(student1.values()))
#fetch the items
#items()
print(student1.items(), type(student1.items()))


