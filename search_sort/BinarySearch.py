
#The binary search is used to find an item in an ORDERED list.

def binarySearch(myItem,myList):
  found = False
  bottom = 0
  top = len(myList)-1
  while bottom <= top and not found:
    middle = (bottom+top)//2
    if myList[middle] == myItem:
      found = True
    elif myList[middle] < myItem:
      bottom = middle + 1
    else:
      top = middle-1
  return found


if __name__ =='__main__':
  shopping = [1,4,6,8,12,15,18,19,24,27,31,42,43,58]
  item = int(input('What item do you want to find?'))
  isitFound = binarySearch(item,shopping)
  if isitFound:
    print('Your item is in the list!')
  else:
    print('Your item is not in the list')