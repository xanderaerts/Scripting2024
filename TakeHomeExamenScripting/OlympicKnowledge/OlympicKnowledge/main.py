import requests
import json
from bs4 import BeautifulSoup



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

    td = soup.find_all("img",{"class":"mw-file-element"})

    print(td.source)

    for img in td.find("img"):
        img_url = img["src"]
        filename = "waterpoloimg.jpg"

        with open(filename,"wb") as f:
            response = requests.get(img_url)
            f.write(response.content)

    print(description) 


    OUTFILE = open("outfile.pdf","w")

    OUTFILE.write(description)

    OUTFILE.close()





    


general()