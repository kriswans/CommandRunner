# SerialNumberTool
The intent of this program is to connect to a list of devices and pull the raw inventory data (to include serial numbers) while associating with hostname and IP address. It can also execute a single IOS command across a list of devices. Output files are in csv format. Error handling has been added to record device connectivity issue.

Notes:

-When installing please be sure to install paramiko for ssh connectivity.
-All .py files should reside in the same directory
-Run SNT_Main as the main program. It will launch a menu to call functions from the other files.



Roadmap: 

1. seperate aaa credentials from program

2. multi-line command execution
