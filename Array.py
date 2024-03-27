my_array=[]
l=int(input("Length of array: "))
for i in range(l):
    items=input("Enter the array items: ")
    my_array.append(items)
print("The array is {}".format(my_array))
my_array.sort()
print("The second largest array element is {}".format(my_array[-2]))