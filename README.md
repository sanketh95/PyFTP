A Simple FTP Client

>Requirements:
Python 2.7

### Usage:
python main.py

List of available commands
Note: Commands are case sensitive

#### pwd
Displays the present working directory

#### cd 
*	usage: cd <dirname>
*	Changes the current directory to 

#### ls
*	usage: ls <dirname:optional>
*	Gives a directory listing of the `dirname`. If no argument provided lists the current directory contents

#### help
*	usage: help <list of command names:optional>
*	Gives the description of the commands

#### search
*	usage: search [-R:optional] keyword
*	Searches and gives a list of dir/file containing substring keyword in the pwd. -R does a recursive search

#### exit
*	Closes the connection to ftp server and exits the application

