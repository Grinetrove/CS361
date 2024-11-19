# User Management Microservice - README
This README provides instructions on how to interact with the User Management Microservice programmatically, detailing how to send requests and receive responses.

# Overview
The microservice allows for user management operations such as registration, login, updating user data, and removing users. It processes requests by reading data from a request.txt file and writes responses to a response.txt file.

# Request Format
Requests are processed by reading from a text file (request.txt) with the following structure:
```
<command>
<username>
<password>
<optional data>
```
## Command List
* add: Registers a new user.
* remove: Removes an existing user.
* login: Logs in a user.
* read: Reads user data.
* update: Updates user data, such as password or other attributes.

## Example Requests
```
add
john_doe
password123
1000
```
***Adds a user 'john_doe' with a total budget of 1000$***
```
add
john_doe
password123
```

***Adds a user 'john_doe' with budget not initialized***
```
add
john_doe
password123
[100, 100, 200, 200, 100, 50, 150, 100]
```
***Adds a user 'john_doe' with individual part budgets***
```
remove
john_doe
password456
```
***Removes a user 'john_doe'***
```
login
john_doe
password123
```
***Confirm a user 'john_doe' exists with a password 'password123'***
```
read
john_doe
password123
```
***Reads all information associated with a user 'john_doe'***
```
update
john_doe
password123
newpassword
```
***Updates the password a user 'john_doe' to 'newpassword' (any non json/dict formatted text will default to a new password)***
```
update
john_doe
password123
{"budget": 2000}
```
***Updates the budget of a user 'john_doe' to 2000***
```
update
john_doe
password123
{"budget": 2000,"password":"newpassword"}
```
***Updates the budget and password of a user 'john_doe' to 2000 and 'newpassword' respectivly***
```
update
john_doe
password123
{"random_statistic": "anything"}
```
***Updates (or creates) a new piece of information for 'john_doe' and saves it as whatever is inputed to be read later***


## Example Results
```
error
Invalid username or password
```
***Returned if a username does not exist or an incorrect password is entered***
```
error
Invalid request format
```
***Returned if incorrect amount of lines is used in command***
```
error
Unknown command
```
***Returned if incorrect command is used***
```
success
User successfully registered
```
***Returned if user is added successfully***
```
error
Username already exists
```
***Returned if add command tries to add username that already exists***
```
success
password:
5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
budget:
1000
Any_Other_info:
info here
```
***Returned if user is read successfully (passwords are hashed - any new info added will add two lines to the read result)***
```
success
User data updated successfully
```
***Returned if user info is updated successfully***
```
error
Invalid update format
```
***Returned if incorrect data format used in update command***
```
success
User removed successfully
```
***Returned if user is removed successfully***



# UML sequence diagram:



![Untitled drawing](https://github.com/user-attachments/assets/08b5a252-197e-401f-b2c6-9fc42e6d362c)









