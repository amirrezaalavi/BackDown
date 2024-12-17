# BackDown: a Project for uploading/downloading a folder to/from a SMB or Samba Server
# Main program to run on startup
#

import upload



option = 0



print("Welcome to BackDown !")
def main(void):
    # Input option
    temp_right_option = False
    while temp_right_option != True:
        temp_option = input("""
            Choose the right option:
                1.Initialize
                2.Backup
                3.Backdown""")
        try:
            option = int(temp_option)
            temp_right_option = True

            # I didn't use switch case here because professor told us in class :)
            if(option == 1):
                Initialization()
            elif(option == 2):
                upload.upload_folder_to_samba()

        except ValueError:
            print("Enter a Number please!")
            continue








def Initialization ():
    pass
