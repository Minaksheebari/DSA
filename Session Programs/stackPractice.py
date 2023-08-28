#Last in first out - LIFO
#mostly used in websites, web applications. 
#Complexity - O(1)

stackList = []
# stackList.append(15)
# stackList.append(20)

#Adding element in stack
def stackAddElement(stackName,element):
    stackName.append(element)
    #print("Stack list: " , stackList)

#Retrive last element from stack
def stackRetriveElement(stackName):
    item = stackName[len(stackName)-1]
    stackName.pop()
    return item

stackAddElement(stackList,25)
stackAddElement(stackList,30)
stackAddElement(stackList,41)
stackAddElement(stackList,89)
stackAddElement(stackList,45)
stackAddElement(stackList,60)
print("Your stack list is: ",stackList)

print("Last element is: ", stackRetriveElement(stackList))
print("New list after retriving last element: ", stackList)

#Search and delete an element
def stackSearchElement(stackName,num):
    newStack=[]
    for i in range(len(stackName)-1,-1,-1):
        if stackName[i] == num:
            stackRetriveElement(stackList)
            return i
           # print("Element found at index: " , i) 
        else:
            stackAddElement(newStack,stackName[i])
            print("New stack is: ",newStack)
            stackRetriveElement(stackList)
            #print("Not found")
    

index = stackSearchElement(stackList,30)
print("Element found at index: ", index)






