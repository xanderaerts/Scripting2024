# %% [markdown]
# # Birthday
# 
# Elke had her birthday last weekend #hooray and that was the inspiration for a whole exercise about dates! You read a birthdate and find out what the zodiac sign is, the age, the radio hit, which historical events took place on that one day of the month, what percentage of people were also born on that day, and so on... and let's face it, how fun is it to gather all that information about your own birthday?
# 
# In this exercise, you will work with files and an API, and you will also do some web scraping... all of this using a single or multi-threaded approach!
# For this assignment, you will need to create six functions as follows:
# - zodiac(day, month) prints the right zodiac sign based on a day and a month
# - percentage(day, month) finds the percentage (rounded by 2 digits) of people born on the same day. You use for this task the file data.csv (file already in CC) which contains records of daily births from 2000 to 2014, including the year, month, day of the month, day of the week, number of births, and date in the format of month/day/year. Since we have data from 14 years, we can say that we have reasonably good information. And the good news: you are allowed to use pandas!
# - historical(day, month) prints a list of 10 historical events that took place on that day of the month, use the API https://api-ninjas.com/api/historicalevents for this task! one(day, month, year) prints the number one hit in the US! Scrape the information from this website https://www.onthisday.com/ (ex: on my birthdate asked Blondie to Call her ;) https://www.onthisday.com/date/1980/april/23)
# wikipedia(day, month) creates a file of all famous birthdays scraped from Wikipedia (hint: take a good look at the url, days are always formatted like this). The function prints out the name of the file created (ex: https://en.wikipedia.org/wiki/April_23 --> April_23.txt
# - age(day, month, year) prints the age (easy ;))
# 
# You must be able to read in different date formats (eg: "04/23/1980", "1980/04/23", "Apr 23, 1980" etc...), and once they are correctly formatted, you will also determine whether the functions should be executed in a single or multi-threaded manner. Don't panic if the order of execution differs (which may happen), and that's why in the multithreading tests in CC, only partial output is verified. <br>
# 
# Write this all in a script "birthday.py" that calls the main() function from an ```if __name__ == "__main__"``` block!
# Note you are allowed to use the external packages pandas, beautifulsoup, requests and dateutil (and also take a close look at the built-in module calendar)!
# 

# %% [markdown]
# # Code
# ## Functions

# %%
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from dateutil.relativedelta import relativedelta
from dateutil import parser
import datetime

# %%
def zodiac(day,month):
    day = int(day)
    month = int(month)
    
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Invalid input"


def age(day, month, year):
    birthdate = day + month + year
    birthdate = datetime.datetime.strptime(birthdate, '%d%m%Y').date()
    today = datetime.date.today()
    age = relativedelta(today, birthdate).years
    return age

def percentage(day,month):
    bdays = pd.read_csv("data.csv") 

    totBirths= bdays[(bdays['month'] == int(month)) & (bdays['date_of_month'] == int(day))]['births'].sum()

    totDays = bdays[(bdays['month'] == int(month)) & (bdays['date_of_month'] == int(day))]['births'].count()

    totSum = bdays['births'].sum()

    if totDays > 0:
        percentage = (totBirths / totSum) * 100
    else:
        percentage = 0

    return percentage

def historical(day,month):
    api_url = "https://api.api-ninjas.com/v1/historicalevents?month=" + str(month) + "&day="+str(day)
    response = requests.get(api_url, headers={'X-Api-Key': ''})

    data = response.text

    events = json.loads(data)

    print("Historical events:")
    for event in events:
        print(f"{event['year']} - {event['event']}")

def one(day,month,year):
    url = "https://www.onthisday.com/date/"+ str(year) + "/"+ monthToString(month) + "/"+ str(day)

    soup = urlToSoup(url)

    list = soup.findAll("li",{"class","event"})

    last = list[len(list) - 1]

    song_artist_info = last.text.split(" - ")
    song = song_artist_info[0].replace("#1 Song:", "").strip()
    artist = song_artist_info[1].strip()

    print("Number one hit: " +song + " - " + artist)


def wikipedia(day,month):
    searchtag = "mw-content-ltr mw-parser-output"

    OUTFILE = monthToString(month) + "_" + str(day) + ".txt"
    url = "https://en.wikipedia.org/wiki/" + monthToString(month) + "_" + str(day)
    soup = urlToSoup(url)

    births_h2 = soup.find('span', string='Births')
    
    current_element = births_h2.find_next()

    running = True

    list = []

    while running:
        if current_element.name == "li":
            list.append(current_element)
            
        if current_element.name == "span" and current_element.string == "Deaths":
            running = False
            break
        current_element = current_element.find_next()

    with open(OUTFILE, "w") as file:
        for item in list:
            file.write(str(item))
            file.write("\n")
    print("File saved as",OUTFILE)

def monthToString(month):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return months[int(month) - 1]

def format_date(date):

    output_format =  "%d %m %Y"
   
    try:
        parsed_date = parser.parse(date)
        formatted_date = parsed_date.strftime(output_format)
        return formatted_date
    except:
        return "Invalid date format"
    

def urlToSoup(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)
    return soup


# %% [markdown]
# ## Main

# %%
def main():
    date = input("Give a date.")

    formattedDate = format_date(date)


    day,month,year = formattedDate.split(" ")

    zodiac(day,month)
    age(day,month,year)
    percentage(day,month)
    historical(day,month)
    wikipedia(day,month)

    

if __name__ == "__main__":
    main()


