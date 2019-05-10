from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import requests
from bs4 import BeautifulSoup
from dateutil import parser
from textstat.textstat import textstat
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com'
}
url = 'https://blog.frame.io/2019/04/26/nab2019-patrick-southern/'
r = requests.get(url, headers=headers)
html = r.text.strip()
print(html)
