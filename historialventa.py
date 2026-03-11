def historial_sales(sales, value):
    print("\nDAILY SALES SUMMARY")
    print()
    
    for product in sales.values():
        print(f"Product: {product[0]}")
        print(f"total amount sales: {product[2]}")
        print()
    
    print(f"total raised: ${value}")