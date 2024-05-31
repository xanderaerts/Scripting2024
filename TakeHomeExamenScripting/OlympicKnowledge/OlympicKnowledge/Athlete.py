from Country import scrape_medailles,scrape_flag
from imports import *
import os

def Athlete(name):

    parts = name.split(" ")

    searchName = ""
    for p in parts:
        p = p.capitalize()
        searchName += p + "_"

    searchName = searchName[:-1]

    # start creating PDF file
    doc = SimpleDocTemplate(searchName +  "_WaterPolo.pdf",pagesize = letter)
    pdf = []

    pdf.append(Paragraph(searchName.replace("_"," "), title_style))
    pdf.append(Spacer(1,12))




    # url = "https://olympics.com/en/athletes/" + searchName -> site to slow :(
    url = 'https://en.wikipedia.org/wiki/' + searchName
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')

        p = soup.find_all("p")
        try:
            description = p[0].text + p[1].text

        except:
            description = p[0]

        
        pdf.append(Paragraph(description,text_style))
        
        infocard = soup.find("table",{"class":"infobox"})


        img = infocard.find("img")
        imgFile = name + ".png"
        try:
            with open(imgFile, "wb") as f:
                response = requests.get(img['src'])
                f.write(response.content)
            
            img = Image(imgFile,inch,inch)
            pdf.append(img)
            pdf.append(Spacer(1,12))
        except:
            os.remove(imgFile)
            pdf.append(Paragraph("Could not find any image.",error_style2))
            
            


        rows = infocard.find_all("tr")

        for row in rows[1:]: # skip first row because we don't want the name twice
            if row.find("td") == None:
                pdf.append(Paragraph(row.text,bold_style2))
                pdf.append(Spacer(1,12))
            else:
                title = row.find("th")
                data = row.find("td")

                div = row.find("div",string = "Medal record")
                lastrow = row

                if div != None:
                    break
            
                if title != None and data != None and div == None:
                    text = f"<strong> {title.text}</strong>: {data.text}"
                    pdf.append(Paragraph(text,text_style))
            
        
        rows = lastrow.find_all("tr")

        if div != None and len(rows) > 0:
            pdf.append(Paragraph(div.text,bold_style2))
            pdf.append(Spacer(1,12))


            for row in rows[3:]:
                if row.find_all("td") == []:
                    pdf.append(Paragraph(row.text,bold_style))
                    pdf.append(Spacer(1,12))
                else:
                    td = row.find_all("td")
                    outer_span = td[0].find('span')
                    inner_span = outer_span.find("span")
                    result = inner_span['title']

                    parts = result.split(" – ")
                    result = parts[0]
                    
                    location = td[1].text

                    text = f"<strong> {result}</strong>: {location}  "
                    pdf.append(Paragraph(text,text_style))
    else:
        pdf.append(Paragraph(f"Could not find the current athlete:{name}",error_style))

    doc.build(pdf)

Athlete("gojko pijetlović")

