#from nltk.corpus import stopwords
#sw = stopwords.words("english")

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context

import nltk
nltk.download('all', halt_on_error=False)
