input_size=int(input("Enter number of elements"))
elements=[]
for i in range(input_size):
    element=float(input("enter the element"))
    elements.append(element)
key=float(input("Enter the number to be found"))
def sequentially_search(elements,key):
    for i in range(len(elements)):
        if elements[i]==key:
            return i
    return -1
print("The entered element's position is ",sequentially_search(elements,key))   
if sequentially_search(elements,key)==-1:
    print("The number is not found")     