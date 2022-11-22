## PSUEDOCODE PLAN:

#login function
#menu commands function: order specific products
#Store user details persistently
#Store courier details persistently
#Store product details persistently
#Update status of order as it changes
#test functions
#


usercourier = []
orderstatus = []
#userorder = []
userbasket = []

with open("UserSavedBasket.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        userbasket.append(x)


with open("UserSavedCourier.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        usercourier.append(x)

DBProducts = []
# open file and read the content in a list
with open("ProductNames.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        DBProducts.append(x)


DBCouriers = []
# open file and read the content in a list
with open("CourierNames.txt", 'r') as filereader:
    for line in filereader:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        DBCouriers.append(x)


#products = ["cheese sandwich", "tuna sandwich", "chicken sandwich"]
#couriers = ["bob", "jim", "john"]
#userorderline = [userbasket, usercourier, orderstatus]



# alternative search algorithm for code
def linear_search(arr,x):
  for i in range(len(arr)):
    if arr[i] == x:
      return "This exists in the database"
      break
    else:
      return "query not found"
      


# allow user to add a product to their basket to purchase
def purchaseproducts():
  userorder = input("Enter product that you would like to purchase: \n")
  if userorder == "finished":
    menu()
  if userorder in DBProducts:
    userbasket.append(userorder)
    purchase_result = "\n This is your basket: \n"
    print(purchase_result)
    print(userbasket)
    menu()
  else:
    purchase_result = "That is not one of the products... \n"
    print(purchase_result)
    menu()



#allow user to choose a courier to hire
def user_choose_courier():
  chosencourier = input("Enter courier name that you would like to hire: \n")
  if chosencourier == "finished":
    menu()
  elif chosencourier in usercourier:
    print("\n You have already hired this courier. \n")
    menu()  
  elif chosencourier in DBCouriers:
    usercourier.append(chosencourier)
    print("\n This is your courier: \n")
    print(usercourier)
    menu()   
  else:
    print("That is not one of the couriers... \n")
    menu()    

#shows the products that are available to purchase
def displayproducts():
  print(DBProducts)
  print()
  menu()

#shows the couriers that are available for hire
def displaycouriers():
  print(DBCouriers)
  print()
  menu()
  
#shows the couriers that have been hired
def displayusercouriers():
  print(usercourier)
  print()
  menu()
  
#shows contents of the user's basket
def displaybasket():
  print(userbasket)
  print()
  menu()
  
#removes item from basket
def removeitem():
  print("This is your basket: \n")
  print(userbasket)
  unwanted_item = input("Enter the item that you would like to remove from your basket. \n")
  try:
    userbasket.remove(unwanted_item)
    print("\n Your basket has been updated: ", userbasket, "\n")
  except:
    print("\n That item is not in your basket. \n")
  finally:
    menu()

#removes courier from list of hired couriers
def firecourier():
  print("This is your list of hired couriers: \n")
  print(usercourier)
  unwanted_courier = input("Enter name of the courier that you would like to remove from your list of hired couriers. \n")
  try:
    usercourier.remove(unwanted_courier)
    print("\n Your list of hired couriers has been updated: ", usercourier, "\n")
  except:
    print("\n That is not one of your hired couriers. \n")
  finally:
    menu()
   

def SaveBasket():
  with open("UserSavedBasket.txt", "w+") as filereader:
    for item in userbasket:
        filereader.write("%s\n" % item)
    print("Saved")
  menu()

def ClearBasket():
  userbasket = []
  with open("UserSavedBasket.txt","w+"):
    print("Cleared")
  menu()

def SaveCourier():
  with open("UserSavedCourier.txt", "w+") as filereader:
    for item in usercourier:
        filereader.write("%s\n" % item)
    print("Saved")
  menu()

def ClearCourier():  
  usercourier = []
  with open("UserSavedCourier.txt","w+"):
    print("\n Cleared \n")
  menu()

def show_command_list():  
    print("\n If you would like to see the product list, type show products.\n")
    
    print("\n If you would like to purchase a product, type purchase products.\n")
    
    print("\n If you would like to see your current basket, type show basket. \n")

    print("\n If you would like to save your current basket, type save basket. \n")
    
    print("\n If you would like to clear your current basket, type clear basket. \n")

    print("\n If you would like to remove an item from your basket, type remove item. \n")
    
    print("\n If you would like to see the courier list, type show couriers. \n")
    
    print("\n If you would like to hire a courier, type hire courier. \n")
    
    print("\n If you would like to see your currently hired couriers, type show hired couriers. \n")
    
    print("\n If you would like to remove a courier from your list of hired couriers, type fire courier. \n")
    
    print("\n If you would like to save your current courier list, type save courier. \n")
    
    print("\n If you would like to clear your current courier list, type clear courier. \n")


    print("\n If you are finished, type finished.\n \n")
    
    menu()


    
def menu():
  cmd = input("\n Enter your commmand. If you would like to see the command list, type command list. \n")
  
  if cmd == "command list":
    show_command_list()
    
  elif cmd == "show product" or cmd == "show products":
    displayproducts()
    
  elif cmd == "purchase product" or cmd == "purchase products":
    purchaseproducts()
  
  elif cmd == "remove item" or cmd == "remove items":
    removeitem()
  
  elif cmd == "save basket":
    SaveBasket()
  
  elif cmd == "clear basket":
    ClearBasket()
    
  elif cmd == "save courier" or cmd == "save couriers":
    SaveCourier()

  elif cmd == "clear courier" or cmd == "clear couriers":
    ClearCourier()

  elif cmd == "show couriers" or cmd == "show courier":
    displaycouriers()
    
  elif cmd == "hire courier" or cmd == "hire couriers":
    user_choose_courier()
    
  elif cmd == "show basket":
    displaybasket()
    
  elif cmd == "show hired courier" or cmd == "show hired couriers":
    displayusercouriers()
  
  elif cmd == "fire courier" or cmd == "fire couriers":
    firecourier()
    
  elif cmd == "finished" or cmd == "finish":
    print("Thank you for ordering.")
    exit()
    
  else:
    print("That is not one of the commands... \n")
    menu()
  
  
menu()

#print("Thank you for ordering.")



# TESTS:
#------------------------------------------------------------------------------------------------------------

def test_purchaseproducts():
  print("tests if user inputted product to order is in product list database")
  test_userorder = input("enter product to order: ")
  try: 
    assert test_userorder in DBProducts
  except: 
    print("Assertion Error. Product entered is not in product list.")

#test_purchaseproducts()

def test_user_choose_courier1():
  print("tests if user inputted courier is in courier database.")
  test_chosencourier = input(("\n Enter courier name that you would like to hire from courier list: \n"))
  try:
    assert test_chosencourier in DBCouriers
  except:
    print("That is not one of the couriers... \n")


#test_user_choose_courier1()




def test_user_choose_courier2():
  print("\n This tests if input is already in list of hired couriers. \n")
  test_chosencourier = input("\n Enter courier name that you would like to hire from courier list: \n")
  if test_chosencourier in DBCouriers:
    try:
      assert test_chosencourier not in usercourier
    except:
      print("\n You have already hired this courier. \n")
  else:
    print("Might not be in courier list")
 
#test_user_choose_courier2()