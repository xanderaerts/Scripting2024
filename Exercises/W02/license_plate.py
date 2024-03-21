# %% [markdown]
# # License plate
# 
# 
# 
# For this task, you create a script called "license_plate.py" that checks the validity of a Belgian license plate. Once the user inputs a license plate, the script needs to verify its validity. If the license plate is valid, the user will be prompted to select a format to display the license plate in. The available formats are the NATO alphabet, Morse code or ASCII art
# Special license plates:
# 
#     1-9: vehicle from king and/or queen (output kind and queen)
#     10-99: vehicles from other royal family members (output royal)
#     A-1 → A-999: official (vehicles)
#     CD-AA111 → CD-ZZ999: diplomat (vehicles)
#     G-LAA-111 → G-LZZ-999: agriculture  (vehicles)
#     M-AAA-000 → M-ZZZ-999: motorcycle(s)
#     O-AAA-111 → O-ZZZ-999: oldtimer(s)
#     Q-AAA-000 → Q-ZZZ-999: trailer(s)
#     T-XAA-000 → T-XZZ-999: taxi(s)
#     Y-AAA-000 → Y-ZZZ-999: test (drives)
# 
# Standard license plates are categorized according to the corresponding years
# 
#     1962-1971: AA.001 → ZZ.999
#     1971-1973: A.001.A → Z.999.Z
#     1973-2008: AAA-001 → ZZZ-999
#     2008-2010: 001-AAA → 999-CFQ
#     2010-now: 1-AAA-001 → 7-ZZZ-999
# 
# Also, take into account a list of forbidden letter combinations.
# AAP AAS AEL ALA ANE ASS BEB BIT BOM BOY BSP BUB BWP BYT CAP CDF CDH CDV CON CSP CUB CUL CUT CVP DCD DIK DOM FDF FOK FOL FOU FUC FUK GAT GAY GEK GOD HIV HOL JEK KAK KKQ KUL KUT LAF LDD LSP LUL MAS MCC MDP MOR MOU MST NIC NIK NIQ NVA PDB PDO PET PFF PIK PIN PIP PIS PJU PKK POT PRL PSB PSC PSL PTB PUE PUT PVV PYK PYN PYP PYS ROM SEX SOA SOT SPA SUL TAK TET TIT TUE VCD VIH VLD VMO VNV ZAC ZAK ZOT
# Create (at least) these functions:
# 
# ```forbidden(plate)```which returns a boolean True if the plate holds a forbidden letter combination and False if not <br>
# ```check(plate)``` which can return the following strings:
#         - invalid plate
#         - forbidden plate - <forbidden combination>
#         - standard plate - <year range>
#         - special plate - <special category> <br>
# ```nato(plate)``` which returns the plate (without nonalphabetical characters) in NATO phonetic alphabet <br>
# ```main()``` which calls all functions as needed <br>
# 
# Write this all in a script that should call the main() function from an ```if __name__ == "__main__":``` block!
# 
# Important: you are only allowed to use 2 out of the 3 suggested packages (so you will have to code at least one function yourself) and you are not allowed to install any additional packages!
# If you do use all 3 packages or any others, your grade will be deduced!
# 
# ```
# Enter license plate: Y.456.T
# standard plate - 1971-1973
# Enter format: morse
# -.-- ....- ..... -.... - 
# 
# 
# Enter license plate: CD-AT654
# special plate - diplomat
# Enter format: blabla
# Wrong format!
# 
# 
# Enter license plate: G-UIO-100
# standard plate - 1973-2008
# Enter format: ascii
#   ____         _   _  ___   ___          _   ___    ___  
#  / ___|       | | | ||_ _| / _ \        / | / _ \  / _ \ 
# | |  _  _____ | | | | | | | | | | _____ | || | | || | | |
# | |_| ||_____|| |_| | | | | |_| ||_____|| || |_| || |_| |
#  \____|        \___/ |___| \___/        |_| \___/  \___/ 
# 
# Enter license plate: 6
# special plate - king and queen
# Enter format: nato
# SIX 
# 
# ```
# 

# %%
import re
from art import *
import phonetic_alphabet as alpha

# %%
def forbidden(plate):
    forbidden_combinations = [ "AAP", "AAS", "AEL", "ALA", "ANE", "ASS", "BEB", "BIT", "BOM", "BOY",
    "BSP", "BUB", "BWP", "BYT", "CAP", "CDF", "CDH", "CDV", "CON", "CSP",
    "CUB", "CUL", "CUT", "CVP", "DCD", "DIK", "DOM", "FDF", "FOK", "FOL",
    "FOU", "FUC", "FUK", "GAT", "GAY", "GEK", "GOD", "HIV", "HOL", "JEK",
    "KAK", "KKQ", "KUL", "KUT", "LAF", "LDD", "LSP", "LUL", "MAS", "MCC",
    "MDP", "MOR", "MOU", "MST", "NIC", "NIK", "NIQ", "NVA", "PDB", "PDO",
    "PET", "PFF", "PIK", "PIN", "PIP", "PIS", "PJU", "PKK", "POT", "PRL",
    "PSB", "PSC", "PSL", "PTB", "PUE", "PUT", "PVV", "PYK", "PYN", "PYP",
    "PYS", "ROM", "SEX", "SOA", "SOT", "SPA", "SUL", "TAK", "TET", "TIT",
    "TUE", "VCD", "VIH", "VLD", "VMO", "VNV", "ZAC", "ZAK", "ZOT" ]

    regex = r"[A-Z]{3}"

    list = re.findall(regex,plate)

    if len(list > 0):
        if list[0] in forbidden_combinations:
            return True 

    return False


# %%
def check(plate):
    output = ""

    if forbidden(plate) == True:

        regex = r"[A-Z]{3}"
        list = re.findall(regex,plate)

        return "forbidden plate " + list[0]

    plate_parts = plate.split("-")


    
    if len(plate_parts) == 1:

        try:
            plate_number = int(plate_parts[0])
            
            output += "special plate"

            if plate_number <= 9 and plate_number > 0:
                output += " - king and queen"

            elif plate_number > 10 and plate_number < 99:
                output += " royal"

            return output
        
        except: 
            plate_parts = plate.split(".")

            if len(plate_parts) == 2: 

                output += "standard plate"

                regex = r"[A-Z]{2}\.[0-9]{3}"

                if re.match(regex,plate) is None:
                    return "invalid plate"
                else:
                    return output + " - " + "1962-1971" 

            elif len(plate_parts) == 3:
                output += "standard plate"

                regex = r"[A-Z]\.[0-9]{3}\.[A-Z]"

                if re.match(regex,plate) is None:
                    return "invalid plate"
                else:
                    return output + " - " + "1971-1973"
           
    elif len(plate_parts) == 2:

        output += "special plate"

        if plate_parts[0] == "A" and int(plate_parts[1]) > 0:
            return output + " - "  +"official"
        
        regex = r"CD-[A-Z]{2}[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "diplomat"
        
        output = "standard plate"
        
        regex = r"[A-Z]{3}-[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "1973-2008"
        
        regex = r"[1-9]{3}-[A-Z]{3}"
        if re.match(regex,plate):
            return output + " - " + "2008-2010"
        
    elif len(plate_parts) == 3:

        output += "special plate"

        regex = r"G-L[A-Z]{2}-[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "agriculture"

        regex = r"M-[A-Z]{3}-[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "motorcycle"
        
        regex = r"O-[A-Z]{3}-[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "oldtimer"
        
        regex = r"Q-[A-Z]{3}-[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "trailer"
        
        regex = r"T-X[A-Z]{2}-[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "taxi"

        regex = r"Y-[A-Z]{3}-[1-9]{3}"
        if re.match(regex,plate):
            return output + " - " + "test"

        regex = r"[1-9]-[A-Z]{3}-[1-9]{3}"
        if re.match(regex,plate):
            return "standard plate - 2010-now"

    return "invalid plate"

# %%
def nato(plate):
    print(plate)

# %%
def ascii(plate):
    tprint(plate)

# %%
def nato(plate):
    print(alpha.read(plate))

# %%
def morse(plate):
    s = ""
    for c in plate: 
        match c: 
            case 'A': s += ". _ "
            case 'B': s += "_ . . "
            case 'C': s += "_ . _ . "
            case 'D': s += "_ . . "
            case 'E': s += ". "
            case 'F': s += ". . _ . "
            case 'G': s += "_ _ . "
            case 'H': s += ". . . . "
            case 'I': s += ". . "
            case 'J': s += ". _ _ _ "
            case 'K': s += "_ . _ "
            case 'L': s += ". _ . . "
            case 'M': s += "_ _ "
            case 'N': s += "_ . "
            case 'O': s += "_ _ _ "
            case 'P': s += ". _ _ . "
            case 'Q': s += "_ _ . _ "
            case 'R': s += ". _ . "
            case 'S': s += ". . . "
            case 'T': s += "_ "
            case 'U': s += ". . _ "
            case 'V': s += ". . . _ "
            case 'W': s += ". _ _ "
            case 'X': s += "_ . . _ "
            case 'Y': s += "_ . _ _ "
            case 'Z': s += "_ _ . . "
            case '1': s += ". _ _ _ _ "
            case '2': s += ". . _ _ _ "
            case '3': s += ". . . _ _ "
            case '4': s += ". . . . _ "
            case '5': s += ". . . . . "
            case '6': s += "_ . . . . "
            case '7': s += "_ _ . . . "
            case '8': s += "_ _ _ . . "
            case '9': s += "_ _ _ _ . "
            case '-' | '.': s+= " "
    print(s)


# %%
if __name__ == "__main__":
    plate = input("Enter license plate: ")
    print(check(plate))

    format = input("Enter format: ")
    
    if format == "ascii":
        ascii(plate)
    elif format == "nato":
        nato(plate)
    elif format == "morse":
        morse(plate)
    else:
        print("Wrong format!")



