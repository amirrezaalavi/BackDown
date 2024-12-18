# What is this?
BackDown is a python project for uploading folders to a samba/SMB server and Downloading from server to client device. The idea came from me having to manually backu my coworkers Data to the main server because they forget to do it manually. It simply works using `pysmb` library

> [!abstract] Note!
> This is not a complete Project and hasn't been fully tested yet.

# How does it works?

## 1.The whole process
User should run `main.py` using python3, e.g. `python3 main.py` (shell arguments are not supported yet); then a menu of Options will appear. User should Initialize some profiles and then do what they want.

## 2. Describing files
The `upload.py` and `download.py` files are for uploading a folder to a server (defined by user). `main.py` is for when the program starts and handling early user input. it also contains `profiles[]` which is the array of different profiles as Objects, and `current_profile` which defines what profile user wants to work with. Finally `initialize.py` is for defining a new profile, which contains these data:
* `client_folder_path` : Address of the folder on client machine which program will write data to/ read data from it.
* `server_ip` : IPv4 address of the server which client wants to work with.
* `server_share` : Name of the Shared folder on the server(root folder of share)
* `server_remote_folder` : Address of the folder on server which user wants to work with
* `server_username` : Username of the server
* `server_password` : Password for the server
These variables would be saved as Objects of a class.
