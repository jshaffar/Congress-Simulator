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
    age = now - int(commaed_birthday[0])
    if date.today().month > int(commaed_birthday[1]) and date.today().day > int(commaed_birthday[2]):
        age -= 1

    return age

def getParty(person):
    return person['terms'][-1]['party']

def getRank(person):
    try:
        return person['terms'][-1]['state_rank']
    except:
        #print("rep has no rank")
        return ""


def getDistrict(person):
    district = person['terms'][-1]['state']
    if (person['terms'][-1]['type'] == 'rep'):
        district += " " + str(person['terms'][-1]['district'])      
    return district 
        

def getJob(person):
    return person['terms'][-1]['type']

with open(r'congress-legislators/legislators-current.yaml') as file:
    full_file = open(FULL_FILE, 'w')
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    documents = yaml.full_load(file)
    fnames = ["name", "govtrack_id", "job", "gender", "age", "party", "rank", "district"]
    writer = csv.DictWriter(full_file, fieldnames = fnames)

    writer.writeheader()

    for person in documents:
        name = getName(person).replace('"', '')
        govtrack_id = person['id']['govtrack']
        job = getJob(person)
        gender = person['bio']['gender']
        age = getAge(person)
        party = getParty(person)
        rank = getRank(person)
        district = getDistrict(person)
        
        writer.writerow({ 'name' : name, 'govtrack_id' : govtrack_id, 'job' : job, 'gender' : gender, 'age': age, 'party':party, 'rank': rank, 'district' : district})