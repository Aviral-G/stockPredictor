from newspaper import Article
import nltk

# Ensure punkt is downloaded
nltk.download('punkt')

url = 'https://www.yahoo.com/news/labor-board-accuses-apple-suppressing-222846876.html'
article = Article(url)

try:
    article.download()
    article.parse()
    article.nlp()  # Run NLP after parsing

    # Print results
    print("Summary:", article.summary)
except Exception as e:
    print("An error occurred:", e)