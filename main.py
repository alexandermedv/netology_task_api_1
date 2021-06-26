import requests


d = {}

hulk_url = "https://superheroapi.com/api/2619421814940190/search/hulk"
lis = requests.get(hulk_url).json()['results']
for item in lis:
    if item['name'] == 'Hulk':
        hulk = item
        d['hulk'] = int(hulk['powerstats']['intelligence'])

captain_america_url = "https://superheroapi.com/api/2619421814940190/search/Captain_America"
lis = requests.get(captain_america_url).json()['results']
for item in lis:
    if item['name'] == 'Captain America':
        cap = item
        d['Captain_America'] = int(cap['powerstats']['intelligence'])

thanos_url = "https://superheroapi.com/api/2619421814940190/search/Thanos"
lis = requests.get(thanos_url).json()['results']
for item in lis:
    if item['name'] == 'Thanos':
        thanos = item
        d['Thanos'] = int(thanos['powerstats']['intelligence'])

sort_heroes = sorted(d.items(), key=lambda x: x[1], reverse=True)
print('Самый умный супергерой:', sort_heroes[0][0], '\nЕго IQ составляет:', sort_heroes[0][1])
