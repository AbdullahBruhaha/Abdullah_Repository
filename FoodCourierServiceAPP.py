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
userorderline = [userbasket, usercourier, orderstatus]
userbasket = []



# alternative search algorithm for code
def linear_search(arr,x):
  for i in range(len(arr)):
    if arr[i] == x:
      return "This exists in the database"
      break
    else:
      return "query not found"
      
#def product_search(products_list,search_item):
 # for product in product_list:
  #  if product == search_item:
   #   return True
    #  print("This exists in the database")
    #else:
    #  return False
    #  print("query not found")

# allow user to add a product to their basket to purchase
def purchaseproducts():
  userorder = input("Enter product that you would like to purchase: \n")
  if userorder == "finished":
    menu()
  if userorder in DBProducts:
    userbasket.append(userorder)
    print("\n This is your basket: \n")
    print(userbasket)
    menu()
  else:
    print("That is not one of the products... \n")
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
   
#
def show_command_list():  
    print("\n If you would like to see the product list, type show products.")
    
    print("\n If you would like to purchase a product, type purchase products.")
    
    print("\n If you would like to see your current basket, type show basket.")
    
    print("\n If you would like to remove an item from your basket, type remove item.")
    
    print("\n If you would like to see the courier list, type show couriers.")
    
    print("\n If you would like to hire a courier, type hire courier.")
    
    print("\n If you would like to see your currently hired couriers, type show hired couriers.")
    
    print("\n If you would like to remove a courier from your list of hired couriers, type fire courier.")
    
    print("\n If you are finished, type finished.")
    
    print()
    menu()


    
def menu():
  cmd = input("\n Enter your commmand. If you would like to see the command list, type command list. \n")
  
  if cmd == "command list":
    show_command_list()
    
  elif cmd == "show products" or cmd == "show product":
    displayproducts()
    
  elif cmd == "purchase products" or cmd == "purchase product":
    purchaseproducts()
  
  elif cmd == "remove item":
    removeitem()
    
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
    
  elif cmd == "finished":
    print("Thank you for ordering.")
    exit()
    
  else:
    print("That is not one of the commands... \n")
    menu()
  
  
menu()

print("Thank you for ordering.")