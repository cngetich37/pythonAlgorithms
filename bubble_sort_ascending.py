# unsorted list
my_list_one = [10, 15, 4, 23, 0]

# iterate through the list and compare each element with an adjacent element using FOR Loop
for j in range(len(my_list_one)-1):
    #minus j means the initial result of the iteration is not added.
    for i in range(len(my_list_one)-1-j):
        # compare the former element with an adjacent element
        if my_list_one[i] > my_list_one[i+1]:
            # if the adjacent element is greater than the former element,swap them
            my_list_one[i], my_list_one[i+1] = my_list_one[i+1], my_list_one[i]
            print(my_list_one)
        else:
            # outputs the steps taken to perform the sort
            print(my_list_one)
    print(" ")

# this will print the list in the ascending order from the least to the greatest
print("Sorted list:" + "" + str(my_list_one))
