def add_burger_product(ws, wb, file_name):
    # Loop until a unique Product ID is entered
    while True:
        product_id = input("Enter Product ID: ").strip()
        id_exists = False

        # Check if the entered Product ID already exists (starting from row 2 to skip header)
        for row in ws.iter_rows(min_row=2):  # Skip header row
            if str(row[0].value).strip() == product_id:
                id_exists = True
                break

        if id_exists:
            print("Product ID already used. Please enter a unique Product ID.")
        else:
            break

    # Prompt user for product details
    category = input("Enter Category (Burgers/Sides/Beverages): ").strip()
    name = input("Enter Product Name: ").strip()
    description = input("Enter Description: ").strip()

    # Input and validate price (must be a positive number)
    while True:
        try:
            price = float(input("Enter Price: ").strip())
            if price < 0:
                print("Price cannot be negative. Please enter again.")
            else:
                break
        except ValueError:
            print("Invalid price. Please enter a number.")

    # Input and validate chef recommendation (must be Yes or No)
    while True:
        chef_recommendation = input("Chef Recommendation (Yes/No): ").strip().capitalize()
        if chef_recommendation in ["Yes", "No"]:
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    # Input and validate rating (must be a number between 1 and 5)
    while True:
        try:
            rating = float(input("Enter Rating (1 - 5): ").strip())
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid rating. Please enter a number between 1 and 5.")

    # Append new product details to the worksheet
    ws.append([product_id, category, name, description, price, chef_recommendation, rating])
    wb.save(file_name)
    print("Product added successfully!")
