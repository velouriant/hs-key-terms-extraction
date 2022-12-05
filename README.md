# hs-key-terms-extraction
 'Key Terms Extraction' project from Hyperskill Python Core path

## Description
Extracting keywords can help you get to the text meaning. Also, It can help you with splitting texts into different categories. In this project, you will learn how to extract relevant words from a collection of news stories. There are many different ways to do it, but we will focus on frequencies, part-of-speech search, and TF-IDF methods. Note that each method can yield the results with varying degrees of accuracy for different texts. In reality, it is always good to try various methods and choose the best.

Script ultimately takes in an xml file containing text of multiple news articles and then:
- Extracts the text;
- Tokenises the words in each article
  - i.e. splits the text into separate words / wordparts
- Lemmatises that list of words
  - i.e. tries to reduce each word to its root word (e.g. 'driven' -> 'drive')
- Filters out everything other than nouns, using 'part of speech' tagging
- Filters out things like punctuation and stopwords (e.g. 'a', 'an', 'the', 'in'), by accessing existing collections in 'string' and 'nltk' module
- Uses Term Frequency-Inverse Document Frequency (TF-IDF) from the 'sklearn' module to identify most important words in each article
  - In essence, TF-IDF identifies most important words by comparing frequency of word in a given document as compared to the frequency of that same word in a bigger corpus of material
- Identifies the 5 most 'important' nouns in each text according to TF-IDF analysis, which requires accessing and interpreting matrix results, and prints those words out with the title of each article 
