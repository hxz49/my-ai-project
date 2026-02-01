import sys
import os
import google.generativeai as genai


def translate(text):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print(text)
        sys.exit(0)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        f"Translate the following Chinese text to English. "
        f"Output ONLY the translated English text, nothing else.\n\n{text}"
    )
    print(response.text.strip())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)

    input_text = " ".join(sys.argv[1:])
    translate(input_text)
