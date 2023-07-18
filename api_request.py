import requests

API_LINK = 'https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json'

# defined the variable to be appended
data = ''
data = requests.get(API_LINK)
transformedData = data.content