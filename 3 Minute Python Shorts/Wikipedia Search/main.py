# Search Wikipedia Using python

# installing required module
# fetching article summary
# limiting article sentences
# changing article language

# pip install wikipedia

import wikipedia

wikipedia.set_lang('hi')
result = wikipedia.summary('India', sentences=2)
print(result)