import urllib.request
import re
import nltk
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize
from googletrans import Translator

translator = Translator()

#nltk.download()

cadena = """Miami officially the City of Miami, is a coastal metropolis and the county seat of Miami-Dade County in South Florida.
 With a population of 442,241 as of the 2020 census, it is the second-most populous city in Florida and 11th-most populous city in 
 the Southeast.The Miami metropolitan area is the ninth-largest in the United States with a population of 6.138 million in 2020.
 The city has the third largest skyline in the U.S. with over 300 high-rises,58 of which exceed 491 ft (150 m).
 Miami is a major center and leader in finance, commerce, culture, arts, and international trade.Miami's metropolitan area is by far
the largest urban economy in Florida and the 12th-largest in the U.S., with a gross domestic product of $344.9 billion as of 2017.
According to a 2018 UBS study of 77 world cities, Miami is the second richest city in the U.S. and third richest globally in purchasing 
power. Miami is a majority-minority city with a Hispanic population of 310,472, or 70.2 percent of the city's population,
as of 2020."""
#enlace = "https://es.wikipedia.org/wiki/Python"
#html = urllib.request.urlopen(enlace).read().decode('utf-8')
text = get_text(cadena)

print("############################################")

#Removing square brackets and extra spaces
formatted_article_text = re.sub('[^a-zA-z]', ' ', text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

sentence_list = nltk.sent_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

#CALCULA LA FRASE QUE MAS SE REPITE
sentence_scores ={}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 50:
                if sent not in  sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

#REALIZA EL RESUMEN CON LAS MEJORES FRASES
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)

summary = translator.translate(summary, dest='es').text
print(summary)