import requests, json

url = "https://query.dropbase.io/dijpjzk7xhdcmbjn27cn7bo/TorontoFinal"

auth = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoiaWpwSnprN3hIZGNNYmpuMjdDTjdibyIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6Ill6Y3U5V1lQcnRIQ2ZCRnh4R2w2ZWJYc1l5bVlUNm5zTTlUem4wMjc3WkowWmRjS1l3RHh2blpYMnNMZmNsVEUiLCJpYXQiOjE2MTA4NjAxMTYsImV4cCI6MTYxMDk0NjUxNiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJBUkxvREh4dzY3ejlraVN1OWY3V0wyIn0.RokV1x7kiQw3d9lhGcq-ny7FhgurwsQQrNcHhrA4sXc"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhYmFzZUlkIjoiaWpwSnprN3hIZGNNYmpuMjdDTjdibyIsImFjY2Vzc1Blcm0iOiJmdWxsIiwidG9rZW5JZCI6Ill6Y3U5V1lQcnRIQ2ZCRnh4R2w2ZWJYc1l5bVlUNm5zTTlUem4wMjc3WkowWmRjS1l3RHh2blpYMnNMZmNsVEUiLCJpYXQiOjE2MTA4NjAxMTYsImV4cCI6MTYxMDk0NjUxNiwiaXNzIjoiZHJvcGJhc2UuaW8iLCJzdWIiOiJBUkxvREh4dzY3ejlraVN1OWY3V0wyIn0.RokV1x7kiQw3d9lhGcq-ny7FhgurwsQQrNcHhrA4sXc'
}

#response = requests.request("GET", 'https://query.dropbase.io/ijpJzk7xHdcMbjn27CN7bo/toronto2?select=matchup', headers=headers)
#r = response.text
#print(response.text.encode('utf8'))
#print(r)

# test = requests.get('https://query.dropbase.io/ijpJzk7xHdcMbjn27CN7bo/toronto2?matchup=eq.JAN 10, 2021 - TOR @ GSW', headers=headers)
# print(test.text)
      

def filter_matchups():
    playedGames = []
    response = requests.get('https://query.dropbase.io/ijpJzk7xHdcMbjn27CN7bo/toronto2?select=matchup', headers=headers)
    r = response.json()
    for x in range(len(r)):
        game = r[x]["matchup"]
        if game not in playedGames:
            playedGames.append(game)
        else:
            pass
    return playedGames

 
def get_rows(gameSelect):
    test = requests.get(f'https://query.dropbase.io/ijpJzk7xHdcMbjn27CN7bo/toronto2?matchup=eq.{gameSelect}', headers=headers)
    return test.json()

#print(filter_matchups())
#rint(get_rows("JAN 10, 2021 - TOR @ GSW"))
      
      

      

      

      

      

      

      

      

      

      

      
