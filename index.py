import copy #we use python's copys module 
#create a shallow copy

bag1=[[1,2,3],[4,5,6]]
#create a shallow copy
bag2 = copy.copy(bag1)
print("Before changing anything :")
print("bag1:", bag1)
print("bag2:", bag2) 
bag1[0][0]=999
print("\nAfter changing anything:")
print("bag1:",bag1)
print("bag2:",bag2)
#======================================
#deeper copy
import copy 
bag1=[[1,2,3],[4,5,6]]
bag2=copy.deepcopy(bag1)
print("Before change anything :")
print("bag1:",bag1)
print("bag2:",bag2)
bag1[0][0]=999
print("after changing anything :")
print("bag1:",bag1)
print("bag2:",bag2)


