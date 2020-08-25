import requests
import json
import csv
from time import sleep
import datetime


with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)


base_url = config_data["base_url"]

games_request_count = config_data["games_request_count"]


responseTeams = requests.get("https://www.balldontlie.io/api/v1/teams")


#fs=open("Teams.json", "w+") 
#json.dump(responseTeams.json(), fs)
#fs.close()

teams_json = responseTeams.json()



#style guide python anschauen! (variablen, for-schleife)




#fs=open("games.json", "w+") 
#json.dump(response2.json(), fs)
#fs.close()


#games_json = response2.json()




for datapoint in teams_json["data"]:

   

    teamId = datapoint["id"]

    zeit = datetime.datetime.now()

    this_year =zeit.year  

    anzahl = "100" #Aufgabe: Anzahl aus config.json
    

    

    print("Abkürzung: " + str(datapoint ["abbreviation"]))
    print("Stadt: " + str(datapoint ["city"]))
    print("Lage: " + str(datapoint ["conference"]))
    print("Liga: " + str(datapoint["division"]))
    print("Teamname: " +str(datapoint["full_name"]))


    responseGames = requests.get(
        'https://www.balldontlie.io/api/v1/games',
        params={'team_ids[]': teamId, "seasons[]": this_year, "per_page" : anzahl  },
    )

    gamesJson = responseGames.json()

    print("Anzahl Spiele : " + str(len(gamesJson["data"])) )

    

    for datapoint2 in gamesJson ["data"]:
        
        home_team = datapoint2 ["home_team"]["full_name"]
        home_team_score = datapoint2 ["home_team_score"]
        visitor_team = datapoint2 ["visitor_team"]["full_name"]
        visitor_team_score = datapoint2 ["visitor_team_score"]

        print(home_team, visitor_team_score, " - ", visitor_team, visitor_team_score)

  


    
    print("")
    print("")


    sleep(2)


    
    
   






