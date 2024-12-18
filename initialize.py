# Imports
import os


# Class(es)
class Profile:
    # Defining Variables
    name = ""
    client_folder_path = "./"
    server_ip = ""
    server_share = "./"
    server_remote_folder = ""
    server_username = ""
    server_password = ""

    def __init__(self, profiles): # Just forwarded to be able to change in case of adding database

        self.name = f"profile_{len(profiles)}"
        print(f"the Name of this profile is {self.name}")
        self.Initialize()


    def Initialize(self):
        temp = ""
        check = True # For Ensuring every data Enters correctly, just in case we want to save data to database later
        print("Initialization ...")
        # Input every temp file with temp variable, then assign it
        # Starting with client_folder_path
        while check:
            temp = input("Enter the Path to the folder on the computer : ")
            if (os.path.exists(temp) == False):
                print("Wrong Path, Try Again")
                continue
            else:
                self.client_folder_path = temp
                print(f"Local folder changed to {self.client_folder_path}")
                temp = "" # Just for preventing problems
                break
        # server_ip
        while check:
            temp = input("Enter ip address of the server (IPv4 only): ")
            valid = True
            temp_parts = 0
            temp_ip = temp.split('.')
            for part in temp_ip :
                try :
                    int(part)
                    temp_parts += 1
                except :
                    valid = False
                    break
            if (not valid) or temp_parts != 4:
                print("Wrong IP address, try again")
                continue
            self.server_ip = temp
            print(f"IP successfully changed to {self.server_ip}")
            temp = ""
            break
        # This part is for data that we can't check
        while check:
            temp = input("Enter the name of the shared folder on the Server : ")
            if(temp == ""):
                print("String empty")
                continue
            self.server_share = temp
            self.server_remote_folder = input("Enter the address of the folder on the Server : ") # This can possibly be empty and its fine
            break
        # In this part we collect optional data
        self.server_username = input("Enter Server username (optional) : ")

        self.server_password = input("Enter Server password (optional) : ")
