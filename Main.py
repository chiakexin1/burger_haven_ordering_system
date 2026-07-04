import AddData
import RetrieveData
import EditData
import DeleteData
import OrderSystem
import PrintBill
import SalesReport
import warnings
import pandas as pd
from openpyxl import load_workbook

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

data_file = 'BurgerHaven.xlsx'
wb = load_workbook(data_file)
ws = wb['MasterList']
order_sheet = wb['Customer_Order']
cols = [0,1,2,3,4,5,6]

def menu():
    while True:
        print("\n--- Burger Haven System ---")
        print("1. Create Burger Product")
        print("2. List Menu Items")
        print("3. Edit Burger Product")
        print("4. Delete Burger Product")
        print("5. Food Ordering System")
        print("6. Print Bill for Customer")
        print("7. Generate Monthly Sales Report")
        print("8. Exit System")

        menu_choose = input("Enter your menu: ").strip()

        if menu_choose == "1":
            AddData.add_burger_product(ws, wb, data_file)

        elif menu_choose == "2":
            df = pd.read_excel(data_file, sheet_name='MasterList', header=0, usecols=cols)
            RetrieveData.retrieve_burger_product(df)
        
        elif menu_choose == "3":
            EditData.edit_burger_product(ws, wb, data_file)
        
        elif menu_choose == "4":
            DeleteData.delete_burger_product(ws, wb, data_file)
        
        elif menu_choose == "5":
            OrderSystem.food_ordering_system(ws, wb, data_file)

        elif menu_choose == "6":
            PrintBill.print_customer_bill(data_file)


        elif menu_choose == "7":
            SalesReport.generate_sales_report(data_file)    

        elif menu_choose == "8":
            print("Exiting the system. Thank you!")
            break
    
        else:
            print("Invalid choice. Please try again.")
menu()
