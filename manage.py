#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


################################################################################################################################
def f():
    from transformers import T5Tokenizer, T5ForConditionalGeneration

    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")

    input_ids = tokenizer("""summarize:  A language model consists of a single Transformer
    layer stack and is fed the concatenation of the input 
    and target, using a causal mask throughout. 

    As usual with LMs, the output only attends to the past input or output..""", return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

    import requests
from bs4 import BeautifulSoup


def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('article')

    return article.text

"""
url = 'http://www.fontanka.ru/2018/04/12/086/'
text = get_text(url)
# print(text)
print(text[:100])  # Первые 100 символов из строки
"""

################################################################################################################################
