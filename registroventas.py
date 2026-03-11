from totalventa import totalcalculation
from historialventa import historial_sales
def registerventas():
    is_true = True
    counter = 0
    sales = {}
    values = 0

    while is_true :
        counter += 1 
        print("-------------------------------------------")
        name_product = input("Product : ")
        price_unitario = int(input("Price : "))
        amount_sales = int(input("amount : "))

        sales[counter] = [name_product, price_unitario ,amount_sales]
    
        new_sale = int(input("""Do you want to enter another sale?:
        1 → Yes
        2 → NO
        Enter →  """))
        print("-------------------------------------------")
        amount = sales[counter][2] 
        price  = sales[counter][1]
        
        individual_sale = totalcalculation(amount, price)
        
        values += individual_sale
                
        if new_sale == 2 :
            print("-------------------------------------------")
            historial_sales(sales, values)
            print("-------------------------------------------")
            is_true = False
            
