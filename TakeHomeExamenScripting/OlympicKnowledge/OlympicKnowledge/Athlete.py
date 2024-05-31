from Country import scrape_medailles,scrape_flag
from imports import *

def Athlete(name):


    #build up the url to scrape 

    parts = name.split(" ")

    searchName = ""

    for p in parts:
        searchName += p + "-"

    searchName = searchName[:-1].lower()

    print(name)
    url = "https://olympics.com/en/athletes/" + searchName
    
    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')

    soup.find("div",{"class":"sc-dkdfbS dOqNtC"})

    print(soup)



    # start creating PDF file
    doc = SimpleDocTemplate(name +  "_WaterPolo.pdf",pagesize = letter)
    pdf = []

    pdf.append(Paragraph(name, title_style))
    pdf.append(Spacer(1,12))





    
    #doc.build(pdf)

Athlete("Gojko Pijetlović")
