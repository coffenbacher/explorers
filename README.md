This is the official Github of the Explorers app.

Built by the Joint Explorers.


GET Search parameters to /activity/search/:
*type: string, name of activity
*latitude: float, lat of user. I.e. 120.0
*longitude: float, lng of user. I.e. 120.0
*radius: float, radius in miles to search
min_difficulty: float, minimum difficulty, i.e. 1
max_difficulty: float, maximum difficulty, i.e. 10
min_hours: float, minimum hours, i.e. 1
max_hours: float, minimum hours, i.e. 1000

RESPONSE:
[
{"name": "#WormFlows", "images": [], "longitude": -122.2, "hours": 6.0, "difficulty": 7, "latitude": 46.2},
{"name": "#Anotherhike", "images": [], "longitude": -122.2, "hours": 6.0, "difficulty": 7, "latitude": 46.2}
]
