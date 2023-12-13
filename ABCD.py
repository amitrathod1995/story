list2=[]

def demo(list1):
    global list2
    for i in list1:
        NewList=i*2
        list2.append(NewList)
    print(f"output is {list2}")
    return list2
demo([1,2,3,4,5])
print(f"return output {list2}")
