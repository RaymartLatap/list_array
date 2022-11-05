print("******** Programmed By ********")
print("******** Raymart Latap ********")
print("********** BSCOE 2-2 **********\n")


# The function used is menu function
def menu():
    print("\n-------------------Menu------------------")
    print("What do you want to do?")
    print("1. Add an Element")
    print("2. Insert an Element")
    print("3. Modify an Element")
    print("4. Delete an Element")
    print("5. Arrange in Ascending Order")
    print("6. Arange in Decending Order")
    print("7. Exit")
    return
	
#Variable used in this Program
array = [1,3,5,7,9,11,13,15,17,19]

menu()
menu_option = int(input("\nWhat do you want to do?(1-7):"))

#Adding Element
if menu_option ==1:
	print("You choose to Add an Element")
	print("\nArray:", array)
	elem = int(input("\nEnter the element you want to add: "))                                   
	array.append(elem)
	print("The element has been added!")
	print("\nThis is the new array: \n", array)

#Insert Element	
elif menu_option ==2:
	print("You choose to Insert an Element")
	idx = int(input("\nEnter the index where you want to insert: "))
	elem = int(input("Enter the elem you want to insert: "))
	array.insert(idx, elem)
	print("The element has been insert")
	print("\nThis is the new array: \n", array)

#Modify Element		
elif menu_option==3:
	print("You choose to Modify an Element")
	idx = int(input("\nEnter the index you want to modify: "))
	array.pop(idx)
	elem = int(input("Enter the element: "))
	array.insert(idx, elem)
	print("The element has modified!")
	print("\nThis is the new array: \n", array)

#Delete Element	
elif menu_option ==4:
	print("You choose to Delete an Element")
	idx = int(input("\nEnter the index you want to delete: "))
	array.pop(idx)
	print("The element has been deleted!")
	print("\nThis is the new array: \n", array)

 #Arrange in Ascending Order      
elif menu_option ==5:
	print("You choose to Arrange in Ascending Order")
	array.sort()
	print("\nThis is the new array:\n", array)

#Arrange in Descending Order	
elif menu_option ==6:
	print("You choose to Arrange in Descending Order")
	array.reverse()
	print("\nThis is the new array:\n", array)

		
elif menu_option ==7:
	print("\nThank you for using this program!\n")
	exit()