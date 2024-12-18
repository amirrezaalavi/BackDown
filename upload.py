# Imports
from smb.SMBConnection import SMBConnection
import platform
import os


# Variable Definition
client_name = platform.node()


# Function(s)
def Upload_folder_to_samba(profile): # Import one profile as Object
    # Create an SMB connection
    conn = SMBConnection(profile.server_username, profile.server_password, client_name, profile.server_ip , use_ntlm_v2=True) # client_name is the name  for identification from the server side

    try:
        # Connect to the Samba server
        conn.connect(profile.server_ip, 445)

        # Reverse check every folder and upload files
        for root, dirs, files in os.walk(profile.client_folder_path):
            for file in files:
                client_file_path = os.path.join(root, file) # Full Path to file, e.g. /home/share/file1
                # Define remote file path
                relative_path = os.path.relpath(client_file_path, profile.client_folder_path) # e.g. ./file1
                remote_file_path = os.path.join(profile.server_remote_folder, relative_path).replace(os.sep, '/')

                # Create folders on the remote server if they don't exist
                remote_dir = os.path.dirname(remote_file_path)
                try:
                    conn.createDirectory(profile.server_share, remote_dir)
                except Exception as e: # This will set e as whatever error occurs
                    print(f"Directory {remote_dir} already exists or cannot be created: {e}")

                # Upload the file
                with open(client_file_path, 'rb') as client_file:
                    conn.storeFile(profile.server_share, remote_file_path, client_file)

                print(f"Uploaded {client_file_path} to {remote_file_path}")
    except :
        print(f"An Error was occured : {Exception}")
    finally:
        # Disconnect from the Samba server ( even if uploading was not successful)
        conn.close()

# Example usage
#   profile.client_folder_path = 'path/to/client/folder'  # Replace with your client folder path
#   profile.server_share = 'your_profile.server_share'                  # Replace with your Samba share name
#   profile.server_username = 'your_profile.server_username'            # Replace with your username
#   profile.server_password = 'your_profile.server_password'            # Replace with your password
#   profile.server_ip = 'server_profile.server_ip'                     # Replace with your Samba server IP address
#   profile.server_remote_folder = 'remote/folder/path'      # Replace with the desired remote folder path
#
#   upload_folder_to_samba(profile.client_folder_path, profile.server_share, profile.server_username, profile.server_password, profile.server_ip, profile.server_remote_folder)
