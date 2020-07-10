
class Category:

    def __init__(self, categoria):
        self.categoria = categoria
        self.ledger = []

    def __str__(self):
        result = self.categoria.center(30,"*")
        for x in self.ledger:
            result = result + "\n" + x["description"].ljust(23)[:23] + str("%.2f"%float(x["amount"])).rjust(7)
        result = result + "\n" + "Total: " + str("%.2f"%float(self.get_balance()))
        return result

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):            
            self.ledger.append({"amount": amount*-1, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for x in self.ledger: total = total + x["amount"]
        return total
    
    def transfer(self, cantidad, aquien):
        if self.check_funds(cantidad):
            self.withdraw(cantidad, "Transfer to " + aquien.categoria)
            aquien.deposit(cantidad, "Transfer from " + self.categoria)
            return True
        return False
    
    def check_funds(self, amount):
        total = 0
        for x in self.ledger: 
            total = total + x["amount"]
        if total < amount: return False
        return True




def create_spend_chart(categories):

    sum = 0
    result = "Percentage spent by category\n"
    spent = []
    total = 0
    porcentajes = []
    maxlen = 0
    a = ""

   

    for x in categories:
        for y in x.ledger:
            if y["amount"] < 0:
                sum = sum + abs(y["amount"])
                total = total + abs(y["amount"])
        spent.append([sum,x.categoria])
        sum = 0

    print(spent)

    for x in spent:
        this = [int(x[0]*100/total),x[1]]
        porcentajes.append(this)

    print(porcentajes)

    #porcentajes = sorted(porcentajes, reverse=True)
    print(porcentajes)
    index = 100
    while index >=0:
        result= result + str(index).rjust(3)+"|"
        for n in range(len(porcentajes)):
            if porcentajes[n][0] >= index:
                result = result + " o "
            else:
                result = result + "   "
        result = result + " \n"
        index = index - 10
    result = result + "    "
    for n in range(len(spent)):
        result = result + "---"
    result = result + "-\n    "
    for n in porcentajes:
        if len(n[1]) > maxlen:
            maxlen = len(n[1])
    
    for n in range(maxlen):
        for x in porcentajes:
            try:
                a = str(x[1])[n]
                result = result + a.center(3)
            except:
                a = " "
                result = result + a.center(3)
        result = result + " \n    "
    
    return result[:-5]
    

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

print(actual==expected)
print(actual)
print(expected)
