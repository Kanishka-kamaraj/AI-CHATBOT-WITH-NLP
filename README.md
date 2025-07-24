# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KANISHKA K

*INTERN ID*:  CT04DH1742

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*: 

AI CHATBOT USING PYTHON AND NLTK

1.DESCRIPTION :

This project is a simple yet functional AI-based chatbot built using Python and the Natural Language Toolkit (NLTK). The main objective of this chatbot is to simulate human-like interaction by responding to user queries in natural language. It demonstrates the basic use of natural language processing (NLP) concepts, text preprocessing techniques, and similarity matching to deliver relevant responses.

2. HOW IT WORKS :
   
The chatbot begins by greeting the user and waits for user input. When the user types a question or a statement, the chatbot processes the input through the following NLP pipeline:

Tokenization – Using NLTK’s word_tokenize, the input sentence is broken into individual words.

Lowercasing – The input is converted into lowercase to maintain consistency.

Removing Punctuation – All punctuation is stripped using Python's string module.

Stopword Removal – Commonly used words (like "is", "the", "a") are removed using NLTK’s stopwords.

Lemmatization – Each word is reduced to its base form using WordNetLemmatizer.

After cleaning the input, the chatbot uses TF-IDF Vectorization from Scikit-learn (TfidfVectorizer) to represent the processed text as a numerical vector. It then compares the user’s query with a predefined list of responses (sample corpus) using cosine similarity. The most similar response is selected and returned as the chatbot’s reply.

Additionally, the chatbot includes some hardcoded replies for common questions like:

"What is your name?"

"Who are you?"

"Tell me a joke"

"How does natural language processing work?"

This helps the bot respond more naturally and reduces irrelevant or repeated answers. If no suitable match is found, a default message like "I'm sorry! I don't understand that." is returned.

3. TECHNOLOGIES USED :

Python 3.13

NLTK: For tokenization, stopword removal, and lemmatization.

Scikit-learn: For TF-IDF vectorization and similarity comparison.

Random and String libraries for basic operations.

4. KEY FEATURES :
   
Simple NLP-based chatbot that can understand basic English sentences.

Handles greetings, basic identity questions, and jokes.

Uses machine learning-based similarity search to find the best response.

Custom rules to avoid repetitive responses and improve accuracy.

Exit command (bye) to gracefully end the conversation.

5. LEARNING OUTCOME :

This project is an excellent introduction to natural language processing, basic machine learning, and Python scripting. It helps beginners understand how machines can process human language using simple yet powerful tools. The modular structure allows future improvements such as adding more training data, integrating a GUI, or using deep learning models.

*OUTPUT* :

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/fe3fa672-9ada-49d5-b176-3071c05d41ef" />
