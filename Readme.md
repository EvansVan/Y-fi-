# Y-fi 
Simple python script to change router password

# General Info
This is a script that i intend to use to access my home router and change the wifi password using python. The script will select a password from a textfile containing pre-selected passwords.

# Technologies
I am using the python selenium package for web control and os for file management.

# Setup
* pip install selenium 
* pip install os

# Usage
* Copy this repository to your local machine. 
* cd to local repo location.
* Provide the new password as text in the pass.txt file found in the test folder.
* Edit net.py file with your router ip and login details.
* Python run net.py from the local machine.


# TO-DO
I also want to leverage the use of api's in this process to enable me to have a list of member numbers  who can be added or removed, to whom the password is shared via text after every change.
