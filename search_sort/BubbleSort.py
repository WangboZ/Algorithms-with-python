def bubbleSort(myList):
  
  for i in range (0, len(myList)-1):
    for j in range (0,len(myList)-1-i):
      if myList[j]>myList[j+1]:
	myList[j],myList[j+1]=myList[j+1],myList[j]
  return myList

theList = [3,4,2,7,1,8,5,9,6]
print (bubbleSort(theList))
