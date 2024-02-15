import spacy
import re

nlp = spacy.load("en_core_web_sm")

keywords_set = {"a", "b", "c"}

principal_pattern = re.compile(r"\b(principals?|principle)\b(?:'s)?(?: room| office)?", re.IGNORECASE)

def extract_keywords(text):
    doc = nlp(text)

    keywords = []
    for token in doc:

        token_text_lower = token.text.lower()


        if token_text_lower in keywords_set:
            keywords.append("block_" + token.text.upper())


        if principal_pattern.search(token_text_lower):
            keywords.append("principal")

    return keywords
