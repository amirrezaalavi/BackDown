
# Imports
import os
from smb.SMBConnection import SMBConnection
import platform


# Variable Definition
client_name = platform.node() # Other methods are OS dependent


# Function(s)
def download_folder_from_samba(profile):
    # Create an SMB connection
    conn = SMBConnection(profile.server_username, profile.server_password, client_name, profile.server_ip, use_ntlm_v2=True)

    try:
        # Connect to the Samba server
        conn.connect(profile.server_ip, 445)

        # List all files in the remote directory
        remote_files = conn.listPath(profile.server_share, profile.server_remote_folder)

        for remote_file in remote_files:
            if not remote_file.isDirectory:
                remote_file_path = os.path.join(profile.server_remote_folder, remote_file.filename).replace(os.sep, '/') # File address, then standardize to /../ format
                local_file_path = os.path.join(profile.client_folder_path, remote_file.filename) # Full address on local Computer

                # Create local directories if they don't exist
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

                # Download the file
                with open(local_file_path, 'wb') as local_file:
                    conn.retrieveFile(profile.server_share, remote_file_path, local_file)

                print(f"Downloaded {remote_file_path} to {local_file_path}")

            elif remote_file.isDirectory:
                # Recursively download subdirectories (to copy inside of every folder as well)
                download_folder_from_samba(profile.server_share, profile.server_username, profile.server_password, profile.server_ip,
                                            os.path.join(profile.server_remote_folder, remote_file.filename),
                                            os.path.join(profile.client_folder_path, remote_file.filename))
    except :
        print(f"An Error was occured : {Exception}")

    finally:
        # Disconnect from the Samba server
        conn.close()

# Example usage
#   profile.server_share = 'your_profile.server_share'                  # Replace with your Samba share name
#   profile.server_username = 'your_profile.server_username'            # Replace with your username
#   profile.server_password = 'your_profile.server_password'            # Replace with your password
#   profile.server_ip = 'server_profile.server_ip'                     # Replace with your Samba server IP address
#   profile.server_remote_folder = 'remote/folder/path'      # Replace with the desired remote folder path
#   profile.client_folder_path = 'path/to/local/folder'    # Replace with your local folder path
#
#   download_folder_from_samba(profile.server_share, profile.server_username, profile.server_password, profile.server_ip, profile.server_remote_folder, profile.client_folder_path)
