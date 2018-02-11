import re
import sys
import urllib2
import BeautifulSoup

usage = "Run the script: ./geolocate.py IPAddress"

ipaddr = str(raw_input("Enter an ip:"))

geody = "http://www.geody.com/geoip.php?ip=" + ipaddr

geody = "https://www.geody.com/geolook.php?world=terra&map=col&q="+ipaddr+"&subm1=go"
html_page = urllib2.urlopen(geody).read()
soup = BeautifulSoup.BeautifulSoup(html_page)

# Filter paragraph containing geolocation info.
paragraph = soup('table')

# Remove html tags using regex.
#geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print paragraph