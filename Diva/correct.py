from .mask import mask_text
from .unmask import unmask_text

def correct_words(text):
    return unmask_text(mask_text(text))
