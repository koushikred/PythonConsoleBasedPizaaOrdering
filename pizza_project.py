#declaring pizza class
class Pizza:

    #intializing the pizza class with cheese,pepermoni and mushroom toppings
    def __init__(self,n,size='', no_cheese_toppings=0, no_pepermoni_toppings=0,
                 no_mushroom_toppings=0):
        self.n = n
        self.size = size
        self.no_cheese_toppings = no_cheese_toppings
        self.no_pepermoni_toppings = no_pepermoni_toppings
        self.no_mushroom_toppings = no_mushroom_toppings

    #method to get the size of pizza
    def get_size(self):
        print("Size :",self.size)
    #method to set the size of the pizza
    def set_size(self,siz):
        self.size = siz
    
    #method to get the cheese toppings
    def get_cheese_toppings(self):
        print('Number of cheese toppings:', self.no_cheese_toppings)
    #method to set the number of cheese topping
    def set_cheese_toppings(self, num):
        self.no_cheese_toppings = num
    
    #method to get the pepermoni toppings
    def get_pepermoni_toppings(self):
        print('Number of cheese toppings:', self.no_pepermoni_toppings)
    #method to set the pepermoni toppings
    def set_pepermoni_toppings(self, num):
        self.no_pepermoni_toppings = num
    
    #method to get the mushroom toppings
    def get_mushroom_toppings(self):
        print('Number of cheese toppings:', self.no_mushroom_toppings)
    #method to set the mushroom toppings
    def set_mushroom_toppings(self, num):
        self.no_mushroom_toppings = num

    #method to calcuate the total cost
    def calcCost(self):
        cost = 0
        if self.size == 'small':
            cost+=10
        elif self.size == 'medium':
            cost+=12
        elif self.size == 'large':
            cost+=14
        else:
            return 'Wrong selection'
        
        return cost + self.no_cheese_toppings*2 +self.no_pepermoni_toppings*2 + self.no_mushroom_toppings*2
    #displaying the information of certain pizza
    def __str__(self):
        t_cost = self.calcCost()
        s = f'Pizza size:{self.size}\nNumber of Cheese Toppings: {self.no_cheese_toppings}\n'\
            f'Number of Pepermoni Toppings: {self.no_pepermoni_toppings}\n'\
            f'Number of Mushrrom Toppings: {self.no_mushroom_toppings}\n'\
            f'Total Cost of the pizza: {t_cost}$'
        
        return s

class DeluxePizza(Pizza):
    numberOfPizzas = 0
    def __init__(self,n,size, no_cheese_toppings=0, no_pepermoni_toppings=0,
                 no_mushroom_toppings=0, stuffedWithCheese=False, veggieToppings=0):
        
        super().__init__(n,size, no_cheese_toppings, no_pepermoni_toppings, no_mushroom_toppings)
        self.stuffedWithCheese = stuffedWithCheese
        self.veggieToppings = veggieToppings
        DeluxePizza.numberOfPizzas +=1
    #method to get the veggie toppings
    def get_veggie_toppings(self):
        print('Number of veggie toppings:', self.veggieToppings)
        return self.veggieToppings
    #method to set the veggie toppings
    def set_veggie_toppings(self):
        self.no_mushroom_toppings = self.no_cheese_toppings + self.no_pepermoni_toppings

    #method to know whether pizza is stuffed with cheese or not 
    def is_stuffed_cheese(self):
        print('Stuffed with cheese', self.stuffedWithCheese)
        return self.stuffedWithCheese
    #method to set the stuffed cheese
    def set_stuffed_cheese(self, bol):
        self.stuffedWithCheese = bol

    #methodto get total number of pizzas
    def get_No_Of_Pizzas(self):
        print('Number of Deluxe Pizza\'s:', self.numbeOfPizzas)
        return self.numberOfPizzas

    #method to calculate the cost
    def calcCost(self):
        cost=super().calcCost()
        if self.stuffedWithCheese:
            if self.size == 'small':
                cost+=2
            elif self.size == 'medium':
                cost+=4
            elif self.size == 'large':
                cost+=6
            else:
                return 'Wrong selection'

        return cost + self.veggieToppings*3

    #displaying the information
    def __str__(self):
        t_cost = self.calcCost()
        s = f'\tPizza size:{self.size}\n\tNumber of Cheese Toppings: {self.no_cheese_toppings}\n'\
            f'\tNumber of Pepermoni Toppings: {self.no_pepermoni_toppings}\n'\
            f'\tNumber of Mushrrom Toppings: {self.no_mushroom_toppings}\n'\
            f'\tCheese Filled Dough: {self.stuffedWithCheese}\n'\
            f'\tNumber of veggie toppings: {self.veggieToppings}\n'\
            f'\tTotal Cost of the pizza: {t_cost}$\n'
        
        return s
#function to check the password
def password_check():
    pas = input("Enter your password:")
    if pas=='deluxepizza':
        return True
    return False

#creating a pizza order
def Adding(c,j):
    print("Enter details for Pizza #{}".format(c+j))
    size = input("\tEnter size options(small/medium/large)")
    no_cheese_toppings=int(input("\tEnter number of cheese toppings(0-10):"))
    no_pepermoni_toppings=int(input("\tEnter number of pepermoni toppings(0-10):"))
    no_mushroom_toppings=int(input("\tEnter number of mushroom toppings(0-10):"))
    stuffedWithCheese=bool(int(input("\tWant stuffed cheese dough Enter 1(True) or 0(False):")))
    veggieToppings=int(input("\tEnter number of veggie toppings(0-10):"))
    #retruning the object
    return DeluxePizza(
        n = c+j, size = size,
        no_cheese_toppings = no_cheese_toppings,
        no_pepermoni_toppings = no_pepermoni_toppings,
        no_mushroom_toppings = no_mushroom_toppings,
        stuffedWithCheese = stuffedWithCheese,
        veggieToppings = veggieToppings
        )


#main
if __name__=='__main__':
    #welcome msg
    print("Hello Papa John, Lets start the business")

    #Taking the input for the total number of pizzas
    maxPizzas = int(input("Enter the number of Pizzas, we can do today:"))
    
    todaysPizzas = [] #list to store todays pizzas
    #day = 0
    #MainDriver()
    c=0
    #runnig an infinite loop till the user wanted to close
    while True:
        #showing the menu
        print("Papa John, what do you want to do?\n"\
              "1.Enter a new pizza order (password required)\n"\
              "2.Change information of a specific order (password required)\n"\
              "3.Display details for all pizzas of a specific size (s/m/l)\n"\
              "4.Statistics on today’s pizzas\n"\
              "5.Quit\n"
              )
        #taking inout from the menu
        choice = int(input("Please enter your choice >"))

        #for choice 1
        if choice==1:#new order
            count=0
            flag=0
            while True:
                count+=1  
                if password_check() :
                    print("Valid password")
                    flag=1
                    break
                else:
                    print("Access Denied")
                    print(f"You have {3-count} tries left")
                    if count==3:
                        break
            if flag==1:
                
                print("Enter the number of pizzas to bake:")
                num_piz = int(input())
                if num_piz<=maxPizzas:
                    for j in range(1,num_piz+1):
                        todaysPizzas.append(Adding(c,j))
                    print(f"Pizzas Ordered: {num_piz}   (: ")
                    maxPizzas = maxPizzas - num_piz
                    c+=j
                else:
                    print(f"We can make only {maxPizzas}")
                    for j in range(1,maxPizzas+1):
                        todaysPizzas.append(Adding(c,j))
                    print("\nPizzas ordered (:")
                    print(f"No pizzas ordered: {maxPizzas} \n")
                    maxPizzas = 0
                    c+=j
        
        elif choice==2: #change/update order
            count=0
            flag=0
            #password check
            while True:
                count+=1
                if password_check():
                    flag=1
                    break
                else:
                    print("Invalid Password ):")
                    print(f"You have {3-count} tries left")
                    if count==3:
                        break
            #if password check done 
            if flag==1:
                ordnum = int(input("Enter the order number you want change:"))
                obj = todaysPizzas[ordnum-1]
                while True:
                    #displaying menu..!
                    print("Papa John, what would you like to change?\n"\
                          "1.Size\n"\
                          "2.Cheese filled or not\n"\
                          "3.Number of cheese toppings\n"\
                          "4.Number of pepperoni toppings\n"\
                          "5.Number of mushroom toppings\n"\
                          "6.Number of vegetable toppings\n"\
                          "7.Quit\n"
                          )
                    #taking choice for the above menu
                    choice = int(input("Enter choice >"))
                    #acting according to the choice
                    if choice==1:
                        obj.set_size(input("Enter the new size:"))
                    elif choice==2:
                        obj.set_stuffed_cheese(bool(int(input("Enter 1 for cheese dough 0 for no cheese dough"))))
                    elif choice==3:
                        obj.set_cheese_toppings(int(input("Enter new number for cheese toppings:")))
                    elif choice==4:
                        obj.set_pepermoni_toppings(int(input("Enter new number for pepermoni toppings:")))
                    elif choice==5:
                        obj.set_mushroom_toppings(int(input("Enter new number for mushroom toppings:")))
                    elif choice==6:
                        obj.set_vegetable_toppings(int(input("Enter new number for vegetable toppings:")))
                    elif choice==7:
                        print("Thanks for updating")
                        break
                    else:
                        print("Invalid choice")
                    #displaying the updated order
                print("After Updating the order")
                print(obj)
                    


                    # s = f'\tPizza size:{obj.size}\n\tNumber of Cheese Toppings: {obj.no_cheese_toppings}\n'\
                    #     f'\tNumber of Pepermoni Toppings: {obj.no_pepermoni_toppings}\n'\
                    #     f'\tNumber of Mushrrom Toppings: {obj.no_mushroom_toppings}\n'\
                    #     f'\tCheese Filled Dough: {obj.stuffedWithCheese}\n'\
                    #     f'\tNumber of veggie toppings: {obj.veggieToppings}\n'\
                    #     f'\tTotal Cost of the pizza after updating: {obj.calcCost()}$\n'
                    
                    #print(s)
                    
    
        elif choice==3:#display details of pizza based on sizes
            print("Enter the pizza size, to get the details:")
            ch = input()
            for i in todaysPizzas:
                if i.size==ch:
                    s = f'\tPizza size:{i.size}\n\tNumber of Cheese Toppings: {i.no_cheese_toppings}\n'\
                        f'\tNumber of Pepermoni Toppings: {i.no_pepermoni_toppings}\n'\
                        f'\tNumber of Mushrrom Toppings: {i.no_mushroom_toppings}\n'\
                        f'\tCheese Filled Dough: {i.stuffedWithCheese}\n'\
                        f'\tNumber of veggie toppings: {i.veggieToppings}\n'\
                        f'\tTotal Cost of the pizza after updating: {i.calcCost()}$\n'
                    print(s)

        elif choice==4: # statistics
            #calculating all the terms required for statistics
            small, medium, large, ct, mt, pt, vt, cd, cost = 0, 0, 0, 0, 0, 0, 0, 0, 0
            cheapest = 99999
            costliest = 0
            #getting the details from todays pizzas
            for i in todaysPizzas:
                if i.size=='small':
                    small+=1
                elif i.size=='medium':
                    medium+=1
                else:
                    large+=1
                
                ct+= i.no_cheese_toppings
                mt+= i.no_mushroom_toppings
                pt+= i.no_pepermoni_toppings
                vt+= i.veggieToppings
                if i.is_stuffed_cheese:
                    cd+=1
                cost+=i.calcCost()

                if cheapest>i.calcCost():
                    cheapest = i.calcCost()
                    cheapestPizza = i
                if costliest<i.calcCost():
                    costliest = i.calcCost()
                    costliestPizza = i

            total = DeluxePizza.numberOfPizzas

            #displaying the menu to choose between different statistics
            while True:
                print("Papa John, what information would you like?\n"\
                      "1.Cost and details of cheapest pizza\n"\
                      "2.Cost and details of most costly pizza\n"\
                      "3.Number of pizzas sold today\n"\
                      "4.Number of pizzas of a specific size\n"\
                      "5.Average cost of pizzas\n"\
                      "6.Quit"
                    )
                #taking the user input for the above menu
                ch = int(input("Enter your choice>"))
                #acting according to the choice
                if ch==1:
                    print("Cheapest pizza details:")
                    print(cheapestPizza)
                elif ch==2:
                    print("Most costliest pizza details:")
                    print(costliesPizza)
                elif ch==3:
                    print("Total number of Pizzas told:",total)
                elif ch==4:
                    print("Total small pizzas:", small)
                    print("Total medium pizzas:", medium)
                    print("Total large pizzas:", large)
                elif ch==5:
                    print("Average cost of Pizzas:",cost/total)
                elif ch==6:
                    print("Thanks for watching the statistics ")
                    break
                else:
                    print("Invalid choice")
        #end the total software after giving 5                             
        elif choice==5: # end
            print("Thanks for using, Done for the day!")
            break
        else:
            print("Invalid choice\n Choose again:")

    #getting pizzas based on size
    def pizzasOfSizes(siz):
        count=0
        for i in todaysPizzas:
            if i.size==siz:
                print(f"Pizza #{count}")
                print(i)
                count+=1
        print(f"Our Chef, made {count} size pizzas today!")
    #taking the size from user
    siz = input("Enter the pizza size to get information of specific size:")
    pizzasOfSize(siz)

    #method to get the lowest price
    def lowestPrice():
        j=0
        for i in todaysPizzas:
            if cheapest>i.calcCost():
                cheapest = i.calcCost()
                cheapestPizza = i
                index = j
            j+=1
        return index
    #method to get highest price
    def highestPrice():
        j=0
        for i in todaysPizzas:
            if costliest<i.calcCost():
                costliest = i.calcCost()
                costliestPizza = i
                index = j
            j+=1
        return index

    #to get prices of pizzas less than the requested price
    def cheaperThan(price):
        print(f"The pizzas price less than {pizza} are")
        for i in todaysPizzas:
            if i.calcCost()<price:
                cost = i.calcCost()
                print(f"No: {i.n} Price: {i.cost}")

    #method to display total pizzas according to size
    def numberOfPizzasOfSize():
        small, medium, large = 0, 0, 0
        for i in todaysPizzas:
            if i.size=='small':
                small+=1
            elif i.size=='medium':
                medium+=1
            else:
                large+=1
        print("Total small pizzas:", small)
        print("Total medium pizzas:", medium)
        print("Total large pizzas:", large)

    #calculating cost of all pizzas
    def totalCost():
        cost=0
        for i in todaysPizzas:
            cost+=i.calcCost()
        return cost
    
    savedata = [] #list to save data
    def save_Pizza():
        savedata.append(['Total Pizzas and Amount Recieved', DeluxePizza.numberOfPizzas, totalCost()] )
        todaysPizzas = []
    print("End for the day want to save the data ?")
    inp = int(input("Enter 1 to save and 0 to not save"))
    if inp==1:
        save_Pizza()
    def displaySavedData():
        print(savedata)

    print("Want to see the data saved?")
    inp = int(input("Enter 1 to see and 0 to not see"))
    if inp==1:
        displaySavedData()
    print("End for the day, See you (: (:")
    

'''print()
print("Todays Statistics:")
print("Total number of pizzas sold:", DeluxePizza.numberOfPizzas)
print("Total small pizzas:", small)
print("Total medium pizzas:", medium)
print("Total large pizzas:", large)
print("Total Cheese Toppings used:", ct)
print("Total Mushroom Toppings used:", mt)
print("Total veggie Toppings used:", vt)
print("Total pepermoni Toppings used:", pt)
print("Total Cheesed Dough pizzas:", cd)'''


    
