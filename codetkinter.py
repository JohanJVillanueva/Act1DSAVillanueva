##### CODE FOR DATA INSIDE LIST ##########
import random
import string

#Data of Random First Names
firstnames = [" Kenneth ", "Carl", "Adrian", "Claire",
"Christine", "Adrian", "Cristina", "Kaye", "Joel", "Alexandra", "Kyle",
"Mahid", "Rey", "Geoffrey", "Maxene", "Ilao", "Joy", "Jose", "Nathaniel",
"Mark", "Vinz", "John", "Yvette", "Cristan", "Julia-Ann", "Dan", "Gerald",
"Patrick", "Ronalyn", "Kyla", "Melody", "Miguel", "Ann", "Mariz", "Kathlyn",
"Kim Luzel", "Nathaniel", "Gwendeline", "Dana", "Rommuel", "John", "Sean",
"Maria", "Angelica", "Joshua", "Aldrin ", "Jay", "Kylene", "Johan", "Arriane " ]

#Data of Random Last Names
lastnames = [
"dela Cruz", "Garcia", "Reyes", "Ramos", "Mendoza", "Santos",
"Flores", "Gonzales", "Bautista", "Villanueva", "Fernandez", "Cruz",
"de Guzman", "Lopez", "Perez", "Castillo", "Francisco", "Rivera",
"Aquino", "Castro",  "Sanchez", "Torres", "de Leon", "Domingo", "Martinez",
"Rodriguez", "Santiago", "Soriano", "Delos Santos", "Diaz", "Hernandez",
"Tolentino", "Valdez", "Ramirez", "Morales", "Mercado", "Tan", "Aguilar",
"Navarro", "Manalo", "Gomez", "Dizon", "del Rosario", "Javier", "Corpuz",
"Gutierrez", "Salvador", "Velasco", "Miranda"]

#Data of Random Sample Addresses
addresses = [
'Cavite', 'Laguna', 'Batanggas', 'Rizal', 'Queszon', 'Mindoro',
'Marinduque', 'Romblon', 'Palawan', 'Manila', 'Makati', 'Pasig',
'Sta. Mesa', 'Pasay', 'Recto', 'Hidalgo','Quiapo',]

#Declaration of Addressbook List
addressbook = []

#Generates a list with 30 different names, locations and phone numbers
#Max data for addressbook is 50
for i in range (30):
    name = firstnames[random.randrange(0, 49)]
    lname = lastnames[random.randrange(0, 49)]
    addr = addresses[random.randrange(0, 17)]
    randnum = random.randrange(100000, 900000)
    addressbook.append([i+1,name,lname, addr, randnum])

###### END OF DATA GENERATION ########################
i=30


#Importing TKINTER Library, Text, Messagebox, Label and TTK
import tkinter as tk
from tkinter import Text
from tkinter import messagebox
from tkinter import Label
from tkinter import ttk

#Initializing Tkinter, establishing paramters like size, resizability and bg color
root = tk.Tk()
root.geometry("315x600")
root.title("Address Book")
root.configure(bg='CadetBlue')
root.resizable(False, False)

#Function for 1.) Adding Contacts
def AddContact():
    global addressbook
    new = tk.Toplevel(root)
    new.geometry("500x500")
    new.title("Add Contact")
    new.configure(bg='goldenrod')
    new.resizable(False, False)

    # Create a Label in New window
    title = Label(new, text="Add Contact", font=('Helvetica 17 bold')).pack(pady=30)

    #firstname
    firstname_text = Label(new, text="First Name", font=('Helvetica 17 bold')).pack(pady=5)
    fname1 = tk.Entry(new, text="0", width=50)
    fname1.pack()

    #lastname
    lastname_text = Label(new, text="Last Name", font=('Helvetica 17 bold')).pack(pady=5)
    lname1 = tk.Entry(new, text="1", width=50)
    lname1.pack()

    #address
    address_text = Label(new, text="Address", font=('Helvetica 17 bold')).pack(pady=5)
    address1 = tk.Entry(new, text="2", width=50)
    address1.pack()

    #contactnumber
    contactnumber_text = Label(new, text="Contact Number", font=('Helvetica 17 bold')).pack(pady=5)
    cnumber1 = tk.Entry(new, text="3", width=50)
    cnumber1.pack()

    # Submit button function for Adding Contacts
    def grabinfo():
        # Getting entry from user
        fname = fname1.get()
        lname = lname1.get()
        address = address1.get()
        cnumber = cnumber1.get()

        # Appending the Entry to a temporary list
        global i
        i += 1
        templist = []
        templist.append(i)
        templist.append(fname.capitalize())
        templist.append(lname.capitalize())
        templist.append(address.capitalize())
        templist.append(cnumber)

        #Check if Address Book is past 50 users
        if i > 49:
            tk.messagebox.showinfo(title="Cannot Add Info", message="Address Book is Full, delete some contacts first before proceeding")
        else:
            #Appending it to the main list
            addressbook.append(templist)
            tk.messagebox.showinfo(title="Info", message=f'sucessfully added {fname} {lname}, {address}, {cnumber} to the list')


    #Submit Button and Information Label
    get = tk.Button(new, text="Submit", command=grabinfo).pack(pady=10)
    addinfo = Label(new, text="This sub-window will allow you to add a Contact to the Adress Book \n simply fill up the needed information on top and click submit to be able to \n append the information. Thank you!", font=('Helvetica 8 bold')).pack(pady=10)

#Function for 2.) Editing Contacts
def EditContact():
    global addressbook
    new = tk.Toplevel(root)
    new.geometry("850x850")
    new.title("Edit Contact")
    new.configure(bg='palegreen4')
    new.resizable(False, False)


    #Mapping the addressbook to be all strings, so that it could be viewed in the Tkinter Text Widget
    addressbook_list = map(str, addressbook)

    #Addressbook widget
    text = Text(new, width=50, height=50)
    text.place(x=10, y=10)

    #Iterating the list to have a \n on each index
    for x in addressbook_list:
        text.insert(tk.END, x + '\n')

    # Create a Label in New window
    title = Label(new, text="Edit Contact", font=('Helvetica 17 bold')).place(x=450, y=10)

    # entrynumber
    entrynumber_text = Label(new, text="Input Entry number", font=('Helvetica 17 bold')).place(x=450, y=50)
    entrynumber2 = tk.Entry(new, text="123123", width=50)
    entrynumber2.place(x=450, y=90)

    #Description
    entrynumber_text = Label(new, text="Change the Info of Selected Entry", font=('Helvetica 17 bold')).place(x=450, y=170)
    # firstname
    firstname_text = Label(new, text="First Name", font=('Helvetica 17 bold')).place(x=450, y=210)
    fname2 = tk.Entry(new, text="123", width=50)
    fname2.place(x=450, y=260)

    # lastname
    lastname_text = Label(new, text="Last Name", font=('Helvetica 17 bold')).place(x=450, y=310)
    lname2 = tk.Entry(new, text="4531", width=50)
    lname2.place(x=450, y=360)

    # address
    address_text = Label(new, text="Address", font=('Helvetica 17 bold')).place(x=450, y=410)
    address2 = tk.Entry(new, text="2657", width=50)
    address2.place(x=450, y=460)

    # contactnumber
    contactnumber_text = Label(new, text="Contact Number", font=('Helvetica 17 bold')).place(x=450, y=500)
    cnumber2 = tk.Entry(new, text="567", width=50)
    cnumber2.place(x=450, y=550)

    # Submit button function for Editing Contacts
    def editinfo():
        # Getting entry from user
        entry = entrynumber2.get()
        entry = int(entry)
        entrynumber = int(entry)
        fname = fname2.get()
        lname = lname2.get()
        address = address2.get()
        cnumber = cnumber2.get()

        # Appending the Entry to a temporary list
        templist = []
        templist.append(entrynumber)
        templist.append(fname.capitalize())
        templist.append(lname.capitalize())
        templist.append(address.capitalize())
        templist.append(cnumber)



        addressbook[entrynumber-1] = templist

        # Mapping the addressbook to be all strings, so that it could be viewed in the Tkinter Text Widget
        addressbook_list = map(str, addressbook)

        # Addressbook widget
        text = Text(new, width=50, height=50)
        text.place(x=10, y=10)

        # Iterating the list to have a \n on each index
        for x in addressbook_list:
            text.insert(tk.END, x + '\n')

        tk.messagebox.showinfo(title="Info", message=f'Sucessfully edited '
                                                     f'entry number: {entrynumber} \n to '
                                                     f'be: {fname}, {lname},{address},{cnumber} to the list')

    # Submit Button and Information Label
    get = tk.Button(new, text="Submit", command=editinfo).place(x=450, y=650)
    editinginfo = Label(new, text="This sub-window will allow you to edit an \n "
                                  "existing entry to the Adress Book.  simply fill up \n the needed "
                                  "information on top and click submit to \n be able to  edit the information. "
                                  "Thank you!", font=('Helvetica 8 bold')).place(x=450, y=580)

#Function for 3.) Deleting Contacts
def DeleteContact():
    global addressbook
    new = tk.Toplevel(root)
    new.geometry("850x850")
    new.title("Delete Contact")
    new.configure(bg='salmon')
    new.resizable(False, False)

    # Mapping the addressbook to be all strings, so that it could be viewed in the Tkinter Text Widget
    addressbook_list = map(str, addressbook)

    # Addressbook widget
    text = Text(new, width=50, height=50)
    text.place(x=10, y=10)

    # Iterating the list to have a \n on each index
    for x in addressbook_list:
        text.insert(tk.END, x + '\n')

    # Create a Label in New window
    title = Label(new, text="Delete Contact", font=('Helvetica 17 bold')).place(x=450, y=10)

    # entrynumber
    entrynumber_text = Label(new, text="Input Entry number to Delete", font=('Helvetica 17 bold')).place(x=450, y=50)
    entrynumber3 = tk.Entry(new, text="5646", width=50)
    entrynumber3.place(x=450, y=90)

    # Delete button function for Deleting Contacts
    def deleteinfo():
        entry = entrynumber3.get()
        entry = int(entry)
        entrynumber = int(entry)

        remove = entrynumber - 1

        addressbook.pop(remove)

        lengthofadd = len(addressbook) - entrynumber + 1
        z = 0
        while z < lengthofadd:
            addressbook[remove][0] = remove + 1
            remove += 1
            z += 1

        # Mapping the addressbook to be all strings, so that it could be viewed in the Tkinter Text Widget
        addressbook_list = map(str, addressbook)

        # Addressbook widget
        text = Text(new, width=50, height=50)
        text.place(x=10, y=10)

        # Iterating the list to have a \n on each index
        for x in addressbook_list:
            text.insert(tk.END, x + '\n')

        tk.messagebox.showinfo(title="Info", message=f'Sucessfully deleted entry number: {entrynumber}')

    # Delete Button and Information Label
    get = tk.Button(new, text="Delete", command=deleteinfo).place(x=450, y=150)
    deletinginfo = Label(new, text="This sub-window will allow you to"
                                   " delete an  existing entry to the \n Adress Book. Simply "
                                   "input the Entry number to Delete it. Thank you!"
                                   "", font=('Helvetica 8 bold')).place(x=450, y=112)



#Function for 4.) Searching Contacts
def SearchContact():
    global addressbook
    new = tk.Toplevel(root)
    new.geometry("850x850")
    new.title("Search Contact")
    new.configure(bg='dark slate blue')
    new.resizable(False, False)

    # Mapping the addressbook to be all strings, so that it could be viewed in the Tkinter Text Widget
    addressbook_list = map(str, addressbook)

    # Addressbook widget
    text = Text(new, width=50, height=50)
    text.place(x=10, y=10)

    # Iterating the list to have a \n on each index
    for x in addressbook_list:
        text.insert(tk.END, x + '\n')

    # Create a Label in New window
    title = Label(new, text="Search Contact", font=('Helvetica 17 bold')).place(x=450, y=10)

    # Search button function for each spcecific attribute of Contacts
    def contactsearch(num):
        global search
        if num == 1:
            search = fname4.get()
        elif num == 2:
            search = lname4.get()
        elif num == 3:
            search = address4.get()
        elif num == 4:
            search = int(cnumber4.get())

        templistofindex = []
        if num == 4:
            for i in range(len(addressbook)):  # loops i from 0 to the length of mylist (num of rows)
                if addressbook[i][num] == search:  # compare each cell to search value
                    templistofindex.append(i)
                    #print("Found")
        else:
            for i in range(len(addressbook)):  # loops i from 0 to the length of mylist (num of rows)
                if addressbook[i][num] == search.capitalize():  # compare each cell to search value
                    templistofindex.append(i)
                    #print("Found")
                else:
                    pass
        z=1
        if len(templistofindex) > 0:
                z=0

                # Addressbook widget
                text = Text(new, width=50, height=50)
                text.place(x=10, y=10)

                while z < len(templistofindex):
                        forprint = templistofindex[z]
                        #print(addressbook[forprint])
                        names = str(addressbook[forprint])
                        text.insert(tk.END, names + '\n')
                        z+=1

                tk.messagebox.showinfo(title="Info", message=f'Found instances of {search} in the list')
                tk.messagebox.showinfo(title="Info", message=f'{search} is on index {templistofindex}')




        else:
                text = Text(new, width=50, height=50)
                text.insert(tk.END, f'{search} not found')
                text.place(x=10, y=10)
                tk.messagebox.showinfo(title="Info", message=f'Did not found instances of {search} in the list')

    def getfname():
        contactsearch(1)
        pass

    def getlname():
        contactsearch(2)
        pass

    def getaddress():
        contactsearch(3)
        pass

    def getcnumber():
        contactsearch(4)
        pass

    #Description
    entrynumber_text = Label(new, text="Search up using the"
                                       " following info: ", font=('Helvetica 15 bold')).place(x=450, y=50)
    # firstname
    firstname_text = Label(new, text="First Name", font=('Helvetica 17 bold')).place(x=450, y=110)
    fname4 = tk.Entry(new, text="0123", width=50)
    fname4.place(x=450, y=140)
    getfname = tk.Button(new, text="Search", command=getfname).place(x=450, y=160)

    # lastname
    lastname_text = Label(new, text="Last Name", font=('Helvetica 17 bold')).place(x=450, y=210)
    lname4 = tk.Entry(new, text="114323", width=50)
    lname4.place(x=450, y=240)
    getlname = tk.Button(new, text="Search", command=getlname).place(x=450, y=260)

    # address
    address_text = Label(new, text="Address", font=('Helvetica 17 bold')).place(x=450, y=310)
    address4 = tk.Entry(new, text="2123132", width=50)
    address4.place(x=450, y=340)
    getaddress = tk.Button(new, text="Search", command=getaddress).place(x=450, y=360)

    # contactnumber
    contactnumber_text = Label(new, text="Contact Number", font=('Helvetica 17 bold')).place(x=450, y=400)
    cnumber4 = tk.Entry(new, text="234", width=50)
    cnumber4.place(x=450, y=430)

    # Search Button and Information Label
    getcnumber = tk.Button(new, text="Search", command=getcnumber).place(x=450, y=450)
    searchinfo = Label(new, text="This sub-window will allow you to search an \n existing "
                                 "entry of the Adress Book.  Simply fill up \n one of the needed information "
                                 "on top and click Search to \n be able to  search the Address Book."
                                 " Thank you!",font=('Helvetica 8 bold')).place(x=450, y=480)

#Function for Viewing of Contacts
def ViewContact():
    global addressbook
    new = tk.Toplevel(root)
    new.geometry("500x850")
    new.title("View Contacts")
    new.configure(bg='rosy brown')
    new.resizable(False, False)

    # Mapping the addressbook to be all strings, so that it could be viewed in the Tkinter Text Widget
    addressbook_list = map(str, addressbook)

    # Addressbook widget
    text = Text(new, width=50, height=50)
    text.pack(pady=10)

    # Iterating the list to have a \n on each index
    for x in addressbook_list:
       text.insert(tk.END, x + '\n')

#################### MAIN MENU ####################
############### LABELS FOR MAIN MENU ##############
titletext = Label(root, text="Address Book", font=("Rockwell", 16)).place(x=85,y=30)
authortext = Label(root, text="by Johan J. Villanueva", font=("Rockwell", 16)).place(x=48,y=500)
credittext = Label(root, text="BSCOE 2-5 | DSA ACT 1", font=("Rockwell", 16)).place(x=40,y=530)

############### BUTTONS FOR MAIN MENU ##############
add = tk.Button(root, text ="Add Contact", command = AddContact, height= 9, width=15).place(x=25, y=100)
edit = tk.Button(root, text ="Edit Contact", command = EditContact, height= 9, width=15).place(x=170, y=100)
delete = tk.Button(root, text ="Delete Contact", command = DeleteContact, height= 9, width=15).place(x=25, y=260)
search = tk.Button(root, text ="Search Contact", command = SearchContact, height= 9, width=15).place(x=170, y=260)
view = tk.Button(root, text ="View Contacts", command = ViewContact, height= 3, width=15).place(x=100, y=420)







root.mainloop()