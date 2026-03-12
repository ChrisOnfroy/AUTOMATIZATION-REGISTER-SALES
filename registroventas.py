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
            product_bol = True
            while product_bol:
                name_product = input("Product : ").strip()
                if name_product and not name_product.isdigit():
                    product_bol = False
                elif name_product.isdigit():
                    print("Error: the name to product only cant numbers")
                else:
                    print("Error: the name of the product cant empty")
            
            price_bol= True            
            while price_bol:
                try:
                    price_unitario = int(input("Price : "))
                    if price_unitario > 0:
                        price_bol = False
                    else:
                        print("Error: the price to product is only positive")
                except ValueError:
                    print("Error: please enter a valide number")
            
            amount_bol = True
            while amount_bol:
                try:
                    amount_sales = int(input("Amount : "))
                    if amount_sales > 0:
                        amount_bol = False
                    else:
                        print("Error: the quantity is only positive")
                except ValueError:
                    print("Error: please enter a valide number")

            sales[counter] = [name_product, price_unitario ,amount_sales]

            bol_sale = True
            while bol_sale :
                try :
                    new_sale = int(input("""Do you want to enter another sale?:
                        1 → Yes
                        2 → NO
                        Enter →  """))
                    if new_sale == 1:
                        bol_sale = False
                    if new_sale >= 3 or new_sale <= 0:
                        print("No validated")
                        bol_sale = True
                    print("-------------------------------------------")
                    amount = sales[counter][2] 
                    price  = sales[counter][1]
                    
                    individual_sale = totalcalculation(amount, price)
                    
                    values += individual_sale

                    if new_sale == 2 :
                        print("-------------------------------------------")
                        historial_sales(sales, values)
                        print("-------------------------------------------")
                        bol_sale = False
                        is_true = False
                except ValueError:
                    print("plesae write a num")

        