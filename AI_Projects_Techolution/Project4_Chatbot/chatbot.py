from groq import Groq

# Add your API key
client = Groq(api_key="YOUR_API_KEY")

print("=== Simple AI Chatbot ===")
print("Type 'exit' to stop")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot stopped.")
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    answer = response.choices[0].message.content

    print("Bot:", answer)