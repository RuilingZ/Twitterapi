import os
from google.cloud import language_v1

client=language_v1.LanguageServiceClient()

text = "Hello world."

document = language_v1.Document(content=text, type=language_v1.Document.Type.PLAIN_TEXT)
print("Text: {}".format(text))

score = words.document_sentiment.score
magnitude = words.document_sentiment.magnitude
sentiment = client.analyze_sentiment(request={'document':doc})
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))