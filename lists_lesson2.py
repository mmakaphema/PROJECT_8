# ADDING OR REMOVING ELEMENTS/ ITEMS FROM A LIST
# USING THE APPEND METHOD

fruits = ["apple", "orange", "kiwi", "watermelon"]
fruits.append("peer")
print(fruits)

 #ADDINGVALUES TO A SPECIFIC POSITION
 #Insert method
 
fruits.insert(1, "banana")
print(fruits)

#Removing an item: REMOVE METHOD

fruits.remove("banana")
print(fruits)

#THE SORT LIST

fruits.sort(reverse= True)
print(fruits)