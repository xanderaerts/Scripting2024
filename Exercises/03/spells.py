# %% [markdown]
# # Spells & potions
# 
# In this task, we explore the world of Harry Potter's spells and potions. You should download the zip file HarryPotter.zip
# Download HarryPotter.zip, which contains various files: characters, potions, spells, and the first three books. In your code, you should be able to unzip the entire file and start from there.
# 
# The goal is to search for the characters who use a specific spell or potion based on a book, spell, or potion.
# 
# Create the following functions:
# 
#    ``` mentions(book, text) ``` this function searches for the number of times a specific spell or potion appears in a book. It prints the count and also returns a dictionary of the character who used it and a list of line numbers. <br>
#    ```character(name)``` this function prints the full name, house, and age of today or at the time of their death. <br>
#    ``` calculate_age(birth,death='') ``` this helper function calculates a person's age based on their date of birth and date of death (if found). If the dates are not given in the format 'dd month yyyy' (sometimes with a comma before the year), the age cannot be calculated. <br>
#    
#    ``` spell(text) ``` this function searches for a specific spell and returns an overview of its characteristics as key-value pairs. <br>
#    ``` potion(text) ``` this function searches for a specific potion and returns an overview of its characteristics as key-value pairs. <br>
#    <br>
# Write this all in a script "spells.py" that should call the main() function from an ``` if __name__ == "__main__": ```block!
# 
# 
# 
# ### Example usage:
# 
# ```
# $ python3 script.py 
# 
# Enter book: 1
# Enter spell/potion: Alohomora
# 
# 4 apperances of Alohomora in book Harry Potter 1.csv
# 
# Hermione on line(s) 724, 1337
# Hermione Jean Granger
# Gryffindor
# Hermione is today 43 years old.
# 
# Ron on line(s) 726, 1396 
# Ronald Bilius Weasley Gryffindor 
# Ron is today 43 years old.  
# 
# SPELL Alohomora 
# Name: Unlocking Charm 
# Incantation: Alohomora 
# Type: Charm 
# Effect: Unlocks target
# Light: Invisible, blue, yellow, or purple
# ```

# %% [markdown]
# # Code
# 
# ### Imports

# %%
import os
import pathlib
import zipfile
import csv
from datetime import datetime

# %% [markdown]
# ### Functions

# %%
def unzip():
    zipbestand = zipfile.ZipFile("HarryPotter.zip","r")
    zipbestand.extractall()
    zipbestand.close()

def mentions(book, text):
    if "Harry Potter" in book:
        FILE =  open(book,"r")
    else:
        book = "Harry Potter " + book + ".csv"
        FILE = open(book,"r")

    csvfile = csv.reader(FILE,delimiter=";")
    
    linenumber = 0
    chars = {}
    counter = 0
    
    for line in csvfile:
        linenumber += 1
        
            

        if len(line) > 1 and text in line[1]:   

            counter += 1        

            namestripped = line[0].strip()

            if(namestripped in chars.keys()):
                chars[namestripped].append(str(linenumber))
            else:
                chars[namestripped] = [str(linenumber)]

    print(counter, "apperances of",text,"in book",book+"\n")
    return chars
    


def calculate_age(birth, death = ''):
    now = datetime.now()

    try:
        birth = birth.replace(",", "")
        birth_date = datetime.strptime(birth, "%d %B %Y")

        if not death:
            age = now.year - birth_date.year - ((now.month, now.day) < (birth_date.month, birth_date.day))
           # if (now.month, now.day) >= (birth_date.month, birth_date.day):
           #     age += 1
            return age
        
        if death:
            death = death.replace(",", "")
            death_date = datetime.strptime(death, "%d %B %Y")
            age = death_date.year - birth_date.year - ((death_date.month, death_date.day) < (birth_date.month, birth_date.day))
            return age
        
    except:
        if death:
            return -1
        else:
            return 1


def character(name):

    FILE = open("Characters.csv","r")
    csvfile = csv.reader(FILE,delimiter=";")
    
    charDict = {}
    for line in csvfile:
        if name in line[1]:
            charDict = {
                "name": line[1],
                "house": line[4],
                "age": calculate_age(line[13],line[14].strip()),
                "mentions": []
            }

        if(charDict != {}):

            print(charDict["name"])
            print(charDict["house"])


            if(charDict["age"] == 1):
                print(name,"is alive and kicking\n")
            elif(charDict["age"] == -1):
                print(name,"died\n")

            elif line[14].strip() == '':
                print(name,"is today",charDict["age"],"years old.\n")
            else:
                print(name,"died at age",charDict["age"],"\n")
            return charDict

def spell(text):
    FILE = open("Spells.csv","r")

    csvfile = csv.reader(FILE,delimiter=";")

    spell = {}

    for line in csvfile:
        if text in line:
            spell['Name'] = line[0]
            spell['Incantation'] = line[1]
            spell['Type'] = line[2]
            spell['Effect'] = line[3]
            spell['Light'] = line[4]
            return spell
    for key, value in spell.items():
        print(f"{key}: {value}")
    return spell

def potion(text):
    FILE = open("Spells.csv","r")

    csvfile = csv.reader(FILE,delimiter=";")

    potion = {}

    for line in csvfile:
        if text in line:
            potion['Name'] = line[0]
            potion['Known ingredients'] = line[1]
            potion['Effect'] = line[2]
            potion['Characteristics'] = line[3]
            potion['Difficulty level'] = line[4]
            
    
    for key, value in potion.items():
        print(f"{key}: {value}")
    return potion

# %% [markdown]
# ### Main

# %%
if __name__ == "__main__":
    book = input("Enter book: ")
    text = input("Enter spell/potion")

    unzip()
    chars = mentions(book,text)

    for char in chars.keys():
        print(char,"on line(s)",",".join(chars[char]))
        character(char)



    spellInfo = spell(text)
    potionInfo = potion(text)

    
    


