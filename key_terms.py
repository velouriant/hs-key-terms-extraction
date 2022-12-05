from lxml import etree
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import string

nltk.download('averaged_perceptron_tagger')

file = etree.parse('news.xml').getroot()
article_list = []
lemmatizer = nltk.stem.WordNetLemmatizer()
vectorizer = TfidfVectorizer()

for article in file[0].iterfind('news'):
    token_text = nltk.tokenize.word_tokenize(article[1].text.lower())
    lemma_text = [lemmatizer.lemmatize(word) for word in token_text]
    filtered_lemmas = [x for x in lemma_text if
                       x not in list(string.punctuation) and
                       x not in nltk.corpus.stopwords.words('english') and
                       nltk.pos_tag([x])[0][1] == "NN"]
    article_list.append({"Heading": article[0].text, "Text": " ".join(filtered_lemmas)})

tfidf_matrix = vectorizer.fit_transform([article['Text'] for article in article_list])
terms = vectorizer.get_feature_names_out()

tfidf_array = tfidf_matrix.toarray()

counter = 0
for article in article_list:
    article['Top'] = [(terms[x], tfidf_array[counter][x]) for x in np.flip((tfidf_array[counter]).argsort()[-10:])]
    article['Top'].sort(key = lambda tup: (tup[1], tup[0]), reverse=True)
    counter += 1
    print(article['Heading'] + ":")
    print(' '.join([tup[0] for tup in article['Top'][:5]]))

