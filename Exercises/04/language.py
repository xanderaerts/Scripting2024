# %% [markdown]
# # Languages
# 
# In this task, we will connect various APIs to extract as much information as possible from a given text.
# 
# The recommended API for obtaining information about countries is https://restcountries.com/v2
# Links to an external site. (which is completely free, note it's version 2) since it provides the same information as in the examples. You may use any API of your choice for the other tasks (sentiment and language detection), but it is important to choose a Free(mium) version. In addition, you will also need the text files available in CodeGrade, namely stopwords.zip and iso_639_1codes.csv.
# Create at least the following functions:
# 
#     ``` language(text)``` detects and 'returns' the language of the given text.
#     ``` stopwords(text,language) ``` identifies and 'returns' the number of stopwords in the provided text, based on the detected language.
#     ``` countries(language) ``` generates and 'returns' a list that includes all countries where the identified language is spoken.
#     ``` sentiment(text) ```  determines and 'returns' the positive or negative sentiment of the given text.
#     ``` population(country) ``` obtains and 'returns' the population of the specified country.
# 
# Besides these functions, create at least one other helper function.
# Write this all in a script "language.py" that calls the main() function from an ```if __name__ == "__main__": ``` block!
# 
# Important note: You are restricted to only use the following packages for your task: requests, re, csv, os, json and string. You are not allowed to install additional packages.
# 
# 
# ### Example usage:
# 
# ```
# $ python3 script.py 
# 
# Enter text: Me siento muy afortunado y feliz hoy porque el sol está brillando y las flores están en flor.
# 
# The dedected language is Spanish
# 10 stopwords found
# The text is positive
# The majority of people who speak Spanish live in Mexico
# 
# 
# Enter text: Ik ben echt ontzettend teleurgesteld en boos met de slechte kwaliteit die ik heb ontvangen van de klantenservice!
# 
# The dedected language is Dutch
# 10 stopwords found
# The text is negativ`
# The majority of people who speak Dutch live in Netherlands
# ```
# 
# 
# 

# %% [markdown]
# # Code
# ## Imports

# %%
import requests
import re
import csv
import os
import json
import string

# %% [markdown]
# ## Functions

# %%
def language(text):
    

    try:
        url = "https://text-analysis12.p.rapidapi.com/language-detection/api/v1.1"

        payload = { "text": text }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        lang = response.json()

        for k in lang['language_probability']:
            return getLangFullName(k)
    except:
        print("Something went wrong with the language detection!")
        exit()

def getLangFullName(shortversion):

    if len(shortversion) > 2:
        return shortversion

    FILE = open("iso_639_1codes.csv")
    csvfile = csv.reader(FILE,delimiter=",")

    for line in csvfile:
        if shortversion in line[0]:
            return line[1]

def getLangShort(longversion):

    if len(longversion) == 2:
        return longversion

    FILE = open("iso_639_1codes.csv")
    csvfile = csv.reader(FILE,delimiter=",")

    for line in csvfile:
        if longversion == line[1]:
            return line[0]

        
def stopwords(text,language):

    counter = 0


    languageFull = getLangFullName(language)
    try:
        File = open(languageFull.lower() + ".txt","r")

        stopwords = File.read().splitlines()
        
        text = text.lower()
        words = text.split(" ")

        for w in words:
            if w in stopwords:
                counter += 1      
        return counter

    except:
        return 0


def sentiment(text):
    url = "https://sentiment-analysis9.p.rapidapi.com/sentiment"

    payload = [
        {
            "id": "1",
            "language": "en",
            "text": translate(text)
        }
    ]
    headers = {
        "content-type": "application/json",
        "Accept": "application/json",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "sentiment-analysis9.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    pred = data[0]['predictions']
    return pred[0]['prediction']
    

# work arnound to use this api, could't find any better api's 
def translate(text):
    url = "https://text-translator2.p.rapidapi.com/translate"

    short = getLangShort(language(text))

    if(short == "en"):
        return text
    
    payload = {
        "source_language": short,
        "target_language": "en",
        "text": text
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key":"" ,
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    data = response.json()

    return data['data']['translatedText']

def countries(lang):

    if(len(lang) > 2):
        url = "https://restcountries.com/v3.1/lang/" + lang
    elif len(lang) == 2:
        url = "https://restcountries.com/v3.1/lang/" + getLangFullName(lang)
    
    response = requests.get(url)

    data = response.json()

    country_names = []

    for country in data:
        country_name = country['name']['common']
        country_names.append(country_name)


    country_names.sort()



    return country_names

def population(country):
    url = "https://restcountries.com/v3.1/name/" + country + "?fields=population"

    response = requests.get(url)

    data = response.json()

    sum = 0

    for pop in data:
       # print(pop)
        sum += pop['population']
        
   # print(sum)
    return sum

def majority(lang):
    countriesSpoken = countries(lang)

    most = 0
    mostCountrie = ""

    for c in countriesSpoken:
        pop = population(c)

        if pop > most:
            most = pop
            mostCountrie = c

    return mostCountrie

# %% [markdown]
# ## Main

# %%
def main():
    text = input("Enter text: ")
    langShort = language(text)
    print("The detected language is", getLangFullName(langShort))
    print(stopwords(text,langShort), "stopwords found")
    print("The text is",sentiment(text))
    print("The majority of people who speak",getLangFullName(langShort),"live in",majority(langShort))
    
if __name__ == "__main__":
    main()


