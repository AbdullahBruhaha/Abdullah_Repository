
# names2 = []
# # open file and read the content in a list
# with open("nameSales.txt", 'r') as filereader:
#     for line in filereader:
#         # remove linebreak from a current name
#         # linebreak is the last character of each line
#         x = line[:-1]

#         # add current item to the list
#         names2.append(x)

# # display list
# print(names2)


# products = ["cheese sandwich", "tuna sandwich", "chicken sandwich"]
# couriers = ["bob", "jim", "john"]

# # open file in write mode
# with open("CourierNames.txt", "w+") as filereader:
#     for item in couriers:
#         # write each item on a new line
#         filereader.write("%s\n" % item)
#     print('Done')


BigBasket = []
userchosen = input("enter smthn")
BigBasket.append(userchosen)
print(BigBasket)

with open("BiggestBasket.txt", "a+") as filereader:
    for item in BigBasket:
        filereader.write("%s\n" % item)
    print('Done')


BigBasket2 = []
# open file and read the content in a list
with open("BiggestBasket.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        BigBasket2.append(x)

# display list
print(BigBasket)
print(BigBasket2)

with open("BiggestBasket.txt","w"):
    print("cleared")