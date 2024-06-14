# Deeva

This far-from perfect project is a simple demostration of detecting incorrect words in a text
and contextually filling them up with the help of Distil-Bert-Base backbone. 

# Installation

pip install git+https://github.com/yourusername/your-repo.git
python -m spacy download en_core_web_sm

# Example Usage

import Diva

text = '''I am a scientist at NASA that is discussing the "face" on mars. I will be explaining how the "face" is
 land form. By sharing my information about this isue i will tell you just that. First off, how could it be a
 martions drawing. There is no plant life on mars as of rite now that we know of, which means so far as we know it
 is not possible for any type of life. That explains how it could not be made by martians. Also why and how would a
 martion build a face so big. It just does not make any since that a martian did this. Next, why it is a landform.
 There are many landforms that are weird here in America, and there is also landforms all around the whole Earth.
 Many of them look like something we can relate to like a snake a turtle a human... So if there are landforms on
 earth dont you think landforms are on mars to? Of course! why not? It\'s just unique that the landform on Mars
 looks like a human face. Also if there was martians and they were trying to get our attention dont you think we
 would have saw one by now? Finaly, why you should listen to me. You should listen to me because i am a member
 of NASA and i\'ve been dealing with all of this stuff that were talking about and people who say martians did
 this have no relation with NASA and have never worked with anything to relate to this landform. One last thing
 is that everyone working at NASA says the same thing i say, that the "face" is just a landform. To sum all this
 up the "face" on mars is a landform but others would like to beleive it\'s a martian sculpture. Which every one
 that works at NASA says it\'s a landform and they are all the ones working on the planet and taking pictures.'''

corrected_text = Diva.correct_words(text)
print(corrected_text)



