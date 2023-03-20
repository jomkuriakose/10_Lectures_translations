#!/usr/bin/python3
  
# Transliteration of English to Indian languages
# Author: Jom Kuriakose
# email: jom@cse.iitm.ac.in
# Date: 12/11/2021

# Import packages
import os
import sys
import argparse
from google.transliteration import transliterate_word
from google.transliteration import transliterate_text
from google.transliteration import transliterate_numerals
from langdetect import detect

# Print comment header
def code_head_print():
    code_head_str='Transliteration of English to Indian languages\n\n'
    code_head_str+='Author: Jom Kuriakose\n'
    code_head_str+='email: jom@cse.iitm.ac.in\n'
    code_head_str+='Date: 12/11/2021\n\n'
    return code_head_str

# Print example command
def ex_cmd_print():
    ex_cmd_str='\nExample: python indic_text_transliteration.py -i <input-word/s> -t <word/text/num> -l <language_tag>\n'
    return ex_cmd_str

# Parse arguments and print details
def parse_args():
    parser = argparse.ArgumentParser(description=code_head_print()+ex_cmd_print(),formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i','--inp', help='Input word/text/numeral', required=True)
    parser.add_argument('-t','--typ', help='Input type (word/text/num)', required=True)
    parser.add_argument('-l','--lang', help='Language tag (bn/hi/kn/ml/mr/or/pa/ta/te)\n\n', required=True)
    args = parser.parse_args()
    return args

# Check if input is English
def check_input(inp):
	if (detect(inp) != 'en'):
		sys.exit('Input language not English')

# Check if language tag is valid and in list of supported languages
# https://github.com/narVidhai/Google-Transliterate-API/blob/master/Languages.md
def check_lang(lang_tag):
	lang_tag_list = ['bn','hi','kn','ml','mr','or','pa','ta','te']
	if lang_tag not in lang_tag_list:
		sys.exit('Language not supported')

# Transliteration function
def transliteration(inp, typ, lang_tag):
	#check_input(inp) # Not working properly for words. Assuming all inputs are English.
	check_lang(lang_tag)
	if (typ == 'word'):
		out = transliterate_word(inp, lang_code=lang_tag)
		if not out:
			print(inp)
			return('-----')
		elif isinstance(out, list):
			return out[0]
		elif out=='':
			print(inp)
			return('-----')
		else:
			return out
	elif (typ == 'text'):
		out = transliterate_text(inp, lang_code=lang_tag)
		if not out:
			print(inp)
			return('-----')
		elif isinstance(out, list):
			return out[0]
		elif out=='':
			print(inp)
			return('-----')
		else:
			return out
	elif (typ == 'num'):
		out = transliterate_numerals(inp, lang_code=lang_tag)
		return out
	else:
		sys.exit('Input type wrong')

# Main function
def main():
	args = parse_args()
	inp = args.inp
	typ = args.typ
	lang_tag = args.lang
	out = transliteration(inp, typ, lang_tag)
	print(out)

# Main function
if __name__ == "__main__":
	main()
