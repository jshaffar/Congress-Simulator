import csv
import yaml
from datetime import date

FULL_FILE = "Data/full_current_congress.csv"

fnames = ["name", "govtrack_id"]

def getName(person):
    try:
        return person['name']['official_full'].replace('"', '')
    except:
        
        name = ''
        for part in person['name']:
            name = name + person['name'][part] + ' '

        return name.strip().replace('"', '')

def getAge(person):
    birthday = person['bio']['birthday']
    commaed_birthday = birthday.split('-')
    now = date.today().year
    unrounded_age = now - int(commaed_birthday[0])
    unrounded_age = 4
    return unrounded_age




with open(r'congress-legislators/legislators-current.yaml') as file:
    full_file = open(FULL_FILE, 'w')
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    documents = yaml.full_load(file)
    fnames = ["name", "govtrack_id", "gender", "age"]
    writer = csv.DictWriter(full_file, fieldnames = fnames)

    writer.writeheader()

    for person in documents:
        name = getName(person).replace('"', '')
        govtrack_id = person['id']['govtrack']
        gender = person['bio']['gender']
        age = getAge(person)
        writer.writerow({ 'name' : name, 'govtrack_id' : govtrack_id, 'gender' : gender, 'age': age})
  
    
'''
CURRENT_SENATORS_FILE = "People/current_congressmen.csv"
CURRENT_CONGRESSMEN_FILE = "People/current.txt"

with open(r'congress-legislators/legislators-current.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    documents = yaml.full_load(file)

    house_file = open(CURRENT_CONGRESSMEN_FILE, "w")
    senate_file = open(CURRENT_SENATORS_FILE, "w")

    for person in documents:
        if (person['terms'][-1]['type'] == 'rep'):
            try:
                house_file.write(str(person['name']['official_full']) + "\n")
            except:
                name = ""
                for part in person['name']:
                    name = name + person['name'][part] + " "
                name += "\n"
                house_file.write(name)

               
    
        elif (person['terms'][-1]['type'] == 'sen'):
            senate_file.write(str(person['name']['official_full']) + "\n")


    house_file.close()
    senate_file.close()
'''