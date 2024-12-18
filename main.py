# BackDown: a Project for uploading/downloading a folder to/from a SMB or Samba Server
# Main program to run on startup
#

# Imports
import upload
import download
from initialize import Profile

# Variable Definition
profiles = []
current_profile = -1


print("Welcome to BackDown !")

# Function(s)
def Change_profile():
    global profiles, current_profile
    if (len(profiles) == 0):
        print("No profiles available. Please Initialize first")
        return
    for i in profiles :
        print(i.name)
    try : # Error catching in case User does not Enter number
        temp_profile = int(input("Enter profile number : "))
        if (temp_profile < len(profiles)):
            current_profile = temp_profile
            print(f"Profile changed to profile_{temp_profile}")
        else:
            print("Profile does not exists")
    except Exception as e:
        print(f"Error occured : {e}")




def Main():
    global profiles, current_profile
    # Input option
    option = 0
    temp_continue = True

    while temp_continue == True:
        temp_option = input("""
        Choose the right option:
            1.Initialize
            2.Change profile
            3.Backup
            4.Backdown
            5.Exit
            """)
        try:
            option = int(temp_option)
            # I didn't use switch case here because professor told us in class :)
            if (option == 1):
                temp_obj = Profile(profiles)
                profiles.append(temp_obj)
                continue

            elif (option == 2):
                Change_profile()
                continue

            elif (option == 3):
                if (current_profile < 0):
                    print("No profiles available. Please Initialize first")
                else:
                    upload.Upload_folder_to_samba(profiles[current_profile])

                continue

            elif (option == 4):
                if (current_profile < 0):
                    print("No profiles available. Please Initialize first")
                else:
                    download.Download_folder_from_samba(profiles[current_profile])
                continue

            elif (option == 5):
                print("GoodBye!")
                break
            else:
                print("Wrong Number")

        except ValueError:
            print("Enter a Number please!")
            continue



Main() # Run the main function at start, maybe in future add args for terminal arguments
