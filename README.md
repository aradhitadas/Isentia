# Isentia 

# Pre-Requisite
Used requests for api call. So python 3 is needed to execute the program. Installed requests module by running - pip install requests

# To run program
1. To generate the csv file, checkout the code & run -- python isentia.py 
2. To run unit test, run -- python test_isentia.py

# Explanation of Code
1. star_wars_characters method:
	1. the response of the get request is received in variable 'response' in text format and then chnaged to dictionary in the variable 'data'.
	2. The information of the starwar character is inside result key so iterating through the 'results', & each of the starwar character details is stored in a dictionary - 'star_chars'.
	3. Now a list is created using the name, height, gender for each one of the starwar character i.e. 'star_chars_list', and then all of the charecters together forms another list - 'star_chars_list_final', which is returned by the method.

2. append_to_file:
	1. A csv file has been created to append the starwar character details. The file is opened in created in currect directory and each row per character is inserted.
	2. The returned list 'star_chars_list_final' from star_wars_characters method is iterated through and all elements of each list inside the star_chars_list_final list is passed to the append_to_file to appeand and created the csv file.
