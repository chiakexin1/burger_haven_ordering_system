def delete_burger_product(ws, wb, file_name):
    # Prompt the user to enter the Product ID they wish to delete
    product_id = input("Enter the Product ID to delete: ").strip()
    found = False # Flag to indicate if the product was found and deleted

    # Iterate through all rows starting from the second row (to skip the header)
    for idx, row in enumerate(ws.iter_rows(min_row=2), start=2):  # Skip header
        # Check if the Product ID in the current row matches the input
        if row[0].value == product_id:
            ws.delete_rows(idx) # Delete the row if the Product ID matches
            wb.save(file_name)  # Save the changes to the Excel file
            print("Product deleted successfully!") # Confirmation message
            found = True
            break # Exit the loop once the product is found and deleted

    # If the product was not found in the list, display a message
    if not found:
        print("Product ID not found. No changes made.")
