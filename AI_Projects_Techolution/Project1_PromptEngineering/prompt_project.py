from groq import Groq
import pandas as pd

# Add your Groq API key
client = Groq(api_key="YOUR_API_KEY")

text = """
Artificial Intelligence is transforming industries by automating tasks,
improving efficiency, and enabling better decision-making.
"""

prompts = [
    "Summarize this text in simple words:",
    "Give a short summary of this text:",
    "Explain this in easy language:",
    "Summarize in 3 bullet points:"
]

results = []

for p in prompts:

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": p + text
            }
        ]
    )

    output = response.choices[0].message.content

    results.append([p, output])

# Save results to Excel
df = pd.DataFrame(results, columns=["Prompt", "Output"])

df.to_excel("results.xlsx", index=False)

print("Done! Check results.xlsx")