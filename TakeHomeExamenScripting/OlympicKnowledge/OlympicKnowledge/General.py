from imports import *

def General(): 
    """ Returns a PDF with all info about Water Polo
    
    Parameters: 
        none
    Returns: 
        none
    """

    url = "https://en.wikipedia.org/wiki/Water_polo" 

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser') # html.parser to fix a warning


    p = soup.find_all("p")
    description = p[1].text

    url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/WaterPolo.JPG"

    response = requests.get(url)
    waterpoloimg = response.content

    WPimg = "waterpoloGeneralIMG.jpg"

    imgfile = open(WPimg,"wb")
    imgfile.write(waterpoloimg)
    imgfile.close()

    url = "https://www.topendsports.com/sport/waterpolo/equipment.htm"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')
    ul_elements = soup.find_all("ul")

    equipmentList = []

    for ul in ul_elements:
        li_elements = ul.find_all('li')

        for li in li_elements:
            if li.find('strong'):
                equipmentList.append(li)

    # start creating PDF file
    doc = SimpleDocTemplate("General_WaterPolo.pdf",pagesize = letter)

    pdf = []

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=26, alignment=1)
    text_style = ParagraphStyle('BodyText', parent=styles['BodyText'], fontName='Helvetica', fontSize=12, leading=14, alignment=TA_JUSTIFY)
    bold_style = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=16, leading=14)

    pdf.append(Paragraph("Water polo", title_style))
    pdf.append(Spacer(1,12))

    img = Image(WPimg,3*inch,3*inch)
    pdf.append(img)
    pdf.append(Spacer(1,12))

    pdf.append(Paragraph(description,text_style))
    pdf.append(Spacer(1,12))

    pdf.append(Paragraph("Equipment:",bold_style))
    pdf.append(Spacer(1,12))


    for item in equipmentList:
        item = item.text
        parts = item.split(" — ")
        name = parts[0].strip()
        definition = parts[1].strip()

        pdf.append(Paragraph(f'<b>{name}</b> - {definition}', text_style))
        pdf.append(Spacer(1, 12))

    doc.build(pdf)
   


General()