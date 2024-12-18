# What is this?
BackDown is a python project for uploading folders to a samba/SMB server and Downloading from server to client device. The idea came from me having to manually backu my coworkers Data to the main server because they forget to do it manually. It simply works using `pysmb` library

> This is not a complete Project and hasn't been fully tested yet.

# How does it works?

## 1. The whole process
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


## 3. Describing functions and methods and their usage
| Name | Usage |
|:-----|:----:|
|function `main`  |Run the project and interact with user|
|function `download_folder_from_samba`|Download the Folder and copy it to specified Folder|
|function `upload_folder_to_samba`|Upload the specified Folder to the server|
|class `profiles`|Creating profiles for handling Variables|

## 4. Future of the project
Main things I want to add:
1. Save profiles to a file so User won't have to enter data every time. Possibly add DataBase.
2. Terminal Arguments so User won't have to interact with interface every time.
3. Add TUI to make it more convinient.
