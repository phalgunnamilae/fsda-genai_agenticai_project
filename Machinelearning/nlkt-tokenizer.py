import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, blankline_tokenize
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

AI = '''Artificial Intelligence refers to the intelligence of machines. This is in contrast to the natural intelligence of
humans and animals. With Artificial Intelligence, machines perform functions such as learning, planning, reasoning and
problem-solving. Most noteworthy, Artificial Intelligence is the simulation of human intelligence by machines.
It is probably the fastest-growing development in the World of technology and innovation. Furthermore, many experts believe
AI could solve major challenges and crisis situations.'''

type(AI)

# Breaks the text into tokens 

AI_tokens = word_tokenize(AI)
print(AI_tokens)
print(len(AI_tokens))

# returns the number of sentences 

AI_sentence = sent_tokenize(AI)
print(AI_sentence)
print(len(AI_sentence))

# Returns the number of paragraphs

AI_blank = blankline_tokenize(AI) 
print(AI_blank)
print(len(AI_blank))


from nltk.tokenize import WhitespaceTokenizer

wt = WhitespaceTokenizer().tokenize(AI)
print(wt)
print(len(wt))

s = 'Good apple cost $3.88 in hyderabad. Please buy two of them. Thanks'

from nltk.tokenize import wordpunct_tokenize

wt_punct = wordpunct_tokenize(s)
print(wt_punct)
print(len(wt_punct))

wt_punct1 = wordpunct_tokenize(AI)
print(wt_punct1)
print(len(wt_punct1))

from nltk.util import bigrams, trigrams, ngrams

sample_string = "I have started my AI journey"
quotes_tokens = nltk.word_tokenize(sample_string)
print(quotes_tokens)
print(len(quotes_tokens))

# bigrams forms the tuples with 2 tokens
quotes_bigrams = list(nltk.bigrams(quotes_tokens))
quotes_bigrams

# trigrams forms the tuples with 3 tokens
quotes_trigrams = list(nltk.trigrams(quotes_tokens))
quotes_trigrams

# ngrams

quotes_ngrams = list(nltk.ngrams(quotes_tokens, 5))
quotes_ngrams


# Stemming

from nltk.stem import PorterStemmer

pst = PorterStemmer()

pst.stem('affection')

pst.stem('cutting')

pst.stem('enthusiasm')

word_to_stem = ['give','giving','given','gave', 'thinking', 'Phalgun kumar']

for i in word_to_stem:
    print(i + ':' +pst.stem(i))
    
    
# Lancester Stemmer

from nltk.stem import LancasterStemmer

lst = LancasterStemmer()

for word in word_to_stem:
    print(word + ':' + lst.stem(word))
    
    
# Snowball stemmer

from nltk.stem import SnowballStemmer

sbst = SnowballStemmer("german")  # choose a language

sbst.stem("Autobahen")

# Wordnet lemmatizer -- gives the complete word

from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer

word_lem = WordNetLemmatizer()

word_to_stem

for word in word_to_stem:
    print(word_lem.lemmatize(word))
    

from nltk.corpus import stopwords

stopwords.words('english')

len(stopwords.words('english'))

stopwords.words('french')
len(stopwords.words('french'))

stopwords.words('german')
len(stopwords.words('german'))

stopwords.words('chinese')
len(stopwords.words('chinese'))

stopwords.words('tamil')
len(stopwords.words('tamil'))


sent = 'sam is natural when comes to drawing'

sent_tokens = word_tokenize(sent)

sent_tokens

for token in sent_tokens:
    print(nltk.pos_tag([token]))


from nltk import ne_chunk

NE_sent = 'The US president stays in white house'

word_tokens = word_tokenize(NE_sent)

for word_token in word_tokens:
    print(nltk.pos_tag([word_token]))

print(nltk.pos_tag(word_tokens))

ne_chunk(word_tokens)

# Create a list of word

text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")


from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
