import os
from http import server

def initialize():

    client_folder_path = "./"
    server_ip = ""
    server_share = "./"
    server_remote_folder = ""
    server_username = ""
    server_password = ""
    temp = ""
    check = True # For Ensuring every data Enters correctly

    print("Initialization ...")
    # Input every temp file with temp variable, then assign it
    # Starting with client_folder_path
    while check:
        temp = input("Enter the Path to the folder on the computer : ")
        if (os.path.exists(temp) == False):
            print("Wrong Path, Try Again")
            continue
        else:
            client_folder_path = temp
            print(f"Local folder changed to {client_folder_path}")
            temp = ""
            break
    # server_ip
    while check:
        temp = input("Enter ip address of the server (IPv4 only): ")
        valid = True
        temp_ip = temp.split('.')
        for part in temp_ip :
            try :
                int(part)
            except :
                valid = False
                print("Wrong IP address, try again")
                break
        if(not valid):
            break
        server_ip = temp
        print(f"IP successfully changed to {server_ip}")
        temp = ""
    # This part is for data that we can't check
    while check:
        temp = input("Enter the name of the shared folder on the Server : ")
        if(temp == ""):
            print("String empty")
            continue
        server_share = temp
        server_remote_folder = input("Enter the address of the folder on the Server : ") # This can possibly be empty and its fine

    # In this part we collect optional data
    server_username = input("Enter Server username (optional) : ")

    server_password = input("Enter Server password (optional) : ")
