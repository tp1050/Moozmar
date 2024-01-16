
import re


def extract_persian_literals_and_numbers(text):
    persian_literals = re.findall(r'[\u0600-\u06FF]+', text)
    numbers = re.findall(r'\d+', text)
    
    return persian_literals, numbers



