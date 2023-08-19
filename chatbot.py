#import lib
import tkinter as tk
from tkinter import messagebox

# Define rules and responses according to need
rules = {
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "what is your name": "I'm a chatbot, so I don't have a name.",
    "bye": "Goodbye! Have a great day!",
}

#GUI of chatbot
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot")  #title

        self.chat_display = tk.Text(root, state='disabled')
        self.chat_display.pack(fill='both', expand=True)  #dis

        self.user_input = tk.Entry(root)
        self.user_input.pack(fill='x')

        self.send_button = tk.Button(root, text="Send", command=self.process_input) #send btn
        self.send_button.pack()

        self.chat_display.tag_config("bot", foreground="blue")
        self.chat_display.tag_config("user", foreground="green") #Gui frontend

    def process_input(self):
        user_message = self.user_input.get()   #input
        self.user_input.delete(0, tk.END)

        response = self.get_response(user_message)  #res

        # chat set
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, "You: " + user_message + "\n", "user")
        self.chat_display.insert(tk.END, "Bot: " + response + "\n", "bot")
        self.chat_display.configure(state='disabled')

        self.chat_display.see(tk.END)
        # gen response
    def get_response(self, user_input):
        user_input = user_input.lower()
        response = "I'm not sure how to respond to that."

        for pattern, reply in rules.items():
            if pattern in user_input:
                response = reply
                break

        return response
    # calling methods in main to load
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()
