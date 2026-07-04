def edit_burger_product(ws, wb, file_name):
    # Prompt the user to enter the Product ID they want to edit
    product_id = input("Enter the Product ID to edit: ").strip()
    found = False # Flag to track whether the product was found

    # Iterate through the worksheet rows starting from row 2 (to skip header)
    for row in ws.iter_rows(min_row=2):  
        if row[0].value == product_id:
            # Display current product details
            print("\nCurrent product details:")
            print(f"Category: {row[1].value}")
            print(f"Name: {row[2].value}")
            print(f"Description: {row[3].value}")
            print(f"Price: {row[4].value}")
            print(f"Chef Recommendation: {row[5].value}")
            print(f"Rating: {row[6].value}")

            # Ask the user to input new values (optional updates)
            print("\nEnter new details (leave blank if no change)")

            category = input("Enter new category (Burgers/Sides/Beverages): ").strip()
            name = input("Enter new product name: ").strip()
            description = input("Enter new description: ").strip()

            # Update price if valid
            price = input("Enter new price: ").strip()
            if price:
                try:
                    price_val = float(price)
                    if price_val < 0:
                        print("Price cannot be negative. Keeping original value.")
                    else:
                        row[4].value = price_val
                except ValueError:
                    print("Invalid price input. Keeping original value.")

            # Update chef recommendation if valid
            chef_recommendation = input("Enter new chef recommendation (Yes/No): ").strip().capitalize()
            if chef_recommendation in ["Yes", "No"]:
                row[5].value = chef_recommendation
            elif chef_recommendation:
                print("Invalid input for chef recommendation. Keeping original value.")

            # Update rating if valid (between 1 to 5)
            rating = input("Enter new rating (1-5): ").strip()
            if rating:
                try:
                    rating_val = float(rating)
                    if 1 <= rating_val <= 5:
                        row[6].value = rating_val
                    else:
                        print("Rating must be between 1 and 5. Keeping original value.")
                except ValueError:
                    print("Invalid rating input. Keeping original value.")

            # Update other fields only if not empty
            if category:
                row[1].value = category
            if name:
                row[2].value = name
            if description:
                row[3].value = description

            wb.save(file_name)
            print("\nProduct edited successfully!")
            found = True
            break

    # If no matching Product ID was found
    if not found:
        print("\nProduct ID not found. No changes made.")
