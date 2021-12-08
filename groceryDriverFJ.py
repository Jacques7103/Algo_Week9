from groceryFJ import *         #Import a module from groceryFJ file

class Shopping_CartFJ(ShoppingFJ):
    def __init__(self, food="Undefine", pound=0, price=0, total_food=0):    #Initialize from super class
        super().__init__(food=food, pound=pound, price=price, total_food=total_food)
        
    def make_listFJ(self):
        item_list = []              #Creting a list
        global user_input           #Make the var global
        user_input = 0              #Creating user_input var
        while user_input <= 0:      #Creating a loop for user to input a number
            try:
                user_input = int(input("Enter the number of food you will order: "))    #Asking an input from user
                if user_input < 0:
                    print("The numbers of food should me minimal 1!")   #If the user input the number below 0, it will ask the user to re-enter the value
            except:
                print("Please enter the specific number!")        #If the user input data types other than int, it will ask the user to re-enter the value
        
        for i in range(user_input):                                         #Creating a loop for user to input the name of the food and the amount of pounds
            new_list = []                                                   #Creating a list
            print(f"\nItem #{i+1}:")                                        #Printing out "Item #n"
            food = input("Enter the name of the food: ")                    #Asking an input from user
            pound = 0                                                       #Create pound var
            new_list.append(food)                                           #Append the user input into new_list
            while pound <= 0:                                               #Creating loop for user to input the amount of pounds
                try:
                    pound = eval(input("Enter the amount of pounds: "))     #Asking an input from user
                    if pound < 0:
                        print("The amount of pounds should be minimal 1!")  #If the user input the number below 0, it will ask the user to re-enter the value
                except:
                    print("Please enter a specific number!")                #If the user input data types other than int, it will ask the user to re-enter the value
            new_list.append(pound)                                          #Append the user input into new_list
            item_list.append(new_list)                                      #Append new_list into item_list (Append a list into a list)
        return item_list                                                    #Return the list

    def display_listFJ(self, item_list):
        cost = []       #Creating a list
        print("\n====================================================================")     #Making a separator between user input and the output
        print("\nHere's a summary of the items you ordered!\n")     
        for f in range(len(item_list)):                                                     #Creating a loop in range of the user input
            for p in range(0, 1):                                                           #Creating a loop in range 1
                self.__food = item_list[f][p]                                               #Take self.__food from the user input(food)
                self.__pound = item_list[f][p+1]                                            #Take self.__pound from the user input(pound)
                order = ShoppingFJ(self.__food, self.__pound)                               #Creating a var for ShoppingFJ class
                print(f"Item: {self.__food}")                                               #Printing the item name
                print(f"Amount ordered: {self.__pound} pounds")                             #Printing the amount the user ordered
                self.__price = order.get_Price()                                            #Run get_Price funct from ShoppingFJ
                order = ShoppingFJ(self.__food, self.__pound, self.__price)                 #Replace the var and adding the self.__price into the ShoppingFJ Initializer
                print(f"Price per pound: ${self.__price:.2f}")                              #Printing the price per pound of the item
                self.__total_food = order.TotalFJ()                                         #Run TotalFJ funct from ShoppingFJ
                print(f"Price of {self.__food}: ${self.__total_food:.2f}\n")                #Printing out the total price of an item
                cost.append(self.__total_food)                                              #Append the total price into cost list
        return cost                                                                         #Return the list
    
    def Call_PriceFJ(self, cost):
        total = 0                                                   #Creating total var
        for total_price in cost:                                    #Creating a loop to get the total price of an item
            total = total + total_price                             #Adding every total price
        print(f"The total Price for your order: ${total:.2f}")      #Printing out the total price of the user order
        
shopping_cart = Shopping_CartFJ()                       #Creating a var for Shopping_CartFJ class             

def main():                                                 #Creating a main funct to run all the funct above
    item_list = shopping_cart.make_listFJ()                 #Creating a var that run make_listFJ funct
    total_food = shopping_cart.display_listFJ(item_list)    #Creating a var that run display_listFJ funct
    shopping_cart.Call_PriceFJ(total_food)                  #Run the funct Call_PriceFJ
    
if __name__ == "__main__":
    main()                                                  #Run the main funct