elements = int(input("Enter the number of elements you want in the list: "))

my_list = []  # Create an empty list to store elements

for i in range(elements):
    element = input(f"Input value of element {i + 1} in this list: ")
    my_list.append(element)

for i in range(len(my_list)):
    print("The position of the element is ", i, "and the value stored in the element is ", my_list[i])
