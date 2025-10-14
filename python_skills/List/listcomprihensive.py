# create the list containing table of 7

a=7
table = []
for i in range(1,11):
    table.append(7*i)

table_com = [5*i for i in range(1,11)]

print(f"table of {a}", table)
print(f"table of 5", table_com)
