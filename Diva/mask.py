import spacy
from spacy.tokens import Token

# Load the English language model
nlp = spacy.load("en_core_web_sm")

new_words = ["Vauban", "\n\n", "\n", "\xa0", "VAUBAN", "vauban", '"', "'", "-"]

# Add the new words to the vocabulary
for word in new_words:
    nlp.vocab.strings.add(word)

# Create a set of valid English words from spaCy's vocabulary
valid_words = set(nlp.vocab.strings)

# Register the custom attribute on the Token class
Token.set_extension("is_non_english", default=False, force=True)

# Define a custom component to replace non-English words
@spacy.Language.component("replace_non_english")
def replace_non_english(doc):
    for token in doc:
        if token.text.lower() not in valid_words:
            token._.is_non_english = True
        else:
            token._.is_non_english = False

    new_tokens = ["[MASK]" if token._.is_non_english else token.text for token in doc]
    return nlp.make_doc(" ".join(new_tokens))

# Add the custom component to the pipeline
nlp.add_pipe("replace_non_english", last=True)

def mask_text(text):
    text = text.replace('"', ' " ')
    doc = nlp(text)
    output_text = " ".join([token.text for token in doc])
    output_text = output_text.replace('[ MASK ]', '[MASK]')
    return output_text
