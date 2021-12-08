from groceryFJ import *

class Shopping_CartFJ(ShoppingFJ):
    def __init__(self, food="Undefine", pound=0, price=0, total_food=0):
        super().__init__(food=food, pound=pound, price=price, total_food=total_food)
        
    def make_listFJ(self):
        item_list = []
        global user_input
        user_input = 0
        while user_input <= 0:
            try:
                user_input = int(input("Enter the number of food you will order: "))
                if user_input < 0:
                    print("The numbers of food should me minimal 1!")
            except:
                print("Please enter the specific number!")
        
        for i in range(user_input):
            new_list = []
            print(f"\nItem #{i+1}:")
            food = input("Enter the name of the food: ")
            pound = 0
            new_list.append(food)
            while pound <= 0:
                try:
                    pound = eval(input("Enter the amount of pounds: "))
                    if pound < 0:
                        print("The amount of pounds should be minimal 1!")
                except:
                    print("Please enter a specific number!")
            new_list.append(pound)
            item_list.append(new_list)
        return item_list

    def display_listFJ(self, item_list):
        cost = []
        print("\n====================================================================")
        print("\nHere's a summary of the items you ordered!\n")
        for f in range(len(item_list)):
            for p in range(0, 1):
                self.__food = item_list[f][p]
                self.__pound = item_list[f][p+1]
                order = ShoppingFJ(self.__food, self.__pound)
                print(f"Item: {self.__food}")
                print(f"Amount ordered: {self.__pound} pounds")
                self.__price = order.get_Price()
                order = ShoppingFJ(self.__food, self.__pound, self.__price)
                print(f"Price per pound: ${self.__price:.2f}")
                self.__total_food = order.TotalFJ()
                print(f"Price of {self.__food}: ${self.__total_food:.2f}\n")
                cost.append(self.__total_food)
        return cost
    
    def Call_PriceFJ(self, cost):
        total = 0
        for total_price in cost:
            total = total + total_price
        print(f"The total Price for your order: ${total:.2f}")
        
shopping_cart = Shopping_CartFJ()
shopping_list = ShoppingFJ()

def main():
    item_list = shopping_cart.make_listFJ()
    total_food = shopping_cart.display_listFJ(item_list)
    shopping_cart.Call_PriceFJ(total_food)
    
if __name__ == "__main__":
    main()