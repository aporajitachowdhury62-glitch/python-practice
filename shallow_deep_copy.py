import copy
l1 = [1,2.5,[10, 20, 30], 'Python']

# shallow copy
l2 = copy.copy(l1)
print(l2)
print(id(l1))
print(id(l2))
# both l1 & l2 have different memory address
l1[0] = 100
print(f"l1 -> {l1}", id(l1))
print(f"l2 -> {l2}", id(l2))
l1[0] = 5 # the value of l1 will be changed only 
l1[2][0] = 50 # the value of l1 & l2 both will be changed
print(f"l1 -> {l1}", id(l1))
print(f"l2 -> {l2}", id(l2))
# the outer list will only have different memory inner list will have same memory

# deep copy
l2 = copy.deepcopy(l1)
l1[0] = 5 # the value of l1 will be changed only 
l1[2][0] = 50 # the value of l1 will be changed only
print(f"l1 -> {l1}", id(l1))
print(f"l2 -> {l2}", id(l2))
# the outer list will have different memory inner list will also have different memory

d1 = {'id': 1111, 'name':'john','marks':{'eng':91.5,'bio':80.0,'maths': 94}}
d2 = copy.deepcopy(d1)
d1['name']='ben'
d1['marks']['maths']= 84
print(f"d1 -> {d1}", id(d1))
print(f"d2 -> {d2}", id(d2))