from django.test import TestCase

# Create your tests here.

from rake_nltk import Rake

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

# Extraction given the text.
r.extract_keywords_from_text('''It is extremely fun to implement algorithms by reading papers. It is the digital equivalent of DIY kits.

There are some rather popular implementations out there, in python(aneesha/RAKE) and node(waseem18/node-rake) but neither seemed to use the power of NLTK. By making NLTK an integral part of the implementation I get the flexibility and power to extend it in other creative ways, if I see fit later, without having to implement everything myself.

I plan to use it in my other pet projects to come and wanted it to be modular and tunable and this way I have complete control.''')

# Extraction given the list of strings where each string is a sentence.
# r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
print(r.get_ranked_phrases())

# To get keyword phrases ranked highest to lowest with scores.
print(r.get_ranked_phrases_with_scores())