from .imports import *

def General(): 
    """ Returns a PDF with all info about Water Polo
    
    Parameters: 
        none
    Returns: 
        none
    """

    doc = SimpleDocTemplate("General_WaterPolo.pdf",pagesize = letter)

    pdf = []

    pdf.append(Paragraph("Water polo", title_style))
    pdf.append(Spacer(1,12))

    url = "https://en.wikipedia.org/wiki/Water_polo" 

    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser') # html.parser to fix a warning

    p = soup.find_all("p")
    description = p[1].text

    url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/WaterPolo.JPG"


    response = requests.get(url)

    if response.status_code == 200:
        
        WPimg = "waterpoloGeneralIMG.jpg"

        img_path = download_and_save_image(url,WPimg)

        img = Image(img_path,3*inch,3*inch)
        pdf.append(img)
        pdf.append(Spacer(1,12))
    else:
        pdf.append(Paragraph("Could not load image",error_style))    

    url = "https://www.topendsports.com/sport/waterpolo/equipment.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')
    ul_elements = soup.find_all("ul")

    equipmentList = []

    for ul in ul_elements:
        li_elements = ul.find_all('li')

        for li in li_elements:
            if li.find('strong'):
                equipmentList.append(li)



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
    if(WPimg):
        os.remove(img_path)