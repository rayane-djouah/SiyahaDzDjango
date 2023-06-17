import json
from django.contrib.auth.hashers import make_password
import hashlib
import binascii
import os


nb_touristes = 5
nb_regionalemployee = 3
nb_centralemployee = 1
nb_users = nb_touristes+nb_regionalemployee+nb_centralemployee
data = []
region = ['Alger','Oran','Jijel']
pointinteret = ['Makam Chahid','La Corniche','Plage de Sidi Abdelaziz']
categorie = ['Monument','Zone de loisirs','Plage']
commune = [' Belouizdad','zouhour','Sidi Abdelaziz']
latitude = [36.7525,35.6997,36.8237]
longitude = [3.0420,-0.6308,5.7506]
trandportations = ['taxi','metro','tram','train','taxi']
theme = ['mémoire et patriotisme','la promenade et des loisirs en bord de mer','la détente et des activités balnéaires']
num_region = 0
description = ["Le Makam Chahid est un monument emblématique d'Alger, rendant hommage aux martyrs de la guerre de libération. Il se compose d'une imposante structure en forme de flamme offrant une vue panoramique.",
               "La Corniche est une promenade côtière animée offrant une vue magnifique sur la mer Méditerranée. Elle abrite des restaurants, des cafés et des boutiques, et est idéale pour se promener et profiter de l'atmosphère maritime.",
               "La plage de Sidi Abdelaziz est une magnifique plage de sable située à Jijel. Elle offre des eaux cristallines et une belle étendue de sable doré, propice à la détente et aux activités balnéaires. C'est un lieu prisé des visiteurs pour son paysage pittoresque et son ambiance paisible."]


for j in range(1, nb_users+1):
    """password = f"user{j}"
    salt = os.urandom(16)  # Génération d'un sel aléatoire

    # Hachage du mot de passe avec PBKDF2 et SHA-256
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    hashed_password = binascii.hexlify(hashed_password).decode('utf-8')"""
    user_data = {
        "model": "auth.user",
        "pk": j,
        "fields": {
            "password": f"user{j}",
            "last_login": None,
            "is_superuser": False,
            "username": f"user{j}",
            "first_name": f"first_name{j}",
            "last_name": f"last_name{j}",
            "email": f"user{j}@esi.dz",
            "is_staff": True,
            "is_active": True,
            "date_joined": "2023-01-01T00:00:00Z",
            "groups": [],
            "user_permissions": []
        }
    }

    if j <= nb_centralemployee:
        centralemployee_data = {
            "model": "SiyahaDzApp.centralemployee",
            "pk": j,
            "fields": {
                "user": j
            }
        }
        data.extend([user_data, centralemployee_data])
    elif j>nb_centralemployee and j<=nb_centralemployee+nb_regionalemployee:
        regionalemployee_data = {
            "model": "SiyahaDzApp.regionalemployee",
            "pk": j,
            "fields": {
                "user": j,
                "region": region[num_region]
            }
        }
        num_region+=1
        data.extend([user_data,regionalemployee_data])
    else:
        tourist_data = {
            "model": "SiyahaDzApp.tourist",
            "pk": j,
            "fields": {
                "user": j
            }
        }
        data.extend([user_data,tourist_data])

    for i in range(0,len(trandportations)):
        transportation_data = {
            "model": "SiyahaDzApp.transportation",
            "pk": trandportations[i],
            "fields": {
                "name": trandportations[i]
            }
        }
        data.extend([transportation_data])


    for i in range(0,len(region)):
        
        pointofinterest_data = {
            "model": "SiyahaDzApp.pointofinterest",
            "pk": pointinteret[i],
            "fields": {
                "name": pointinteret[i],
                "category": categorie[i],
                "theme": theme[i],
                "city": region[i],
                "commune": commune[i],
                "latitude": latitude[i],
                "longitude": longitude[i],
                "description": description[i],
                "views_count": 0,
                "openhour": "08:00:00",
                "closehour": "18:00:00"
            }
        }
        data.extend([pointofinterest_data])

    for i in range(0,len(trandportations)):
        for j in range(0,len(pointinteret)):
            pointofinterest_transportation_data = {
                "model": "SiyahaDzApp.pointofinterest_transportation",
                "pk": f"{pointinteret[j]}-{trandportations[i]}",
                "fields": {
                    "point_of_interest": pointinteret[j],
                    "transportation": trandportations[i]
                }
            }
            data.extend([pointofinterest_transportation_data])

    event_data = {
        "model": "SiyahaDzApp.event",
        "pk": "Cérémonie de commémoration des martyrs",
        "fields": {
            "name": "Cérémonie de commémoration des martyrs",
            "point_of_interest": pointinteret[0],
            "description": "Une cérémonie solennelle pour rendre hommage aux martyrs de la guerre de libération nationale",
            "opendate": "2023-07-05",
            "closedate": "2023-07-05",
            "image": f"storage/photoevent/event1.jpg"
        }
    }
    data.extend([event_data])

    event_data = {
        "model": "SiyahaDzApp.event",
        "pk": "Festival de la Corniche",
        "fields": {
            "name": "Festival de la Corniche",
            "point_of_interest": pointinteret[1],
            "description": "Festival de la Corniche",
            "opendate": "2023-08-15",
            "closedate": "2023-08-20",
            "image": f"storage/photoevent/event2.jpg"
        }
    }
    data.extend([event_data])

    event_data = {
        "model": "SiyahaDzApp.event",
        "pk": "Concours de sports nautiques",
        "fields": {
            "name": "Concours de sports nautiques",
            "point_of_interest": pointinteret[2],
            "description": "Un concours passionnant de sports nautiques, y compris le surf, la planche à voile et la natation, sur la magnifique plage de Sidi Abdelaziz",
            "opendate": "2023-07-10",
            "closedate": "2023-07-10",
            "image": f"storage/photoevent/event3.jpg"
        }
    }
    data.extend([event_data])

    for i in range(0,len(pointinteret)):
        photo_data = {
            "model": "SiyahaDzApp.photo",
            "pk": f"{pointinteret[i]}-point{i}.jpg",
            "fields": {
                "point_of_interest": pointinteret[i],
                "image": f"storage/point_of_interest/photos/point{i}.jpg"
            }
        }
        data.extend([photo_data])
"""# Générer un entier aléatoire entre 1 et 100 inclus
random_number = random.randint(0, len(trandportations)-1)"""


with open('data.json', 'w') as fichier:
    json.dump(data, fichier,indent=4)
