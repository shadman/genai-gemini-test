import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY="AIzaSyBaAqUTlHXMyoP3TUqwLWvdTe44UxugmeE"
genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


model = genai.GenerativeModel('gemini-1.5-flash')

# input and pass through generative content
input = "What is the meaning of life?"
response = model.generate_content(input)

to_markdown(response.text)

#other help 
#response.prompt_feedback
#response.candidates
#https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb#scrollTo=5b4Hkfj-pm3p
