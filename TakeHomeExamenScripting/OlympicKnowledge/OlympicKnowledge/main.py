import requests
import json
from bs4 import BeautifulSoup
from fpdf import FPDF as PDF


def general(): 
    """ Returns a PDF with all info about Water Polo
    
    Parameters: 
        none
    Returns: 
        none
    """

    url = "https://en.wikipedia.org/wiki/Water_polo" 

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser') # html.parser to fix a warning s


    p = soup.find_all("p")
    description = p[1].text

    url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/WaterPolo.JPG"


    response = requests.get(url)
    waterpoloimg = response.content

    imgfile = open("waterpoloimg.jpg","wb")
    imgfile.write(waterpoloimg)
    imgfile.close()


    url = "https://www.topendsports.com/sport/waterpolo/equipment.htm"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')
    ul = soup.find_all("ul")

    equipmentList = []

    for li in ul:
        st = li.find("strong")
        if(st):
            equipmentList.append(li.text)
    


    
    pdf = PDF()
    pdf.add_page()


    pdf.set_font('Arial','B',26)
    pdf.cell(0,10,"Water polo")
    pdf.ln()

    pdf.image("waterpoloimg.jpg",10,35,75,75)


    pdf.set_xy(95,35)
    pdf.set_font('Arial','',12)
    pdf.multi_cell(100,5,description,0,'J')

    pdf.set_xy(10,115)

    for item in equipmentList:
        parts = item.split("—")

        name = parts[0].strip()
        defenition = parts[1].strip()

        pdf.set_font('Arial','B',12)

        pdf.cell(0,10,name,0,0)
        pdf.set_font('Arial','',12)
        pdf.multi_cell(20,10,defenition)
    pdf.ln()

    pdf.output("General_WaterPolo.pdf") 




    


general()