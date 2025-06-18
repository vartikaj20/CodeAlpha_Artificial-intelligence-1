import json
import os
import difflib

DATA_FILE = "faq_data.json"

def load_faq_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    else:
        return {
            "what is your name": "I'm FAQBot, your assistant!",
            "who made you": "FAQ Bot made by Vartika.",
            "faq bot made by vartika": "Yes, FAQ Bot is proudly made by Vartika!",
            "what is the capital of india": "New Delhi is the capital of India.",
            "why is it made": "It is made for my internship.",
            "where is it made": "It is made in India, Bharat.",
        }

def save_faq_data(faq_data):
    with open(DATA_FILE, "w") as f:
        json.dump(faq_data, f, indent=4)

def find_best_match(question, faq_data, threshold=0.75):
    question = question.lower().strip()
    questions = list(faq_data.keys())
    matches = difflib.get_close_matches(question, questions, n=1, cutoff=threshold)
    if matches:
        # Additionally, check similarity ratio explicitly
        ratio = difflib.SequenceMatcher(None, question, matches[0]).ratio()
        if ratio >= threshold:
            return matches[0]
    return None

def get_answer(question, faq_data):
    matched_question = find_best_match(question, faq_data)
    if matched_question:
        return faq_data[matched_question]
    return None

def learn_new_answer(question, faq_data):
    answer = input("I don't know the answer. Please teach me:\nYou: ").strip()
    faq_data[question.lower().strip()] = answer
    save_faq_data(faq_data)
    print("FAQBot: Thank you! I've learned something new and saved it.")

def run_chatbot():
    faq_data = load_faq_data()
    print("🤖 Welcome to the FAQ Chatbot! Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("FAQBot: Goodbye!")
            break

        answer = get_answer(user_input, faq_data)
        if answer:
            print("FAQBot:", answer)
        else:
            learn_new_answer(user_input, faq_data)

if __name__ == "__main__":
    run_chatbot()



