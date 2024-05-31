from Country import scrape_medailles,scrape_flag
from imports import *

def Year(year):

    yearsList = []

    if len(year.strip()) == 4:
        yearsList.append(year)

    elif len(year.strip()) > 4:
        parts = year.split("-")

        startyear = int(parts[0])

        while not is_olympic_year(startyear):
            startyear += 1


        endyear = int(parts[1])

        for i in range(startyear,endyear+4,4):
            yearsList.append(str(i))
        
    # start creating PDF file
    doc = SimpleDocTemplate(year +  "_WaterPolo.pdf",pagesize = letter)
    pdf = []

    pdf.append(Paragraph(year + " medals in water polo on the olympic games", title_style))
    pdf.append(Spacer(1,12))




    medailles = scrape_medailles(pdf)

    titleyear = ""

    for m in medailles:
        yearPlace = m[0]
        currentYear = yearPlace[:4]

        if currentYear in yearsList:
            if m[0] != titleyear:
                titleyear = m[0]
                pdf.append(Paragraph(m[0] + ":",bold_style2))
            

            if m[1] == 1:
                text = m[2] + " : " + "GOLD MEDAL"
            elif m[1] == 2:
                text = m[2] + " : " + "SILVER MEDAL"
            elif m[1] == 3:
                text = m[2] + " : " + "BRONZE MEDAL"
                

            flagIMG =  scrape_flag(m[2],pdf)
            if flagIMG != None:
                img = Image(flagIMG,inch/2,inch/2)
                pdf.append(img)

            pdf.append(Paragraph(text,bold_style))

            players = m[3:]
            player_list = ListFlowable([ListItem(Paragraph(player, text_style)) for player in players],
                                    bulletType='bullet', start='square')
            pdf.append(player_list)
    
    doc.build(pdf)











def is_olympic_year(year):
    exceptions = {1916, 1940, 1944}
    if year >= 1896 and (year - 1896) % 4 == 0 and year not in exceptions:
        return True
    return False

Year("2000-2020")