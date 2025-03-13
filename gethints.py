import requests
import scapy.all as scapy


right = 0
down = 2
left = 4
up = 6

def get_items (x, y, direction):
    url = f"https://api.dofusdb.fr/treasure-hunt?x={x}&y={y}&$limit=50&lang=fr&direction={direction}"
    payload = {}
    headers = {
  'Token': 'PUT YOUR TOKEN HERE !!!!!!!!!!!!'
}
    response = requests.request("GET", url, headers=headers, data=payload).json()
    return response["data"]


def get_item_distance(item_data, item_name: str):
    for map in item_data:
        for pois in map["pois"]:
            if str(pois['name']['fr']).strip()  == item_name.strip():
                return map["distance"]
    return -1 


distance = get_item_distance(get_items(-2, 0, down), "Fleurs smiley")
print(distance)