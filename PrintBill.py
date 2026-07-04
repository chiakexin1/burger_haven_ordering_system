import pandas as pd
from datetime import datetime

def print_customer_bill(data_file):
    try:
        customer_id = input("Enter Customer ID to print bill: ")

        
        df = pd.read_excel(data_file, sheet_name="Customer_Order")
        df.columns = df.columns.str.strip()  # Strip any leading/trailing spaces

        
        customer_id_col = next((col for col in df.columns if col.lower().replace(" ", "") == "customerid"), None)
        name_col = next((col for col in df.columns if "name" in col.lower()), None)
        payment_col = next((col for col in df.columns if "payment" in col.lower()), None)
        date_col = next((col for col in df.columns if "date" in col.lower()), None)
        time_col = next((col for col in df.columns if "time" in col.lower()), None)
        products_col = next((col for col in df.columns if "ordered" in col.lower()), None)
        amount_col = next((col for col in df.columns if "amount" in col.lower()), None)

        if not all([customer_id_col, name_col, payment_col, date_col, time_col, products_col, amount_col]):
            print("Error: Required columns not found in the sheet.")
            return

       
        order_df = df[df[customer_id_col].astype(str) == str(customer_id)]

        if order_df.empty:
            print(f"No order found for Customer ID: {customer_id}")
            return

        customer_name = order_df.iloc[0][name_col]
        payment_method = order_df.iloc[0][payment_col]
        date = order_df.iloc[0][date_col]
        time = order_df.iloc[0][time_col]
        datetime_str = f"{date} {time}"

        total_amount = 0.0
        ordered_items = []

        for _, row in order_df.iterrows():
            items = str(row[products_col]).split(',')
            price = float(row[amount_col])
            total_amount += price
            ordered_items.extend([item.strip() for item in items])

        # Receipt content
        bill_lines = [
            "               BURGER HAVEN",
            "        123 Foodie Street, Kuala Lumpur",
            "     Tel: +60 12-345 6789 | burgerhaven.my",
            "==================================================",
            f"Date & Time     : {datetime_str}",
            f"Customer ID     : {customer_id}",
            f"Customer Name   : {customer_name}",
            "--------------------------------------------------",
            "Ordered Items:"
        ]
        for item in ordered_items:
            bill_lines.append(f"  - {item}")
        bill_lines.extend([
            "--------------------------------------------------",
            f"Total Amount    : RM{total_amount:.2f}",
            f"Payment Method  : {payment_method}",
            "==================================================",
            "      Thank you for ordering at Burger Haven!",
            "         We value your feedback 💬",
            "",
            " Please click the link to leave a review:",
            " https://burgerhaven.my/feedback",
            "==================================================",
            "               Thank You ",
            "            Please come again. 🍔 ",
            "==================================================\n",
        ])

        # Display & Save
        print("\n" + "\n".join(bill_lines))
        filename = f"Receipt_{customer_id}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("\n".join(bill_lines))

        print(f"\nReceipt saved as '{filename}'")

    except Exception as e:
        print("An error occurred:", e)
