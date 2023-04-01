# Casey Hsu Student ID: 101376814
# Professor: Michael
# Assignment 1

# Employee Fields Dictionary
employeeFields = {
    "id":"Employee ID", "name":"Employee Name", "position":"Employee Position", 
    "years":"Years Employed", "discountID":"Discount ID"
}

# Item Fields Dictionary
itemFields = {
    "itemId":"Item ID", "itemName":"Item Name", "price":"Item Price",
}

# Validation Tuple
validPositions = ("manager", "hourly")

# Lists
employeeList = []
itemList = []

# Menu Function
def displayMenu():
    print("\n------------------------------------------------------")
    print("|                                                    |")
    print("|               1. Add a New Employee                |")
    print("|             2. Create a Inventory Item             |")
    print("|                 3. Place an Order                  |")
    print("|             4. Print Employee Summary              |")
    print("|                    5. Exit                         |")
    print("|                                                    |")
    print("------------------------------------------------------\n")
    return menuInput()

# Menu Option Function
def menuInput():
    while True:
        try:
            option = int(input("Please select from one of the options: "))
            if option in [1, 2, 3, 4, 5]:
                return option
            else:
                print("Invalid menu option, please try again")
        except ValueError:
            print("Invalid menu option, please try again")

# Menu Options
def menuOptions():
    while True:
        option = displayMenu()
        if option == 1:
            print("\nAdding New Employee\n")
            menuLoop(addEmployee, "add another employee?")
        elif option == 2:
            print("\nCreating Inventory Item\n")
            menuLoop(addItem, "add another item?")
        elif option == 3:
            print("\nPlacing a Order\n")
            menuLoop(placeOrder, "make another purchase?")
        elif option == 4:
            print("\nPrinting Employee Summary\n")
            menuLoop(viewEmployeeSummary, "view employee summary again?")
        elif option == 5:
            print("\nThank you for using the System")
            exit()
        else:
            print("\nInvalid option, please try again")

# Menu Loop Function
def menuLoop(keyType="id", key="id"):
    while True:
        keyType()
        if input(f"Would you like to {key} (y/n): ").lower() == "n":
            break

# Search Function
def search(array, key, keyType="id"):
    for employee in array:
        if employee[keyType] == key:
            return True
    return False

# Input Conversion
def convertInput(inp, inpType, fieldList):
    if inpType not in fieldList:
        return False
    if inpType == "name":
        return str(inp.title())
    elif inpType == "position":
        return str(inp.lower())
    elif inpType == "id":
        return int(inp)
    elif inpType == "years":
        return int(inp)
    elif inpType == "discountID":
        return int(inp)
    elif inpType == "itemId":
        return int(inp)
    elif inpType == "itemName":
        return str(inp.title())
    elif inpType == "price":
        return float(inp)

# Input Validation
def validateInput(inp, inpType, fieldList):
    if inpType not in fieldList:
        return False   
    if inpType == "id":
        if not inp.isnumeric() or int(inp) < 0:
            return False
        else:
            inp = int(inp)
            if search(employeeList, inp, "id"):
                print("\nEmployee ID is already in use.")
                return False
            else:
                return True
    elif inpType == "name":
        if inp == "":
            return False
        else:
            return all(inp.isalpha() or inp.isspace() for inp in inp)
    elif inpType == "position":
        return inp.lower() in validPositions
    elif inpType == "years":
        return inp.isnumeric() and int(inp) > 0 and int(inp) < 50
    elif inpType == "discountID":
        if not inp.isnumeric() or int(inp) < 0:
            return False
        else:
            inp = int(inp)
            if search(employeeList, inp, "discountID"):
                print("\nDiscount ID is already in use.")
                return False
            else:
                return True   
    elif inpType == "itemId":
        if not inp.isnumeric() or int(inp) < 0:
            return False
        else:
            inp = int(inp)
            if search(itemList, inp, "itemId"):
                print("\nItem ID is already in use.")
                return False
            else:
                return True
    elif inpType == "itemName":
            if inp == "":
                return False
            else:
                return all(inp.isalpha() or inp.isalnum() or inp.istitle() or inp.isspace() for inp in inp)
    elif inpType == "price":
        if not inp.isnumeric() or float(inp) < 0:
            return False
        return inp.isnumeric() or float(inp) > 0
    
# Add Employee Function
def addEmployee():
    employee = {}
    for field in employeeFields:
        while True:
            employee[field] = input(f"Please enter {employeeFields[field].lower()}: ")
            if validateInput(employee[field], field, employeeFields):
                employee[field] = convertInput(employee[field], field, employeeFields)
                break
            else:
                print(f"\nThe provided {employeeFields[field].lower()} is invalid, please try again\n")
    employee.update({"discounts": 0})
    employee.update({"purchases": 0})
    employeeList.append(employee)
    print(f"\nEmployee has been added to the system successfully\n")
    
# Add Item Function
def addItem():
    item = {}
    for field in itemFields:
        while True:
            item[field] = input(f"Please enter {itemFields[field].lower()}: ")
            if validateInput(item[field], field, itemFields):
                item[field] = convertInput(item[field], field, itemFields)
                break
            else:
                print(f"\nThe provided {itemFields[field].lower()} is invalid, please try again\n")
    itemList.append(item)
    print(f"\nItem has been added to the system successfully\n")

# Display Items Function
def displayItems():
    print("Item ID: | Item Name: | Price:\n")
    for item in itemList:
        print(f"Item ID: {item['itemId']} | Item Name: {item['itemName']} | Price: ${item['price']}\n")

# Employee Summary Function
def viewEmployeeSummary():
    if len(employeeList) == 0:
        print("\nNo employees have been added to the system yet\n")
        return False
    for employee in employeeList:
        print(f"Employee ID: {employee['id']} | Employee Name: {employee['name']} | Employee Position: \
{employee['position']} | Employee Years: {employee['years']} | Employee Discounts: {employee['discounts']} \
| Employee Purchases: {employee['purchases']} | Employee Discount ID: {employee['discountID']}\n")

# Order Function
def placeOrder():
    if len(itemList) == 0:
        print("\nNo Items have been added to the system yet\n")
        return False
    displayItems()
    while True:
        try:
            discountId = int(input("Please enter Discount ID: "))
            if search(employeeList, discountId, "discountID"):
                break
            else:
                print("Discount ID not found, please try again")
        except ValueError:
            print("Discount ID not found, please try again")
    while True:
        try:
            itemId = int(input("Please enter Item ID: "))
            if search(itemList, itemId, "itemId"):
                break
            else:
                print("Item ID not found, please try again")
        except ValueError:
            print("Item ID not found, please try again")
    for employee  in employeeList:
        if employee["discountID"] == discountId:
            for item in itemList:
                if item["itemId"] == itemId:
                    if employee["position"] == "manager":
                        if employee["years"] > 5:
                            discount = (employee["years"] * 0.1) + 0.1
                        else:
                            discount = (employee["years"] * 0.02) + 0.1
                    elif employee["position"] == "hourly":
                        discount = employee["years"] * 0.02
                        if discount > 0.1:
                            discount = 0.1
                    if employee["discounts"] < 200:
                        employee["discounts"] += round((item["price"] * discount), 2)
                        employee["purchases"] += item["price"] - (item["price"] * discount)
                        print(f"\nOrder placed, the total price is ${item['price'] - (item['price'] * discount)}\n")
                        return
                    else:
                        employee["purchases"] += item["price"]
                        print(f"\nOrder placed, the total price is ${item['price']}\n")
                        return
    print("\nOrder failed, please try again\n")

menuOptions()