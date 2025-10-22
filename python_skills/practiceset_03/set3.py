'''Create a tuple coordinates = (10, 20) and print both elements.
Try to modify the tuple by setting coordinates[0] = 50 — note what
happens.
Convert the tuple to a list, change its first element to 50 , and convert it back
to a tuple.

'''

coordinates = (10, 20)
print(coordinates[0], coordinates[1])
#coordinates[0] = 50

list_tuple = list(coordinates)
print(list_tuple)
list_tuple[0] = 50

tuple_list = tuple(list_tuple)
print(tuple_list)