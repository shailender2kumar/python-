

from openai import OpenAI
# client = OpenAI(api_key="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")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)