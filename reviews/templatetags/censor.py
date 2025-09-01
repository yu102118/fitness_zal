# reviews/templatetags/censor.py

from django import template
import re

register = template.Library()

BAD_WORDS = ['идиот', 'дерьмовый', 'Мастурбатор', 'фу']

@register.filter(name='censor')
def censor(value):
    def replace_bad_word(match):
        return '*' * len(match.group())
    
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, BAD_WORDS)) + r')\b', re.IGNORECASE)
    return pattern.sub(replace_bad_word, str(value))
