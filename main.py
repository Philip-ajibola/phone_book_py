import time
contact_info = {}
list1=[]
def collect_info(name,number,address,email_address):
    global contact_info
    contact_info = {"contact_name": name,"phone_number": number,"contact_address": address,"contact_email": email_address}
def users_info():
    name = str(input("enter name "))
    pone_number= str(input("enter phone number "))
    address = str(input("enter address "))
    email_address = str(input("enter email address "))
    collect_info(name,pone_number,address,email_address)

def add_new_contact():
    contact = contact_info
    list1.append(contact)
    print("saving>>>>>>>>")
    time.sleep(2)
    return "contact saved"
def clear_list():
    list1.clear()
def search_contact(name):
    user_info = ""
    condition = False
    if list1:
        print(list1)
        for contact in list1:
            print(len(contact))
            for key, value in contact.items():
              if key == "contact_name" and name.lower() == value :
                condition = True
                for keys, user in contact.items():
                    user_info += f"{keys}:  {user} \n  "

                break
        if condition:
            return user_info
        else:
            print(f"{name} is not in list of contact")

    else:
        return "Your contact list is empty "
def delete_contact(name):
        if list1:
            for contact in list1:
                for key, value in contact.items():
                    if name.lower() == value:
                        list1.remove(contact)
                    break
            return f"{name} Contact Deleted"
        else:
            return "No contact Found "


def edit_contact(name,new_name):
    if list1:
        for contact in list1:
            for key,value in contact.items():
                if name.lower() == value:
                    contact[key] = new_name
                    break
        return "Contact Edited"
    else:
        return "No Contact Found "
def display_all_contact():
    if list1:
        result =""
        for contact in list1:
         for name in contact.values():
             result += f"{name}\n"
             break
        return result
    else:
        return 'No Contact Found'
def main_menu():
    print("""
    ----------->>>> PHONE BOOK <<<<--------------
    [<1>] Display All Contact
    [<2>] Add New Contact
    [<3>] Search Contact
    [<4>] Exit
    ----------->>>>>>        <<<<<<<------------------
    """)
def operate_phone_book():
    main_menu()
    while True:
     number = int(input())
     match(number):
        case 1:
            print(display_all_contact())
            userInput = int(input("[<1>] Back to Main Menu "))
            while userInput != 1:
                userInput = int(input("Enter a valid number "))
            if (userInput == 1):
                time.sleep(1)
                main_menu()
        case 2:
            users_info()
            print(add_new_contact())
            userInput = int(input("[<1>] Back to Main Menu \n [<2>] Add More Contact "))
            while userInput != 1 and userInput != 2:
                userInput = int(input("Enter a valid number "))
            while userInput ==2 :
                print()
                users_info()
                print(add_new_contact())
                userInput = int(input("[<1>] Back to Main Menu \n [<2>] Add More Contact "))


            if (userInput == 1):
                time.sleep(1)
                main_menu()
        case 3:
            print()
            name = str(input("Enter Name You are searching for "))
            print(search_contact(name))
            userInput = int(input(" [<1>] Edit Contact          [<2>] Delete Contact \n              [<3>] Back To Main Menu "))
            while userInput < 1 or userInput > 3:
                userInput = int(input("Enter a valid number "))
            if userInput == 1:
               new_name = str(input("Enter The name you want to save number with "))
               print( edit_contact(name,new_name))
               time.sleep(1)
               main_menu()
            elif userInput == 2:
                print(delete_contact(name))
                time.sleep(1)
                main_menu()
            elif userInput == 3:
                time.sleep(1)
                main_menu()
        case 4:
            print("Good Bye")
            break
        case _:
            print("Enter valid input")

#operate_phone_book()