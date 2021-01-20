import yaml

CURRENT_SENATORS_FILE = "People/current_senators.txt"
CURRENT_CONGRESSMEN_FILE = "People/current_congressmen.txt"

with open(r'congress-legislators/legislators-current.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    documents = yaml.full_load(file)

    house_file = open(CURRENT_CONGRESSMEN_FILE, "w")
    senate_file = open(CURRENT_SENATORS_FILE, "w")

    for person in documents:
        if (person['terms'][-1]['type'] == 'rep'):
            try:
                house_file.write(str(person['name']['official_full']) + '\n')
            except:
                name = ""
                for part in person['name']:
                    name = name + person['name'][part] + " "
                name += '\n'
                house_file.write(name)

               
    
        elif (person['terms'][-1]['type'] == 'sen'):
            senate_file.write(str(person['name']['official_full']) + '\n')


    house_file.close()
    senate_file.close()

    
  
