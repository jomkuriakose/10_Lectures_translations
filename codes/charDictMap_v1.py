#!/usr/bin/python3

import os
import sys
glos = {}

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
	#print(word)
	fid = open('run1.sh', 'w', encoding='utf8')
	fid.write('cd unified-parser; rm wordpronunciation; rm wordpronunciation_4_transliteration; ./unified-parser "'+word+'" 1 1 0 0; cd ..')
	fid.close()
	os.system('./run1.sh')
	os.system('./run2.sh')

def transliteration_wrapper(inp_word,mapping,inp_lang_tag,out_lang_tag,parser_flag):
	if (parser_flag == 'unified-parser'):
		unified_parser(inp_word)
		temp_fid = open('unified-parser/wordpronunciation_4_transliteration','r')
		temp_word = temp_fid.read()
		temp_fid.close()
		trans_word = transliterate(temp_word.strip(),mapping,inp_lang_tag,out_lang_tag)
		if not trans_word:
			trans_word = '-----'
		return(trans_word)
	elif (parser_flag == 'one-to-one'):
		trans_word = transliterate(inp_word,mapping,inp_lang_tag,out_lang_tag)
		if not trans_word:
			trans_word = '-----'
		return(trans_word)
	else:
		sys.exit('Parser flag wrong!!')

def add_glos(sub_word, map_word):
	global glos
	if sub_word in glos.keys():
		if not (map_word in glos[sub_word]):
			glos[sub_word].append(map_word)
	else:
		glos[sub_word] = [map_word];

def main():
	global glos
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

	for i in range(0,len(inp_data)):
		inp_line = inp_data[i].strip().split('\t')
		inp_words = inp_line[1].strip().split(' ')
		if len(inp_words) > 1:
			trans_words = []
			for j in range(0,len(inp_words)):
				inp_word = inp_words[j].strip()
				trans_word = transliteration_wrapper(inp_word,mapping,inp_lang_tag,out_lang_tag,parser_flag)
				trans_words.append(trans_word)
			add_glos(inp_line[0], ' '.join(trans_words))
		else:
			inp_word = ''.join(inp_words)
			trans_word = transliteration_wrapper(inp_word,mapping,inp_lang_tag,out_lang_tag,parser_flag)
			add_glos(inp_line[0],trans_word)
	
	fid = open(out_file,'w')
	for key in glos:
		fid.write(str(key)+"\t"+str(", ".join(glos[key])+"\n"))
	fid.close()
	
# Main function
if __name__ == "__main__":
	main()
