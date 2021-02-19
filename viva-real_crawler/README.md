# Web scrapping project - Viva Real - Curitiba apartment listings

This project was built using mainly python and selenium to get some data about the apartment listing prices in Curitiba-PR-Brazil. The data was obtained from the Viva Real site, and processed using Python.

The data was collect on 20210216 and it's not intended to be exhaustive.

Libraries used:
```python
from selenium import webdriver
import pandas as pd
import time
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import re 
import seaborn as sns
import numpy as np
import math
from geopy.extra.rate_limiter import RateLimiter
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
```


Some visualization of the data:

