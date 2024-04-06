import json

# Sample knowledge base (replace with actual data structure)
knowledge_base = {}

def save_knowledge_base(data):
    """Saves the knowledge base to a JSON file."""
    try:
        with open("knowledge_base.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Knowledge base saved successfully!")
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error saving knowledge base: {e}")

def load_knowledge_base():
    """Loads the knowledge base from a JSON file."""
    try:
        with open("knowledge_base.json", "r") as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading knowledge base: {e}")
        return {}

def greet():
    """Greets the user."""
    print("Hi! I'm your learning chatbot. Let's chat!")

def learn(user_input):
    """Learns from user input by updating the knowledge base."""
    # Basic learning logic (replace with more sophisticated NLP techniques)
    words = user_input.lower().split()
    for word in words:
        if word not in knowledge_base:
            knowledge_base[word] = 1
        else:
            knowledge_base[word] += 1

def respond(user_input):
    """Responds to the user based on learned knowledge."""
    # Simple response based on word frequency (improve with natural language processing)
    words = user_input.lower().split()
    most_frequent_word = max(knowledge_base, key=knowledge_base.get)
    if most_frequent_word in user_input:
        return f"Interesting! You seem to be interested in '{most_frequent_word}'. Tell me more!"
    else:
        return "That's new! I'm learning from you. How can I help you today?"

def main():
    """Main loop for chat interaction."""
    knowledge_base = load_knowledge_base()  # Load existing knowledge base
    greet()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        learn(user_input)
        response = respond(user_input)
        print("Chatbot:", response)

        save_knowledge_base(knowledge_base)  # Update knowledge base

if __name__ == "__main__":
    main()
