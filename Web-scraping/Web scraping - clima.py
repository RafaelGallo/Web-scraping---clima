import pandas as pd
import json
import requests

from bs4 import BeautifulSoup
from datetime import date

date = date.today()
site_HTML = requests.get("https://api.hgbrasil.com/weather?key=e1a836da&lat=-23.682&log=-46.875&user_ip=remote").content

s = BeautifulSoup(site_HTML, "html.parser")
day = json.loads(s.prettify())
formt = json.dumps(day, indent = 2)
print(formt)
