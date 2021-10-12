listData=['I','A','N','2' ,'3', None,None,None]
listPointer=[1,2,3,4,-1,5,6,-1]
def findNode(item):
     nullPointer=-1
     startPointer=0
     currentNodePointer=startPointer
     while currentNodePointer!=nullPointer and listData[currentNodePointer]!=item:
         currentNodePointer=listPointer[currentNodePointer]
     return currentNodePointer

val=input("Please insert an element\n")
pointer=findNode(val)
if pointer==-1:
    print("Item is not found")
else:
    print("Item is found at CurrentNodePointer", pointer)

