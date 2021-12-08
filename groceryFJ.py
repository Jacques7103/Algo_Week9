class ShoppingFJ:
    def __init__(self, food = "Undefine", pound = 0, price = 0, total_food = 0):
        self.__food = food
        self.__pound = pound
        self.__price = price
        self.__total_food = total_food
        
    def __ItemListFJ(self):
        self.__food = self.__food.lower()
        if self.__food == "dry cured iberian ham":
            self.__price = 177.80
        elif self.__food == "wagyu steaks":
            self.__price = 450.00
        elif self.__food == "matsutake mushrooms":
            self.__price = 272.00
        elif self.__food == "kopi luwak coffee":
            self.__price = 206.50
        elif self.__food == "moose cheese":
            self.__price = 487.20
        elif self.__food == "white truffles":
            self.__price = 3600.00
        elif self.__food == "blue fin tuna":
            self.__price = 3603.00
        elif self.__food == "le bonnotte potatoes":
            self.__price = 270.81
        else:
            self.__price = 0.00
    
    def get_Price(self):
        self.__ItemListFJ()
        return self.__price
            
    def TotalFJ(self):
        total_food = self.__pound * self.__price
        self.__total_food = total_food
        return self.__total_food
    
    def __str__(self):
        self.__price = item.__ItemListFJ()
        return self.__price
        

item = ShoppingFJ()