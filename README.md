
# Python Text Sentiment Analysis Using TextBlob & Article




## Installation

For this project need to install nltk

```bash
  pip install nltk
```
The Natural Language Toolkit (NLTK) is an open source Python library for Natural Language Processing. A free online book is available. (If you use the library for academic research, please cite the book.)

Steven Bird, Ewan Klein, and Edward Loper (2009). Natural Language Processing with Python. O'Reilly Media Inc.
https://www.nltk.org/book/

For this project need to install textblob

```bash
  pip install textblob
```
Textblob helps us to take a small chunk of texts like a paragraph from a big story or the summary of the story

For this project need to install newspaper3k
```bash
  pip install newspaper3k
```

## Documentation

[Go through the project the link is given here click me](https://github.com/soumya18122002/Python_text_sentiment_analysis_textblob_article)

We are going to analyse the sentiment of an newspaper so this module is needed

Here first you can see we take an url into the variable url

url = "https://en.wikipedia.org/wiki/Mathematics" 

Then convert it into the object of the Article to take some of the part of the webiste as an article then download all the html of the article using **download()** method then ready it for the natural language processsing using the method **nlp()**

For downloading the article also firstly we need to do run a command ino the code 
```bash
import nltk
nltk.download('punkt')
```
Then if you analysis all the html then simply store **article.text** in a variable or if you store only the summary of the text then need to run **article.summary**

Now to analysis the sentiment we need to make the object of the TextBlob and then need to check the sentiment more specifically the polarity of the sentiment

Sentiment return a tuple of form (polarity, subjectivity ) where polarity is a float within the range [-1.0, 1.0] and subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. :rtype: namedtuple of the form Sentiment(polarity, subjectivity)

Now we can simply print the sentiment if it comes near -1 it is negative if it comes near 1 then it is something positive


We also can do experiment by making an text file here I make a dammy text file named **senti.txt** and analysis the sentiment of that file