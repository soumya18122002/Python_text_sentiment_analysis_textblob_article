import nltk
nltk.download('punkt')
from textblob import TextBlob
from newspaper import Article

url = "https://en.wikipedia.org/wiki/Mathematics"

article = Article(url) # to make the url an article

article.download() # to download html content of the links
article.parse() # to retreive all the htmls from the article
article.nlp() # to make it prepare for the natural language processing or for keyword extraction from the html that we received from the link

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
# here polarity defines that if it is -1.0 the text is a negative one and if it is in the side of 0 then neutral one and if it is near 1 then positive one 

print(sentiment)

with open('senti.txt','r') as f:
    text2 = f.read()

blob2 = TextBlob(text2)
sentiment2 = blob2.sentiment.polarity
print(sentiment2)