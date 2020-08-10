import requests
import json
import csv


response = requests.get("https://www.balldontlie.io/api/v1/players")


fs= open("nba.json", "w+")
json.dump(response.json(), fs)
fs.close()


nba_json =response.json()

for datapoint in nba_json["data"]:
    print("ID: " + str(nba_json["data"].index(datapoint)))   
    print("Vorname: " + str(datapoint["first_name"]))
    print("Nachname: " + str(datapoint["last_name"]))
    print("Team: " + str(datapoint["team"]["full_name"]))
    

print("Funktion1")



f = open("data.csv" , "w+" , newline="")


header = ["id" , "Vorname" , "Nachname" , "Team"] 
writer = csv.writer(f, delimiter=";")
writer.writerow(header)

for datapoint in nba_json["data"]:
    
    data = [str(nba_json["data"].index(datapoint))]
    Vorname = [str(datapoint["first_name"])]
    Nachname = [str(datapoint["last_name"])]
    Team= [str(datapoint["team"]["full_name"])]
    
    writer.writerow(data + Vorname + Nachname + Team)

f.close()