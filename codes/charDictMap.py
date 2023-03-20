#!/usr/bin/python3

import os
import sys

def make_lang_mapping(map_file,lang_list):
	mapping = {}
	fid = open(map_file,'r')
	map_data = fid.readlines()
	for i in range(1,len(lang_list)):
		mapping[lang_list[i]] = {'script-cls':{},'cls-script':{}}
	for i in range(0,len(map_data)):
		map_line = map_data[i].split('\t')
		if(len(map_line)==len(lang_list)):
			for j in range(1,len(lang_list)):
				mapping[lang_list[j]]['script-cls'][map_line[j].strip()] = map_line[0].strip()
				mapping[lang_list[j]]['cls-script'][map_line[0].strip()] = map_line[j].strip()
		else:
			sys.exit('Wrong number of mapping in Line: '+str(i))
	return mapping

def transliterate(word,mapping,inp_lang_tag,out_lang_tag):
	trans_word = []
	for letter in word:
		if(letter in mapping[inp_lang_tag]['script-cls'].keys()):
			cls_id = mapping[inp_lang_tag]['script-cls'][letter]
			trans_letter = mapping[out_lang_tag]['cls-script'][cls_id]
			if (trans_letter == '#'):
				return 0
			else:
				trans_word.append(trans_letter)
		else:
			return 0
	return "".join(trans_word)

def unified_parser(word):
	fid = open('run1.sh','w')
	fid.write('cd unified-parser; ./unified-parser "'+word+'" 1 1 0 0; cd ..')
	fid.close()
	os.system('./run1.sh')
	os.system('./run2.sh')

def main():		
	map_file = sys.argv[1]
	inp_file = sys.argv[2]
	out_file = sys.argv[3]
	inp_lang_tag = sys.argv[4]
	out_lang_tag = sys.argv[5]
	parser_flag = sys.argv[6] # unified-parser, one-to-one

	lang_list = ['ph_id','cls_id','ml','ta','te','ka','hi','be','gu','od']
	mapping = make_lang_mapping(map_file,lang_list)

	fid = open(inp_file,'r')
	inp_data = fid.readlines()
	fid.close()

	fid = open(out_file,'w')

	for i in range(0,len(inp_data)):
		inp_word = inp_data[i].strip()
		if (parser_flag == 'unified-parser'):
			unified_parser(inp_word)
			temp_fid = open('unified-parser/wordpronunciation_4_transliteration','r')
			temp_word = temp_fid.read()
			temp_fid.close()
			trans_word = transliterate(temp_word.strip(),mapping,inp_lang_tag,out_lang_tag)
			if (trans_word == 0):
				trans_word = 'No Mapping Found'
			else:
				fid.write(trans_word+'\n')
		elif (parser_flag == 'one-to-one'):
			#print(inp_word)
			trans_word = transliterate(inp_word,mapping,inp_lang_tag,out_lang_tag)
			#print(trans_word)
			if (trans_word == 0):
				trans_word = 'No Mapping Found'
			else:
				fid.write(trans_word+'\n')
		else:
			sys.exit('Parser flag wrong!!')
	fid.close()
	
# Main function
if __name__ == "__main__":
	main()
