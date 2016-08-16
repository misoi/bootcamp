"""
define a function that takes two lists which is list1 and list 2
"""

def list_missing(list1,list2):
	
# loops through the list2
	for i in list2: 
	# checks if numbers in list2 is not in list1 
		if i not in list1:
			# if its not there it is added to empty list3
			list3.append(i)
			# prints the list3
			return list3
list1 = [7,4,3]
list2 = [7,2,4,3]
list3 = []
print list_missing(list1,list2)

