# Main.py
Base Class for all operations including
1. Display all data
2. Add
3. Update
4. Delete
5. Search

and Extra functional such as 
1. Sort
2. About Us
3. Setting
When you create `MyClass` Object it will check 
> if file name is given
> other wise ask from user. 

### load function 
given file name is exit then read line by line and change to list
if file don't exit get user for column name and save it with file name given from __init__ method

### scanner function
- if we can change int or float from data change the datatype
- it is used when we add new data or when we load data 
- it take  array as input and return array of data type changed.
### get column no function 
it is created to avoid code repetition that is used in **Search, Sort, Update** function to ask relative column.

### Search function
if data type is numeric there are three option (greater than, less than and equal)
else data type is string it match the row start with the given characters.

### sort function
the are two option you can chose, ascending and descending order

### setting function 
can change display type (table view and dictionary view)
can change clear output or not
### Show function
Show table function is responsive with the data length.
Show function is content independent it can change with the data.
# Dinosour.py
Dinosaur Class inheritance From `MyClass` from main.py and it contain 
**logo** attribute and **show_logo** function on it own

# Key Features
- Base class is content independent
- Use functional Programming such as **join, map, lambda**
- Use both private and public methods.
- Use inheritance 

Last Update : 28/4/2025
