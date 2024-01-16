import requests

def find_doctors(lat, lon,q='  پوست دکتر'):

  # API URL updated
  url = 'https://nominatim.openstreetmap.org' 
  
  params = {
    'q': q,
    'format': 'json',
    'lat': lat,
    'lon': lon,    
    'addressdetails': 1
  }

  response = requests.get(url, params=params)
  
  KEY=
  
  def search_neshan(lat, lon,q='  پوست دکتر'):
      url=f"https://api.neshan.org/v1/search"
      
      params={
          "term":q,
          "lat":lat,
          "lon":lon
          }
      header={"Api-Key":KEY}
      r=req
