#!/usr/bin/python3

import os
import sys
import re

from indic_text_transliteration import transliteration

re_num = re.compile('^[0-9]+$')
re_en = re.compile('^[a-zA-Z]+$')
re_bn = re.compile('^[\u0980-\u09FF]+$')
re_hi = re.compile('^[\u0900-\u097F]+$')
re_kn = re.compile('^[\u0C80-\u0CFF]+$')
re_ml = re.compile('^[\u0D00-\u0D7F]+$')
re_or = re.compile('^[\u0B00-\u0B7F]+$')
re_pa = re.compile('^[\u0A00-\u0A7F]+$')
re_ta = re.compile('^[\u0B80-\u0BFF]+$')
re_te = re.compile('^[\u0C00-\u0C7F]+$')

re_numi = re.compile('[0-9]')
re_eni = re.compile('[a-zA-Z]')
re_bni = re.compile('[\u0980-\u09FF]')
re_hii = re.compile('[\u0900-\u097F]')
re_kni = re.compile('[\u0C80-\u0CFF]')
re_mli = re.compile('[\u0D00-\u0D7F]')
re_ori = re.compile('[\u0B00-\u0B7F]')
re_pai = re.compile('[\u0A00-\u0A7F]')
re_tai = re.compile('[\u0B80-\u0BFF]')
re_tei = re.compile('[\u0C00-\u0C7F]')

re_bnij = re.compile('([0-9]+|[A-Za-z]+|[\u0980-\u09FF]+)')
re_hiij = re.compile('([0-9]+|[A-Za-z]+|[\u0900-\u097F]+)')
re_knij = re.compile('([0-9]+|[A-Za-z]+|[\u0C80-\u0CFF]+)')
re_mlij = re.compile('([0-9]+|[A-Za-z]+|[\u0D00-\u0D7F]+)')
re_orij = re.compile('([0-9]+|[A-Za-z]+|[\u0B00-\u0B7F]+)')
re_paij = re.compile('([0-9]+|[A-Za-z]+|[\u0A00-\u0A7F]+)')
re_taij = re.compile('([0-9]+|[A-Za-z]+|[\u0B80-\u0BFF]+)')
re_teij = re.compile('([0-9]+|[A-Za-z]+|[\u0C00-\u0C7F]+)')

def only_has(string,check):
	if (check == 'num'):
		res = re_num.search(string)
	elif (check == 'en'):
		res = re_en.search(string)
	elif (check == 'bn'):
		res = re_bn.search(string)
	elif (check == 'hi' or check == 'mr'):
		res = re_hi.search(string)
	elif (check == 'kn'):
		res = re_kn.search(string)
	elif (check == 'ml'):
		res = re_ml.search(string)
	elif (check == 'or'):
		res = re_or.search(string)
	elif (check == 'pa'):
		res = re_pa.search(string)
	elif (check == 'ta'):
		res = re_ta.search(string)
	elif (check == 'te'):
		res = re_te.search(string)
	else:
		sys.exit('Language not supported')
	return res is not None

def also_has(string,check):
	if (check == 'num'):
		res = re_numi.search(string)
	elif (check == 'en'):
		res = re_eni.search(string)
	elif (check == 'bn'):
		res = re_bni.search(string)
	elif (check == 'hi' or check == 'mr'):
		res = re_hii.search(string)
	elif (check == 'kn'):
		res = re_kni.search(string)
	elif (check == 'ml'):
		res = re_mli.search(string)
	elif (check == 'or'):
		res = re_ori.search(string)
	elif (check == 'pa'):
		res = re_pai.search(string)
	elif (check == 'ta'):
		res = re_tai.search(string)
	elif (check == 'te'):
		res = re_tei.search(string)
	else:
		sys.exit('Language not supported')
	return res is not None

# Main function
def main():
	input_dict_file = sys.argv[1]
	output_dict_file = sys.argv[2]

	# en/bn/hi/kn/ml/mr/or/pa/ta/te

	input_lang_tag = sys.argv[3]
	output_lang_tag = sys.argv[4]

	fid = open(input_dict_file,'r')
	glos = fid.readlines()
	fid.close()

	fid = open(output_dict_file,'w')

	for i in range(0,len(glos)):
		word = glos[i].split('\t')
		fid.write(word[0]+'\t'+transliteration(word[0],'word',output_lang_tag)+'\n')
	
	fid.close()

# Main function
if __name__ == "__main__":
	main()

