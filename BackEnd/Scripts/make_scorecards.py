import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

FILE_NAME = "Playground/file_corrected.csv"
CURRENT_CONGRESS_FILE_NAME = "Data/full_current_congress.csv"


def text_to_score(full_text, subtext):
    if full_text == "" or subtext not in full_text:
        return ""
    index = full_text.find(subtext + ":") + len(subtext)
    
    end_index = 0
    if full_text[index + 2].isdigit():
        end_index = full_text.find('%', index)
    else:
        end_index = index + 3
    num = full_text[index + 2 : end_index]
    return num

def write_scorecard_one_member(govtrack_id, name, writer, file):

    URL = 'https://www.govtrack.us/congress/members/' + str(govtrack_id)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    dA = soup.text
    results = soup.find(id='model-body')
    scorecard = soup.find(id="scorecards")

    score_text = ""
    if scorecard != None:
        score_text = scorecard.text

    human_rights_conservation = text_to_score(score_text, "Human Rights Campaign")
    league_of_conservation_voters = text_to_score(score_text, "League of Conservation Voters")
    planned_parenthood_action_fund = text_to_score(score_text, "Planned Parenthood Action Fund")
    niac_action = text_to_score(score_text, "NIAC Action")
    american_civil_liberties_union = text_to_score(score_text, "American Civil Liberties Union")
    unted_states_chamber_of_commerce = text_to_score(score_text, "United States Chamber of Commerce")
    numbers_usa = text_to_score(score_text, "NumbersUSA")
    the_national_organization_for_the_reform_of_marajuana_laws = text_to_score(score_text, "The National Organization for the Reform of Marijuana Laws")
    americans_for_prosperity = text_to_score(score_text, "Americans for Prosperity")
    the_club_for_growth = text_to_score(score_text, "The Club for Growth")
    freedomworks = text_to_score(score_text, "FreedomWorks")
    
    writer.writerow({"name" : name, "govtrack_id" : govtrack_id, "human_rights_conservation" : human_rights_conservation, "league_of_conservative_voters" : league_of_conservation_voters, "planned_parenthood_action_fund" :planned_parenthood_action_fund,
        "niac_action" : niac_action, "american_civil_liberties_union" : american_civil_liberties_union, "unted_states_chamber_of_commerce" : unted_states_chamber_of_commerce, "numbers_usa" : numbers_usa,"the_national_organization_for_the_reform_of_marajuana_laws" : the_national_organization_for_the_reform_of_marajuana_laws,
            "americans_for_prosperity" : americans_for_prosperity, "the_club_for_growth" : the_club_for_growth, "freedomworks" : freedomworks})

def write_scorecard_entire_congress():
    df = pd.read_csv(CURRENT_CONGRESS_FILE_NAME)
    fnames = ["name", "govtrack_id", "human_rights_conservation", "league_of_conservative_voters", "planned_parenthood_action_fund",
        "niac_action", "american_civil_liberties_union", "unted_states_chamber_of_commerce", "numbers_usa","the_national_organization_for_the_reform_of_marajuana_laws"
            ,"americans_for_prosperity", "the_club_for_growth", "freedomworks"]
    
    file = open(FILE_NAME, "w")
    writer = csv.DictWriter(file, fieldnames = fnames)
    writer.writeheader()
    for iter, member in df.iterrows():
        print(member[0])
        write_scorecard_one_member(member[1], member[0], writer, file)
        print(iter)

    file.close()

write_scorecard_entire_congress()


