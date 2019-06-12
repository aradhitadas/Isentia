
import json
import requests
import os
import csv
import logging

# Create your tests here.


class ApiHelper:

        def star_wars_characters(self,page_nr):
            # returns a list (or generator)
            # of the name, height, and gender of each
            # Star Wars character
            
            response = requests.get(url = page_nr).text
            
            data = json.loads(response)
            #print(data["results"])
            results = data["results"]
            star_chars_list = []
            star_chars_list_final = []
            for i in results:
                star_chars_list = []
                star_chars = i
                
                star_chars_list.append(star_chars["name"])
                star_chars_list.append(star_chars["height"])
                star_chars_list.append(star_chars["gender"])

                star_chars_list_final.append(star_chars_list)
            

            return(star_chars_list_final)


            

def append_to_file(filepath, name, age, gender):
        # append the 'name', 'height' and 'gender' of each Star Wars
        # character to a text file (or csv) provided by 'filepath'
        
        row = [name,age,gender]

        with open(filepath, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)

        csvFile.close()
        

url = "https://swapi.co/api/people/"
obj = ApiHelper()
star_chars_list_final=obj.star_wars_characters(url)

filepath = os.getcwd() + "/startwar.csv"

row = ["Name","Height","Gender"]

with open(filepath, 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()
        
for item in star_chars_list_final:
    append_to_file(filepath,item[0],item[1],item[2])
    