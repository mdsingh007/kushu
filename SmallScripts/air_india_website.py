from bs4 import BeautifulSoup
import urllib

url = 'https://bookme.airindia.in/AirIndiaB2C/Booking/Select'

response = urllib.request.urlopen(url)
webContent = response.read()
open('air_india.html', 'a').write(str(webContent))
print(webContent)