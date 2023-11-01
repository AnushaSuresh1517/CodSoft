# Define a dictionary of predefined rules
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm here to help you.",
    "what's your name": "I'm just a chatbot, so I don't have a name. How can I assist you?",
    "bye": "Goodbye! If you have more questions in the future, feel free to come back.",
    "default": "I'm not sure how to respond to that. Please ask another question.",
}

# Define a function to generate responses based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case insensitivity

    # Check if the user input matches any predefined rules
    if user_input in responses:
        return responses[user_input]
    else:
        return responses["default"]

# Main chat loop
print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    
    response = chatbot_response(user_input)
    print("Chatbot:", response)
