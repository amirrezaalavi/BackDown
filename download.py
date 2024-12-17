import os
from smb.SMBConnection import SMBConnection
import platform


client_name = platform.node()
def download_folder_from_samba(server_share, server_username, server_password, server_ip, server_remote_folder, local_folder_path):
    # Create an SMB connection
    conn = SMBConnection(server_username, server_password, client_name, server_ip, use_ntlm_v2=True)

    try:
        # Connect to the Samba server
        conn.connect(server_ip, 445)

        # List all files in the remote directory
        remote_files = conn.listPath(server_share, server_remote_folder)

        for remote_file in remote_files:
            if not remote_file.isDirectory:
                remote_file_path = os.path.join(server_remote_folder, remote_file.filename).replace(os.sep, '/')
                local_file_path = os.path.join(local_folder_path, remote_file.filename)

                # Create local directories if they don't exist
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

                # Download the file
                with open(local_file_path, 'wb') as local_file:
                    conn.retrieveFile(server_share, remote_file_path, local_file)

                print(f"Downloaded {remote_file_path} to {local_file_path}")

            elif remote_file.isDirectory:
                # Recursively download subdirectories (to copy inside of every folder as well)
                download_folder_from_samba(server_share, server_username, server_password, server_ip,
                                            os.path.join(server_remote_folder, remote_file.filename),
                                            os.path.join(local_folder_path, remote_file.filename))

    finally:
        # Disconnect from the Samba server
        conn.close()

# Example usage
#   server_share = 'your_server_share'                  # Replace with your Samba share name
#   server_username = 'your_server_username'            # Replace with your username
#   server_password = 'your_server_password'            # Replace with your password
#   server_ip = 'server_server_ip'                     # Replace with your Samba server IP address
#   server_remote_folder = 'remote/folder/path'      # Replace with the desired remote folder path
#   local_folder_path = 'path/to/local/folder'    # Replace with your local folder path
#
#   download_folder_from_samba(server_share, server_username, server_password, server_ip, server_remote_folder, local_folder_path)
