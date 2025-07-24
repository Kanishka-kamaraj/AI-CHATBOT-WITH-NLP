import nltk
import warnings
import string
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Lemmatizer and tokenizer
lemmer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greeting handler
GREETING_INPUTS = ("hello", "hi", "greetings", "hey")
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Exact phrase responses
SPECIAL_RESPONSES = {
    "what is your name": "I'm just called 'Chatbot' for now 🙂",
    "who are you": "I'm a simple chatbot created using Python and NLTK.",
    "tell me a joke": "Why did the computer show up late to work? It had a hard drive!",
    "thank you": "You're welcome! 😊",
    "goodbye": "See you soon! Have a great day."
}

# Q&A data
qa_pairs = {
    "how does natural language processing work":
        "Natural Language Processing (NLP) allows machines to understand and process human language. It combines computational linguistics with AI and machine learning.",
    "what can you do":
        "I can chat, tell jokes, explain NLP, and help you understand how AI chatbots work.",
    "how are you":
        "I'm just a bunch of code, but I'm functioning perfectly! Thanks for asking 😄",
    "what is nlp":
        "NLP stands for Natural Language Processing. It's a branch of AI that helps computers understand and respond to human language.",
}

# Prepare TF-IDF from question list
question_list = list(qa_pairs.keys())
vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words=None)  # Don't remove stopwords
question_vectors = vectorizer.fit_transform(question_list)

# Generate response
def generate_response(user_input):
    user_input_clean = user_input.lower().strip()

    # Exact match
    if user_input_clean in SPECIAL_RESPONSES:
        return SPECIAL_RESPONSES[user_input_clean]

    # Vector similarity match
    tfidf_input = vectorizer.transform([user_input_clean])
    similarity_scores = cosine_similarity(tfidf_input, question_vectors)

    idx = similarity_scores.argsort()[0][-1]
    confidence = similarity_scores[0][idx]

    if confidence > 0.4:
        return qa_pairs[question_list[idx]]
    else:
        return "I'm sorry! I don’t understand that."

# Main loop
print("Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! 👋")
        break
    elif greeting(user_input):
        print("Chatbot:", greeting(user_input))
    else:
        print("Chatbot:", generate_response(user_input))
