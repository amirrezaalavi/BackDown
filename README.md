# What is this?
BackDown is a python project for uploading folders to a samba/SMB server and Downloading from server to client device. The idea came from me having to manually backu my coworkers Data to the main server because they forget to do it manually. It simply works using `pysmb` library

> This is not a complete Project and hasn't been fully tested yet.
---

# How does it works?

## 1. How to run the project

>Since the project was written in python, You need `python3`, `python3-pip` and `python3-venv` or "python3 virtual enviroment" packages. other packages will be installed automatically with pip3.

First clone the project using `git` or download and extract the zip file, then head to the parent folder and enter a Terminal(or Powershell for Windows). write `python3 -m venv BackDown` to recreate the python enviroment. Then type `source BackDown/bin/activate` (or `BackDown\bin\Activate.ps1` for PowerShell)
now to install required packages, run `pip install -r requirements.txt` and then run the project : `python3 BackDown/main.py`

***

## 2. Describing files
The `upload.py` and `download.py` files are for uploading a folder to a server (defined by user). they both require a object of `Profile` method which is inside `initialize.py`. Then using the variables they will try to stablish a connection with server.
`Download_folder_from_samba` inside `download.py` will try to recursivally download every file in `server_remote_folder` parameter of the recieved profile and `Upload_folder_to_samba` from `upload.py` tries to upload the file from `client_folder_path` to the server.
These two parts of program both import `os`, `platform`, `smb.SMBConnection`.
|Name of Lib|Usage|
|:----:|:----:|
|os| Using for finding pathes on the clients system, copying and pasting files, get different kind of pathes|
|smb| For working with remote files on smb server|
|platform | only for platform independent User information|

`Download_folder_from_samba` inside `download.py`, will first recieve a object called platform, then tries to establish a connection using `server_username`, `server_password`, `server_remote_folder`, `client_name`, `server_ip`
> ntlm_v2 is the microsoft security standard for SMB

Then tries to connect to server using port 445 and IPv4. Then lists every file and folder inside the server. Then checks for local folder and if doesn't exist, it will create one. Then for every file, copies the file from the server into the local folder, and for every folder on server, changes relative path to the old relative path + folders name and restarts the function to recursively copy every file over to client computer

`Upload_folder_to_samba` from `upload.py` does similarlly the same thing, Just instead of recursive function methods, it loops inside the folder and send every file with full path to Samba server using `StoreFile()` method.


`main.py` contains a function called `Main()` which is for when the program starts and handling early user input. it also contains `profiles[]` which is the array of different profiles as Objects, and `current_profile` which defines what profile user wants to work with. `main.py` will get user options to choose what function to call, or to make a new object of `Profile` method.
`Main()` will start with showing the menu and prompt user for input, to then call the related function.
Also `Change_profile` is for changing the profile if any other exists.

Finally `initialize.py` contains a class called `Profile` which is for defining a new profile, and contains these parameters:
* `name` : name of the object created by the program itself, pattern is profile_x where x is a natural number.
* `client_folder_path` : Address of the folder on client machine which program will write data to/ read data from it.
* `server_ip` : IPv4 address of the server which client wants to work with.
* `server_share` : Name of the Shared folder on the server(root folder of share)
* `server_remote_folder` : Address of the folder on server which user wants to work with(optional - because user can use the whole shared folder as backup folder).
* `server_username` : Username of the server(optional).
* `server_password` : Password for the server(optional).

`Profile` has an instructor just in case if we want to connect DB later, but now it will only create a name `profile_x` for every profile and calls `Initialize()`, then `Initialize` will loop every part to ensure every variable is not empty.
These variables would be saved as parameters of a class. and be returned to `Main()` to be saved in a new object.

---

## 3. Describing functions and methods and their usage

| Name | Usage |
|:-----|:----:|
|function `Main` |Run the project and interact with user|
|function `Download_folder_from_samba`|Download the Folder and copy it to specified Folder|
|function `Upload_folder_to_samba`|Upload the specified Folder to the server|
|function `Initialize`|Get every parameter from user and save to an object
|class `Profiles`|Creating profiles for handling Variables|

***

## 4. Future of the project
Main things I want to add:
1. Save profiles to a file so User won't have to enter data every time. Possibly add DataBase to store more data.
2. Terminal Arguments so User won't have to interact with interface every time.
3. Add TUI to make it more convinient.
4. Set a scheduler for Automatic Backups
