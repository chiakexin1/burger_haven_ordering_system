def retrieve_burger_product(df):
    # Check if the DataFrame is empty (no products available)
    if df.empty:
        print("\nNo products available in the menu.")
    else:
        # Display the menu with a formatted table if products are available
        print("\n--- Burger Haven Menu ---\n")
        print(df.to_string(index=False, justify='center')) # Show all product data without index
