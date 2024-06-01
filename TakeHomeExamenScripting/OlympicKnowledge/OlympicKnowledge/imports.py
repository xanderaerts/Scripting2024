import requests
import json
from bs4 import BeautifulSoup
import cairosvg
import os
from io import BytesIO
from PIL import Image as PImage

# all import for reportlab
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, ListItem, ListFlowable
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors


# styles for report lab
styles = getSampleStyleSheet()
title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=26, alignment=1)
text_style = ParagraphStyle('BodyText', parent=styles['BodyText'], fontName='Helvetica', fontSize=12, leading=14, alignment=TA_JUSTIFY)
bold_style = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=16, leading=14)
bold_style2 = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=20, leading=14)
error_style = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=16, leading=14,textColor = colors.red)
error_style2 = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=12, leading=14,textColor = colors.red)


def scrape_medailles(pdf):
    url = "https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_water_polo_(men)"
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text,'html.parser')

        table = soup.find("table",{"class":"wikitable plainrowheaders"})

        rows = table.find_all("tr")

        medailles = []

        for row in rows:
            td = row.find_all("td")
            if len(td) != 4: continue # to skip rows with no results
            
            counter = 0 
            # 0 = year of olympics
            # 1 = gold winner
            # 2 = zilver winner
            # 3 = bronze winner

            medaille =  []

            for data in td:
                if counter == 0:
                    a = data.find("a")

                    if(a != None):
                        yearOlympics = a.text
                    else:
                        continue
                
                a = data.find("a")
                if a != None:
                    #if country in a.text.lower():
                        playersRaw = data.find_all("a")
                        players = []
                        for p in playersRaw:
                            if len(p.text) > 3:
                                players.append(p.text)
                        players.insert(0,counter) # insert the counter, so we know later which medialle is won 
                        players.insert(0,yearOlympics)

                        if players[1] != 0:

                            medailles.append(players)

                counter += 1
    else:
        pdf.append(Paragraph("Couldn't download information",error_style))

    return medailles

def scrape_flag(country,pdf):

    flagIMG = "flagimg_" + country + ".png"
    
    if not os.path.isfile(flagIMG):


        url = 'https://countriesnow.space/api/v0.1/countries/flag/images'
        payload = {
                "country": country
        }

        response = requests.post(url, json=payload)


        if response.status_code == 200:
            
            text = response.text

            data = json.loads(text)
            flagURL = data['data']['flag']
            img_path = download_and_save_image(flagURL,flagIMG)

            return img_path
        else:
            return None
    else:

        return flagIMG
        

def download_and_save_image(url, image_filename):
    response = requests.get(url)

    '''if url[:-4] == "svg":
        img_data = cairosvg.svg2png(response.content)
    else:
        img_data = response.content

        
    image = PImage.open(BytesIO(img_data))
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, image_filename)
    
    with open(image_path, 'wb') as f:
        image.save(f)'''

    # Check if the content is an image
    content_type = response.headers.get('content-type', '').lower()
    if 'image' in content_type:
        img_data = response.content
        
        # Save the image based on content type
        if 'svg' in content_type:
            # Convert SVG to PNG
            img_data = cairosvg.svg2png(bytestring=img_data)
            
        # Save other image types with PIL
        image = PImage.open(BytesIO(img_data))
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), image_filename)
        with open(image_path, 'wb') as f:
            image.save(f)
    
    return image_path
