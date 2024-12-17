#import os
from smb.SMBConnection import SMBConnection
import platform
import os

client_name = platform.node()
def upload_folder_to_samba(client_folder_path, server_share, server_username, server_password, server_ip, server_remote_folder):
    # Create an SMB connection
    conn = SMBConnection(server_username, server_password, client_name, server_ip , use_ntlm_v2=True) # client_name is the name  for identification from the server side

    try:
        # Connect to the Samba server
        conn.connect(server_ip, 445)

        # Reverse check every folder and upload files
        for root, dirs, files in os.walk(client_folder_path):
            for file in files:
                client_file_path = os.path.join(root, file) # Full Path to file, e.g. /home/share/file1
                # Define remote file path
                relative_path = os.path.relpath(client_file_path, client_folder_path) # e.g. ./file1
                remote_file_path = os.path.join(server_remote_folder, relative_path).replace(os.sep, '/')

                # Create folders on the remote server if they don't exist
                remote_dir = os.path.dirname(remote_file_path)
                try:
                    conn.createDirectory(server_share, remote_dir)
                except Exception as e: # This will set e as whatever error occurs
                    print(f"Directory {remote_dir} already exists or cannot be created: {e}")

                # Upload the file
                with open(client_file_path, 'rb') as client_file:
                    conn.storeFile(server_share, remote_file_path, client_file)

                print(f"Uploaded {client_file_path} to {remote_file_path}")

    finally:
        # Disconnect from the Samba server ( even if uploading was not successful)
        conn.close()

# Example usage
#   client_folder_path = 'path/to/client/folder'  # Replace with your client folder path
#   server_share = 'your_server_share'                  # Replace with your Samba share name
#   server_username = 'your_server_username'            # Replace with your username
#   server_password = 'your_server_password'            # Replace with your password
#   server_ip = 'server_server_ip'                     # Replace with your Samba server IP address
#   server_remote_folder = 'remote/folder/path'      # Replace with the desired remote folder path
#
#   upload_folder_to_samba(client_folder_path, server_share, server_username, server_password, server_ip, server_remote_folder)
