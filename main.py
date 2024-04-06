import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
   with open(file_path, 'r') as file:
     data: dict = json.load(file)
   return data

def save_knowledge_base(file_path: str, data: dict):
  with open(file_path, 'w') as file:
    json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    # Lowercase the user question for case-insensitive matching
    user_question_lower = user_question.lower()

    # Separate words in the user question
    user_words = user_question_lower.split()

    # Find best match based on keyword presence in question keywords
    best_match = None
    best_match_score = 0
    for question in questions:
        question_score = 0
        for keyword in question["keywords"]:
            if keyword in user_words:
                question_score += 1
        if question_score > best_match_score:
            best_match = question["question"]
            best_match_score = question_score

    # Optionally, consider using a minimum score threshold to avoid poor matches
    if best_match_score >= 2:  # Change threshold as needed
        return best_match
    else:
        return None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
      
def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer = input('')

            if new_answer.lower() != 'skip':
                new_question = user_input  # Capture the user's original question
                keywords = [word.lower() for word in user_input.split()]  # Extract keywords from user input
                knowledge_base["questions"].append({"question": new_question, "keywords": keywords, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned a new response')

if __name__ == '__main__':
    chat_bot()
