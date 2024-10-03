#
#   @file author: Justine Tenorio
#
#
#   This program uses a dictionary to store employee records, 
#   with employee names as keys and Employee objects as values. 
#   The emp.Employee class is used to create employee objects with 
#   attributes like name, ID number, department, and job title.
#
#
import pickle
import emp

################
LOOK_UP = 1 
ADD = 2     
CHANGE = 3  #Global Constants
DELETE = 4  
PRINT = 5
QUIT = 9    
################

#Global constant for the filename
FILENAME = 'employee.dat'
    
def main():
    #Load the existing objects dictionary
    mycontacts = load_file()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)

        elif choice == ADD:
            add(mycontacts)
            
        elif choice == CHANGE:
            change(mycontacts)
            
        elif choice == DELETE:
            delete(mycontacts)
        
        elif choice == PRINT:
            print_all(mycontacts)
            
    save_file(mycontacts)
    print("File saved.")
    exit = input("Press enter key to exit...")

#
#
#   Prints a menu to choose from and asks for a choice
#
#
def get_menu_choice():
    print()
    print('Menu')
    print('-----------------')
    print("1. Look up an Employee")
    print("2. Add a new Employee")
    print("3. Change an existing Employee")
    print("4. Delete a contact")
    print("5. Prints all")
    print("9. Quit")
    print()

    choice = int(input("Enter your choice: "))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice: "))

    return choice

#
#
#   using pickle, ppens the file employee.dat
#   and loads the employee records
#
#
def load_file():
    try:
        infile = open(FILENAME, 'rb')

        contact_dct = pickle.load(infile)

        infile.close()
    except IOError:
        contact_dct = {}

    return contact_dct

#
#
#   Looks up an employee by name and display their detail
#
#
def look_up(mycontacts):
    #Get a name to look up
    name = input("Enter a name to look up: ")
    
    print(mycontacts.get(name, "The name is not found."))
    

#
#
#    using pickle, Saves the employee records to employee.dat
#
#
def save_file(mycontacts):
    outfile = open(FILENAME, 'wb')

    #Pickle the dictionary to the file and save it
    pickle.dump(mycontacts, outfile)

    outfile.close()
    
    
#
#
#   Adds a new employee to the records
#
#
def add(mycontacts):
    #Asks for dettails about the employee to add
    name = input("Name: ")
    id_num = input("ID: ")
    dept = input("Department: ")
    job = input("Job: ")

    entry = emp.Employee(name, id_num, dept, job)

    #If the name does not exist in the dictionary
    #Add it as a key with the entry object as
    #the associated value
    if name not in mycontacts:
        mycontacts[name] = entry
        print("The entry has been added")

    else:
        print("That name already exists.")

#
#
#   Change details about an existing employee
#
#
def change(mycontacts):
    #Get a name to look up
    name = input("Enter a name to change: ")

    if name in mycontacts:
        id_num = input("Enter the new ID number: ")
        dept = input("Enter the new department: ")
        job = input("Enter the nwe job title: ")

        entry = emp.Employee(name, id_num, dept, job)

        mycontacts[name] = entry
        print("Information update")

    else:
        print("That name is not found.")


#
#
#   Deletes an employee from the records
#
#
def delete(mycontacts):
    name = input("Enter a name to delete: ")

    if name in mycontacts:
        del mycontacts[name]
        print("Entry deleted.")

    else:
        print("That name is not found.")

#
#
#   Prints all the data
#
#
def print_all(mycontacts):
    for name, employee in mycontacts.items():
        print()
        print(f"Name: {name}")
        print(employee)
        print()  # Add a blank line for better readability

main()
