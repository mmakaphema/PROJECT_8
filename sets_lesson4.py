# SETS
'''
my_set = {1,2, 3, 4, 5,6}
print(my_set)

my_set.add(7)
print(my_set)
      
my_set.remove(6)
print(my_set)
'''
#OPERATIONS WITH SETS
#1. UNION: COMBIES 2 SETS
#removes any duplicates

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

#1 UNION
union_set = set1.union(set2)
print(union_set)

#2.INTERSECTION
inter_set = set1.intersection(set2)
#Findsthe common element between 2 sets
print(inter_set)

#DIFFERENCE
#Finds the elements that are present in one, but not the other.

diff_set = set1.difference(set2)
print(diff_set)

differ_set = set2.difference(set1)
print(differ_set)