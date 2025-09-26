import spacy


# load english language model

nlp = spacy.load("en_core_web_sm")

# Text

text = "Apple is looking at buying U.K startup or $1 billion"

# process the text

doc = nlp(text)
print(doc)

# print named entities found in the text

print("Named Entities, Phrases, and Concepts")

for ent in doc.ents:
    print(f"{ent.text:15} {ent.label_:10} {ent.start_char:10} {ent.end_char:10}")

# Text summarization -- Summarizes the core content of the documents


doc = nlp("data science and ai and gen ai creates a great career")

'''for token in doc:
    print(token)

for token in doc:
    print(token.pos_)

for token in doc:
    print(token)'''

for token in doc:
    print(token.text , token.pos_ , token.lemma_ , token.dep_ , token.tag_ , token.is_alpha, token.is_stop)


text = """There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[4] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured """

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

print(len(STOP_WORDS))

stopWords = list(STOP_WORDS)

print(stopWords)

doc = nlp(text)

print(doc)


tokens = [token.text for token in doc]
print(tokens)

# calculate the frequency of the tokens 

word_frequencies = {}

for word in doc:
    if word.text.lower() not in stopWords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text]+=1

print(word_frequencies)
print(word_frequencies.values())
max_frequency = max(word_frequencies.values())
print(max_frequency)

# get the normalized frequency 

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

print(word_frequencies)

sentence_tokens = [sent for sent in doc.sents]
print(sentence_tokens[0])

sentence_scores = {}

for sentence_token in sentence_tokens:
    sent_weight = 0
    for sent_word in sentence_token:
        word = sent_word.text.lower()
        if word in word_frequencies:
            sent_weight += word_frequencies[word]
    sentence_scores[sentence_token] = sent_weight
    print(f" weight of sentence {sentence_token} is {sentence_scores[sentence_token]}")

from heapq import nlargest

# create top  6 sentences 

select_length = int(len(sentence_tokens)*0.4)
print(select_length)

summary = nlargest(select_length, sentence_scores, sentence_scores.get)
print(summary)

# if we need to combine all these sentences 

final_summary = [summ.text for summ in summary]
print(final_summary)