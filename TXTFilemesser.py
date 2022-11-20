names1 = ['Jessa', 'Eric', 'Bob', 'Jebb','Kaladin']

# open file in write mode
with open("nameSales.txt", "w+") as fp:
    for item in names1:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')



names2 = []

# open file and read the content in a list
with open("nameSales.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        names2.append(x)

# display list
print(names2)

DBCouriers = []
# open file and read the content in a list
with open("CourierNames.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        DBCouriers.append(x)

# display list
print(DBCouriers)

DBProducts = []
# open file and read the content in a list
with open("ProductNames.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        DBProducts.append(x)

# display list
print(DBProducts)