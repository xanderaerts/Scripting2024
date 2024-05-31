from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

styles = getSampleStyleSheet()
title_style = styles['Title']
bold_style = styles['Heading2']
text_style = styles['BodyText']

def Year(year):
    def is_olympic_year(year):
        return (year - 1896) % 4 == 0

    def get_flag_image(country):
        flag_path = f"flagimg_belgium.png"
        return Image(flag_path, 0.5 * inch, 0.3 * inch)

    def scrape_medailles(pdf):
        # Dummy implementation for scraping medals
        return [
            ["1900 Paris", 1, "Mixed team", "Thomas Coe", "Robert Crawshaw", "William Henry"],
            ["1900 Paris", 2, "Belgium", "Jean de Backer", "Victor de Behr", "Henri Cohen"],
            ["1900 Paris", 3, "Mixed team", "Bill Burgess", "Jules Clévenot", "Alphonse Decuyper"]
        ]

    yearsList = []

    if len(year.strip()) == 4:
        yearsList.append(year)
    elif len(year.strip()) > 4:
        parts = year.split("-")
        startyear = int(parts[0])
        while not is_olympic_year(startyear):
            startyear += 1
        endyear = int(parts[1])
        for i in range(startyear, endyear + 4, 4):
            yearsList.append(str(i))

    # Start creating PDF file
    doc = SimpleDocTemplate(year + "_WaterPolo.pdf", pagesize=letter)
    pdf = []

    pdf.append(Paragraph(year + " ' medals in water polo on the Olympic games", title_style))
    pdf.append(Spacer(1, 12))

    medailles = scrape_medailles(pdf)

    titleyear = ""

    for m in medailles:
        yearPlace = m[0]
        currentYear = yearPlace[:4]

        if currentYear in yearsList:
            if m[0] != titleyear:
                titleyear = m[0]
                pdf.append(Paragraph(m[0] + ":", bold_style))

            medal_type = {1: "GOLD MEDAL", 2: "SILVER MEDAL", 3: "BRONZE MEDAL"}[m[1]]
            text = f"{m[2]} : {medal_type}"

            flag_image = get_flag_image(m[2])
            team_paragraph = Paragraph(text, text_style)
            pdf.append(flag_image)
            pdf.append(team_paragraph)

            players = m[3:]
            player_list = ListFlowable(
                [ListItem(Paragraph(player, text_style)) for player in players],
                bulletType='bullet', start='square'
            )
            pdf.append(player_list)

    doc.build(pdf)

# Example call to the function
Year("1900")
