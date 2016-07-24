import re
import unicodedata

ar_word_pattern = re.compile(u'^[\u0621-\u065e\u066e-\u06d5]{2,}$')
ar_accent_pattern = re.compile(u'[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0640]')
ar_char_replacements = {
    u'\u0629': u'\u0647',
    u'\u06a9': u'\u0643',
    u'\u06af': u'\u0643',
    u'\u0623': u'\u0627',
    u'\u0624': u'\u0648',
    u'\u0625': u'\u0627',
    u'\u0622': u'\u0627',
    u'\u0649': u'\u064a',
    u'\u06cc': u'\u064a',
    u'\u0626': u'\u064a'
    }

dotless_forms = {
    u'\u0628': u'\u066e', u'\u062a': u'\u066e', u'\u062b': u'\u066e',
    u'\u062c': u'\u062d', u'\u062e': u'\u062d', u'\u0630': u'\u062f',
    u'\u0632': u'\u0631', u'\u0634': u'\u0633', u'\u0636': u'\u0635',
    u'\u0638': u'\u0637', u'\u063a': u'\u0639', u'\u0641': u'\u06a1',
    u'\u0642': u'\u066f', u'\u0646': u'\u06ba', u'\u064a': u'\u0649'}

abjad_values = {
    u'\u0627': 1, u'\u0628': 2, u'\u062c': 3, u'\u062f': 4, u'\u0647': 5,
    u'\u0648': 6, u'\u0632': 7, u'\u062d': 8, u'\u0637': 9, u'\u064a': 10,
    u'\u0643': 20, u'\u0644': 30, u'\u0645': 40, u'\u0646': 50, u'\u0633': 60,
    u'\u0639': 70, u'\u0641': 80, u'\u0635': 90, u'\u0642': 100, u'\u0631': 200,
    u'\u0634': 300, u'\u062a': 400, u'\u062b': 500, u'\u062e': 600, u'\u0630': 700,
    u'\u0636': 800, u'\u0638': 900, u'\u063a': 1000,
    u'\u0621': 1, u'\u0624': 1, u'\u0626': 1
    }

def is_arabic_word(word):
    #return if word includes only arabic letters and marks
    return ar_word_pattern.match(word) != None

def normalize(text, ignore=[]):
    #normalize an Arabic string by removing diacritics, tatweel, and normalizing character forms    
    text = ar_accent_pattern.sub('', text)
    text = u''.join([c if c in ignore else ar_char_replacements.get(c, c) for c in text])
    return text

def load_stopwords():
    #load normalized stopword list
    return set([normalize_ar(line.strip()) for line in codecs.open('ar_stopword_raw.txt', encoding='utf-8')])

def abjad_value(text):
    #teating tah marbuta equivalent to hah
    #treating hamza as only 1 regardless of the value of its seat
    #supress normalization of yah with hamza
    return sum([abjad_values.get(c, 0) for c in normalize(text, [u'\u0624', u'\u0626'])])

def remove_dots(text):
    text = u''.join([dotless_forms.get(c, c) for c in normalize(text)])
    #normalize non-final noon and yeh to \u066e
    return re.sub(ur'[\u06ba\u0649](?=[\u0621-\u065e\u066e-\u06d5])', u'\u066e', text)

def debug_char_data(text):
  for char in text:
    try:
      char = unicode(char)
      codepoint = hex(ord(char))
      name = unicodedata.name(char)
      category = unicodedata.category(char)
      print codepoint + ' "' + char + '\" ' + name + ' (' + category + ')'
    except ValueError:
      print '\"' + char + '\" cannot be interpreted'
      pass
