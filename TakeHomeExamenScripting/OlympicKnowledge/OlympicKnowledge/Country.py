from .imports import *

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
        try:
            img = Image(flagIMG,inch,inch)
            pdf.append(img)
            pdf.append(Spacer(1,12))
        except:
            pdf.append(Paragraph("Couldn't download flag",error_style))
            
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
    if(flagIMG):
        os.remove(flagIMG)
