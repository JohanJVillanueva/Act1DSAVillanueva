##### CODE FOR DATA INSIDE LIST ##########
import random
j = 0
# Data of Random First Names
firstnames = [
    " Kenneth ", "Carl", "Adrian", "Claire",
    "Christine", "Adrian", "Cristina", "Kaye", "Joel", "Alexandra", "Kyle",
    "Mahid", "Rey", "Geoffrey", "Maxene", "Ilao", "Joy", "Jose", "Nathaniel",
    "Mark", "Vinz", "John", "Yvette", "Cristan", "Julia-Ann", "Dan", "Gerald",
    "Patrick", "Ronalyn", "Kyla", "Melody", "Miguel", "Ann", "Mariz", "Kathlyn",
    "Kim Luzel", "Nathaniel", "Gwendeline", "Dana", "Rommuel", "John", "Sean",
    "Maria", "Angelica", "Joshua", "Aldrin ", "Jay", "Kylene", "Johan", "Arriane "]

# Data of Random Last Names
lastnames = [
    "dela Cruz", "Garcia", "Reyes", "Ramos", "Mendoza", "Santos",
    "Flores", "Gonzales", "Bautista", "Villanueva", "Fernandez", "Cruz",
    "de Guzman", "Lopez", "Perez", "Castillo", "Francisco", "Rivera",
    "Aquino", "Castro", "Sanchez", "Torres", "de Leon", "Domingo", "Martinez",
    "Rodriguez", "Santiago", "Soriano", "Delos Santos", "Diaz", "Hernandez",
    "Tolentino", "Valdez", "Ramirez", "Morales", "Mercado", "Tan", "Aguilar",
    "Navarro", "Manalo", "Gomez", "Dizon", "del Rosario", "Javier", "Corpuz",
    "Gutierrez", "Salvador", "Velasco", "Miranda"]

# Data of Random Sample Addresses
addresses = [
    'Cavite', 'Laguna', 'Batanggas', 'Rizal', 'Queszon', 'Mindoro',
    'Marinduque', 'Romblon', 'Palawan', 'Manila', 'Makati', 'Pasig',
    'Sta. Mesa', 'Pasay', 'Recto', 'Hidalgo', 'Quiapo', ]

# Declaration of Addressbook List
addressbook = []

# Generates a list with 30 different names, locations and phone numbers
# Max data for addressbook is 50
for i in range(30):
    # makes random phone number
    name = firstnames[random.randrange(0, 49)]
    lname = lastnames[random.randrange(0, 49)]
    addr = addresses[random.randrange(0, 17)]
    randnum = random.randrange(100000, 900000)
    addressbook.append([i + 1, name, lname, addr, randnum])

###### END OF DATA GENERATION ########################
i = 30


# Function for 'Main Menu'. This for the
# users to be able to pick and  Choose an action.
def PrintInput():
    j = 0
    print("------------------Address Book------------------")
    print("---------------by Johan Villanueva--------------")
    print("---------------BSCOE 2-5 DSA Act 1--------------")
    print("What would you like to do?")
    print("1.) Add Contact")
    print("2.) Edit Contact")
    print("3.) Delete Contact")
    print("4.) View Contacts")
    print("5.) Search Address Book")
    print("6.) Exit\n")
    print("Choose an option:\n")
    pass


# Function for 1.) Adding Contacts
def AddContact():
    global i
    if i > 49:
        # Checking if Addressbook is full or not
        print("Address Book full, please delete Entries first.")
        start()
    else:
        # Gathering info from User
        print("------------------Add Contact------------------")
        fname = input("Please enter your first name | Format: First Name\n")
        lname = input("Please enter your last name | Format: Last Name\n")
        address = input("Please enter your address\n")
        cnumber = int(input("Please enter your contact number | Format: No spaces\n"))

        # Making a Temporary List to be able to append to the main list
        i += 1
        templist = []
        templist.append(i)
        templist.append(fname.capitalize())
        templist.append(lname.capitalize())
        templist.append(address.capitalize())
        templist.append(cnumber)

        # Appending it to the main list
        print(f' You have added these information to the list {templist}')
        addressbook.append(templist)

        start()


def EditContact():
    global i
    print("------------------Edit Contact------------------")
    entrynumber = int(input("Input the desired Entry Number to "
                            "be able to edit the contents of said entry: \n"))
    if entrynumber > i:
        print("Given Entry number is not present in the list")
        start()
    else:
        # If Entry number is valid; user proceeds to edit the entry
        entrynumber = entrynumber - 1
        print(addressbook[entrynumber])

        print("Please re-input the following to be able to edit the contact:")

        # Gathering info from User
        fname = input("Please enter your first name | Format: First Name\n")
        lname = input("Please enter your last name | Format: Last Name\n")
        address = input("Please enter your address\n")
        cnumber = int(input("Please enter your contact number | Format: No spaces\n"))

        # Making a Temporary List to be able to append to the main list
        templist = []
        templist.append(entrynumber + 1)
        templist.append(fname.capitalize())
        templist.append(lname.capitalize())
        templist.append(address.capitalize())
        templist.append(cnumber)

        # Appending it to the main list
        print(f' You have added these information to the list {templist}')
        addressbook[entrynumber] = templist

        start()


def DeleteContact():
    # Prints out the whole addressbook, for user to access
    global addressbook
    length = len(addressbook)
    for k in addressbook:
        print(k)

    print("------------------Delete Contact------------------")
    entrynumber = int(input("Input the desired Entry Number to Delete it from the List: \n"))

    if entrynumber > i:
        print("Given Entry number is not present in the list")
        start()
    else:
        remove = entrynumber - 1

        print(addressbook[remove])
        addressbook.pop(remove)

        # Removes 1 from the first index of the nested list, to reflect the deletion of an Entry
        lengthofadd = len(addressbook) - entrynumber + 1
        z = 0
        while z < lengthofadd:
            addressbook[remove][0] = remove + 1
            remove += 1
            z += 1

        # Prints out the whole addressbook, for user to access
        for k in addressbook:
            print(k)

        start()


def ViewContacts():
    # Prints out the whole addressbook, for user to access
    for k in addressbook:
        print(k)
    start()


def SearchContacts():
    print("------------------Search Contact------------------")
    print("What would you like to search for??")
    print("1.) First Name")
    print("2.) Last Name")
    print("3.) Address")
    print("4.) Contact Number")

    # Making a Temporary List to be able to append to the main list
    templistofindex = []
    # Waiting for users input on which search term will be used.
    search = input("Choose an option:\n")

    def contactsearch(num):
        # Based on the num, the for statement will look for the specific search term
        # Only on the num index, for it to use less compute.
        if num == 4:
            for i in range(len(addressbook)):
                if addressbook[i][num] == search:
                    templistofindex.append(i)
                else:
                    pass
        else:
            for i in range(len(addressbook)):
                if addressbook[i][num] == search.capitalize():
                    templistofindex.append(i)
                else:
                    pass

    # if statements to ask user which specific attribute of the Contact will he/she search for
    if search == '1':
        search = input("Input First Name: \n")
        contactsearch(1)
    elif search == '2':
        search = input("Input Last Name: \n")
        contactsearch(2)
    elif search == '3':
        search = input("Input Address: \n")
        contactsearch(3)
    elif search == '4':
        search = int(input("Input Contact Number: \n"))
        contactsearch(4)
    else:
        print("Invalid Input")
        start()

    # If search is found, program will print out the desired search query
    z = 1
    if len(templistofindex) > 0:
        print(f'Found instances of {search} in the list')
        print(f'{search} is on index {templistofindex}')
        z = 0
        while z < len(templistofindex):
            forprint = templistofindex[z]
            print(addressbook[forprint])
            z += 1
    # If search is not found in the list:
    else:
        print(f'{search} not found')

    start()


# Function for Main Menu
def start():
    global j
    while j < 1:
        PrintInput()
        answer = input()
        # If statements for the various functions of the program
        if answer == '1':
            print("You have chosen \"1.) Add Contact\"\n")
            AddContact()
            j += 1

        elif answer == '2':
            print("You have chosen \"2.) Edit Contact\"\n")
            EditContact()
            j += 1

        elif answer == '3':
            print("You have chosen \"3.) Delete Contact\"\n")
            DeleteContact()
            j += 1

        elif answer == '4':
            print("You have chosen \"4.) View Contacts\"\n")
            ViewContacts()
            j += 1

        elif answer == '5':
            print("You have chosen \"5.) Search Address Book\"\n")
            SearchContacts()
            j += 1

        elif answer == '6':
            print("Exiting program. Thank you!")
            break

        else:
            print("Please choose a correct option")


start()
