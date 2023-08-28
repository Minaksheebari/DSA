#First in First out - FIFO

QueueList = []

#Adding element in Queue
def queueAddElement(queueName,element):
    queueName.append(element)

#Retrive first element from queue
def queueRetriveElement(queueName):
    item = queueName[0]
    queueName.pop(0)
    return item

queueAddElement(QueueList,23)
queueAddElement(QueueList,45)
queueAddElement(QueueList,15)
queueAddElement(QueueList,86)
queueAddElement(QueueList,35)

print("Your Queue list is: ",QueueList)

print("first element is: ", queueRetriveElement(QueueList))
print("New list after retriving first element: ", QueueList)

#Search and delete an element
def queueSearchElement(queueName,num):
    newQue=[]
    flag=0
    returnIndex=0
    for i in range(0,len(queueName)):
        if num==queueName[0]:
            flag=1
            queueRetriveElement(queueName)
            returnIndex = i
            
        else:
            if(flag==0):
                queueAddElement(newQue,queueName[0])
                print("New Queue is: ",newQue)
                queueRetriveElement(queueName)

            #print("Not found")
        
    queueName = newQue + queueName
    print(queueName)
    return returnIndex

index = queueSearchElement(QueueList,15)
print("Element found at index: ", index)
