import sys
import os
from openai import OpenAI


def translate(text):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(text)
        sys.exit(0)

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Translate the following Chinese text to English. Output ONLY the translated English text, nothing else."},
            {"role": "user", "content": text},
        ],
    )
    print(response.choices[0].message.content.strip())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)

    input_text = " ".join(sys.argv[1:])
    translate(input_text)
