import requests
from datetime import datetime

My_Lat = 20.593683
My_Lng = 78.962883

parameter ={
    "lat": My_Lat,
    "lng": My_Lng,
    "formatted": 0,
}  

response = requests.get("https://api.sunrise-sunset.org/json", 
                        params=parameter)
response.raise_for_status()
data =response.json()
sunrise =data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
datetime =datetime.now()
print(datetime.hour)

