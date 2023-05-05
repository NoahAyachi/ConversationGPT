import openai

# Set your OpenAI API key
openai.api_key = "YOUR API KEY HERE"


class ChatBot:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    # Sends the received message to the GPT-3 API and returns the response
    def respond(self, conversation):
        messages = [
            {**message, "role": (self.role if message["role"] == self.name else message["role"])}
            for message in conversation.get_messages()
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
        )
        response_content = response["choices"][0]["message"]["content"]
        return response_content.strip()


class Conversation:
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_messages(self):
        return self.messages


def chat(bot1, bot2, num_turns, start_message):
    conversation = Conversation()
    conversation.add_message(bot1.role, start_message)
    print(f"{bot1.name}: {start_message}")
    print()

    last_message = start_message

    for _ in range(num_turns):
        response = bot2.respond(conversation)
        conversation.add_message(bot2.role, response)

        # Print only the new message from the conversation (skip if it's the same as the last message)
        if response != last_message:
            print(f"{bot2.name}: {response}")
            print()

        # Swap their roles for the next turn
        bot1, bot2 = bot2, bot1
        last_message = response


if __name__ == "__main__":
    # Create two instances of ChatBot with their corresponding roles
    bot1 = ChatBot("Bot1", "user")
    bot2 = ChatBot("Bot2", "assistant")

    # Start the conversation between the two bots with an initial message and 4 more turns
    chat(bot1, bot2, 4, "The earth is flat!! I'm telling you! I dont care what you say or think")
    
    





