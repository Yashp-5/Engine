SEARCH_KEY = "823bea96335db4762"
SEARCH_ID = "AIzaSyAwXEjzKnTI35ksp8wWklJ2kOP1gC1Xcuo"
COUNTRY = "in"

SEARCH_URL= "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&gl=" +COUNTRY
RESULT_COUNT=20

import os
if os.path.exists("private.py"):
    from private import *