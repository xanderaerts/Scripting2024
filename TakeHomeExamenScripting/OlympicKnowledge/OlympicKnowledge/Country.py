from imports import *

import os

def Country(country): 
    """ Generates a PDF with all medalists water polo from a given country.
    
    Parameters: 
        none
    Returns: 
        none
    """
    country = country.lower().strip()
    
    # start creating PDF file
    doc = SimpleDocTemplate(country + "_WaterPolo.pdf",pagesize = letter)
    pdf = []

    pdf.append(Paragraph(country.capitalize() + " medals in water polo on the olympic games", title_style))
    pdf.append(Spacer(1,12))

    flagIMG = scrape_flag(country,pdf)
    if flagIMG != None:
        img = Image(flagIMG,inch,inch)
        pdf.append(img)
        pdf.append(Spacer(1,12))
    else:
        pdf.append(Paragraph("Couldn't download flag",error_style))
   
    medailles = scrape_medailles(pdf)


    for m in medailles:

        if country in m[2].lower().strip():

            m.pop(2)

            year = m[0]
            
            if m[1] == 1:
                text = year + " : " + "GOLD MEDAL"
            elif m[1] == 2:
                text = year + " : " + "SILVER MEDAL"
            elif m[1] == 3:
                text = year + " : " + "BRONZE MEDAL"

            pdf.append(Paragraph(text,bold_style))

            players = m[2:]  # Assuming players are listed from the 3rd element onwards
            player_list = ListFlowable([ListItem(Paragraph(player, text_style)) for player in players],
                                    bulletType='bullet', start='square')
            pdf.append(player_list)

    doc.build(pdf)


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
                        players.insert(0,counter) # change the country to the counter, so we know later which medialle is won 
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

            response = requests.get(flagURL)
            flag = response.content 

            png_data = cairosvg.svg2png(flag)


            FLAGFILE = open(flagIMG,"wb")
            FLAGFILE.write(png_data)
            FLAGFILE.close()

            return flagIMG
        else:
            return None
    else:

        return flagIMG
        



Country("france")