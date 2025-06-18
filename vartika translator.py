from deep_translator import GoogleTranslator

# Mapping numbers to language codes
LANGUAGE_OPTIONS = {
    "1": ("Hindi", "hi"),
    "2": ("English", "en"),
    "3": ("Sanskrit", "sa"),
    "4": ("Spanish", "es"),
    "5": ("French", "fr"),
    "6": ("Russian", "ru"),
    "7": ("Marathi", "mr"),
    "8": ("Tamil", "ta"),
    "9": ("Telugu", "te")
}

def show_language_menu():
    print("Choose a language to translate TO:")
    for num, (name, _) in LANGUAGE_OPTIONS.items():
        print(f"{num}. {name}")

def get_language_code(choice):
    return LANGUAGE_OPTIONS.get(choice, (None, None))[1]

def translate_text(text, target_language_code):
    try:
        translated = GoogleTranslator(source='auto', target=target_language_code).translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {str(e)}"

def chatbot():
    print("🌍 Translation Chatbot by VARTIKA (Choose from 9 languages)")
    print("Type 'exit' to quit.\n")

    show_language_menu()
    lang_choice = input("Enter the number for the target language: ").strip()
    target_lang_code = get_language_code(lang_choice)

    if not target_lang_code:
        print("❌ Invalid choice. Please restart the program.")
        return

    print(f"\nYou selected: {LANGUAGE_OPTIONS[lang_choice][0]}")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        result = translate_text(user_input, target_lang_code)
        print(f"Bot (translated): {result}")

if __name__ == "__main__":
    chatbot()
