#creating chatbot
def chatbot():
    print("chatbot: Hey!\nType bye to end conversation")
    while True:
        user = input("user: ").lower()
        if user == "hello":
            print("chatbot: Hi!")
        elif user == "how are you":
            print("chatbot: I am fine, Thanks.")
        elif  user == "hi":
            print("Hey!")
        elif user == "what is your name":
            print("chatbot: I am a python chatbot")
        elif user == "bye":
            print("chatbot: Goodbye!")
            break
        else:
            print("Sorry, I do not understand.")

chatbot()

