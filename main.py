from newspaper import Article
import nltk
from gtts import gTTS
import os

article = Article('https://traficozmg.com/2023/09/cierres-viales-por-manifestaciones-del-28s-estas-seran-las-rutas/')
article.download()
article.parse()

nltk.download('punkt')
article.nlp()
language = 'es'
mytext = article.text
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("read_article.mp3")
os.system("start read_article.mp3")
