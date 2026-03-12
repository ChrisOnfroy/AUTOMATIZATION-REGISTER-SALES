# Import functions from other files
# totalcalculation: calculates price × amount for one product
from totalventa import totalcalculation
# historial_sales: shows all sales information
from historialventa import historial_sales


def registerventas():
    # Control variable for the main loop
    # True = continue, False = stop
    is_true = True
    
    # Counts how many products the user enters
    counter = 0
    
    # Empty dictionary to store all products
    # Format: {1: [product, price, amount], 2: [product, price, amount], ...}
    sales = {}
    
    # Accumulator for total value of all sales
    values = 0

    # Main program loop - continues until user chooses to exit
    while is_true:
            # Increase counter for each new product
            counter += 1 
            
            # Print separator line for better readability
            print("-------------------------------------------")
            
            # === PRODUCT NAME INPUT - VALIDATION LOOP ===
            # Control variable for product name validation
            product_bol = True
            
            # Loop until user enters a valid product name
            while product_bol:
                # Ask for product name and remove spaces at start/end
                name_product = input("Product : ").strip()
                
                # Check if name is not empty and not only numbers
                if name_product and not name_product.isdigit():
                    # Valid name - exit the loop
                    product_bol = False
                # Check if name contains only numbers
                elif name_product.isdigit():
                    # Show error - name cannot be only numbers
                    print("Error: the name to product only cant numbers")
                # Name is empty
                else:
                    # Show error - name cannot be empty
                    print("Error: the name of the product cant empty")
            
            # === PRICE INPUT - VALIDATION LOOP ===
            # Control variable for price validation
            price_bol = True
            
            # Loop until user enters a valid price
            while price_bol:
                try:
                    # Ask for price and convert to integer
                    price_unitario = int(input("Price : "))
                    
                    # Check if price is positive
                    if price_unitario > 0:
                        # Valid price - exit the loop
                        price_bol = False
                    else:
                        # Show error - price must be positive
                        print("Error: the price to product is only positive")
                
                # Handle error if user doesn't enter a number
                except ValueError:
                    print("Error: please enter a valide number")
            
            # === AMOUNT INPUT - VALIDATION LOOP ===
            # Control variable for amount validation
            amount_bol = True
            
            # Loop until user enters a valid amount
            while amount_bol:
                try:
                    # Ask for amount and convert to integer
                    amount_sales = int(input("Amount : "))
                    
                    # Check if amount is positive
                    if amount_sales > 0:
                        # Valid amount - exit the loop
                        amount_bol = False
                    else:
                        # Show error - amount must be positive
                        print("Error: the quantity is only positive")
                
                # Handle error if user doesn't enter a number
                except ValueError:
                    print("Error: please enter a valide number")

            # Save product information in the sales dictionary
            # counter = product number (1, 2, 3...)
            # [name_product, price_unitario, amount_sales] = product details
            sales[counter] = [name_product, price_unitario, amount_sales]

            # === CONTINUE OR FINISH - MENU LOOP ===
            # Control variable for the menu
            bol_sale = True
            
            # Loop until user makes a valid choice
            while bol_sale:
                try:
                    # Show menu options
                    new_sale = int(input("""Do you want to enter another sale?:
                        1 → Yes
                        2 → NO
                        Enter →  """))
                    
                    # If user chooses 1 (Yes)
                    if new_sale == 1:
                        # Exit menu loop but continue main loop
                        bol_sale = False
                    
                    # If user chooses invalid number (not 1 or 2)
                    if new_sale >= 3 or new_sale <= 0:
                        print("No validated")
                        bol_sale = True
                    
                    # Print separator line
                    print("-------------------------------------------")
                    
                    # Get amount for current product from sales dictionary
                    amount = sales[counter][2] 
                    
                    # Get price for current product from sales dictionary
                    price  = sales[counter][1]
                    
                    # Calculate total for this product using imported function
                    # amount × price = individual_sale
                    individual_sale = totalcalculation(amount, price)
                    
                    # Add this product's total to the overall total
                    values += individual_sale

                    # If user chooses 2 (No - finish)
                    if new_sale == 2:
                        # Print separator line
                        print("-------------------------------------------")
                        
                        # Show all sales history using imported function
                        # Pass sales dictionary and total values
                        historial_sales(sales, values)
                        
                        # Print final separator line
                        print("-------------------------------------------")
                        
                        # Exit menu loop
                        bol_sale = False
                        
                        # Exit main program loop (stop the program)
                        is_true = False
                
                # Handle error if user doesn't enter a number
                except ValueError:
                    print("plesae write a num")