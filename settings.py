SEARCH_KEY = "insert your own"
SEARCH_ID = "insert your own"
COUNTRY = "in"

SEARCH_URL= "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&gl=" +COUNTRY
RESULT_COUNT=20

import os
if os.path.exists("private.py"):
    from private import *