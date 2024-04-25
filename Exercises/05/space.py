# %% [markdown]
# # Rocket Sience 
# 
# Astronomy is considered one of the most difficult fields of study, hence the phrase 'it's not rocket science'... However, space is a very interesting field, even for children. Therefore, in this assignment, let's make the most difficult aspects of astronomy as accessible as possible for children!
# 
# For this assignment, you will need to create four functions that relate to space education for children. The functions are as follows:
# 
# - explain(text) This function gathers information from https://spaceplace.nasa.gov/glossary/en/ and prints a kidsproof definition for the given term. Print out ''No definition found!' if nothing was found.
# - related(text) This function will print 5 related words to a specific term from https://relatedwords.io. Print out ''No related terms!' if nothing was found.
# - coloring(text) This function will download the first coloring page from https://www.ultracoloringpages.com that relates to the given term. Print out 'Failed to download image!' if nothing was found.
# - book(text) This function will search for the first children's book that has the specific term in its title or description from the list of space books for kids. Print out ''No related terms!' if nothing was found. provided at https://childhood101.com/space-books-for-kids/ and prints its information. Print out ''No book found!' if nothing was found.
# 
# Think very carefully about extra functions, is it necessary to scrape each page every time, or can you scrape certain pages once and store that information in a dictionary or a list? That's why you should provide at least one extra function, but hopefully, you'll create more! This is an exercise in how to make your code better, more structured, but especially less aggressive because don't forget that web scraping is in a gray area.
# 
# Write this all in a script "space.py" that calls the main() function from an if __name__ == "__main__": block!
# 
# Please note that only BeautifulSoup and Requests are the allowable external packages for this assignment, which are already accessible in Codegrade.
# 

# %% [markdown]
# # Code 
# ## Imports

# %%
from bs4 import BeautifulSoup
import requests

# %% [markdown]
# ## Functions

# %%
def explain(text):
    url = "https://spaceplace.nasa.gov/glossary/en/"
    
    soup = urlToSoup(url)

    contentDiv = soup.find("div",{"class","content"})
    spaceTerms = contentDiv.findAll("p")
    
    for s in spaceTerms:
        splited = s.text.split(":")
        if text.lower() == splited[0].lower():
            print(splited[1])
            return 0

    print("No definition found!")

def related(text):
    url = "https://relatedwords.io/" + text
    
    soup = urlToSoup(url)

    list = soup.findAll("span",{"class","term"})

    terms = []

    for i in range (0,len(list)):
        terms.append(list[i].text.strip())
        print(list[i].text.strip())
        if i == 4: return 0
    
    print("No related terms!")

def coloring(text):
    url = "https://www.ultracoloringpages.com/s/" + text +"-coloring-pages"
    
    soup = urlToSoup(url)

    content = soup.find("div",{"class","page-thumb"})

    if content != None:
        for img in content.findAll("img"):
            name = img.get('alt').split(" ")[0]
            img_url = img["src"]
            filename = name + ".png"

            with open(filename,"wb") as f:
                resp = requests.get(img_url)
                f.write(resp.content)

        print("Downloaded",filename)
        return 0   
    print("Failed to download image!")

def book(text):
    url = "https://childhood101.com/space-books-for-kids/"
    
    soup = urlToSoup(url)

    content = soup.find_all("tr")

    for c in content:
        splitted = c.text.split(":")
        
        if text.lower() in  c.text.lower():
            title = splitted[0].strip()
            rest = splitted[1].replace("Available", "")
            print(title +":" + rest)
            return 0
    print("No book found!")

def urlToSoup(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text)
    return soup

# %% [markdown]
# ## Main

# %%
def main():
    term = input("Enter a space related term: ")
    term = term.strip().lower()

    explain(term)
    print()
    
    related(term)
    print()
    
    coloring(term)
    print()
    
    book(term)

if __name__ == "__main__":
    main()



