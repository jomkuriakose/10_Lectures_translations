#!/usr/bin/python3

import os
import sys
import re
import argparse

glos = {};

# Print comment header
def code_head_print():
	code_head_str='Compare transcription file and transcription_sub file and make dictionary file in other languages.\n\n'
	code_head_str+='Author: Jom Kuriakose\n'
	code_head_str+='email: jom@cse.iitm.ac.in\n'
	code_head_str+='Date: 13/12/2021\n\n'
	return code_head_str

# Print example command
def ex_cmd_print():
	ex_cmd_str='\nExample: python3 getDictFromSubFile_v2.py -i <input-file> -s <input-sub-file> -o <output-file>\n'
	return ex_cmd_str

# Parse arguments and print details
def parse_args():
	parser = argparse.ArgumentParser(description=code_head_print()+ex_cmd_print(),formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-i','--inp', help='Input file', required=True)
	parser.add_argument('-s','--sub', help='Input Sub file', required=True)
	parser.add_argument('-o','--out', help='Output file\n\n', required=True)
	args = parser.parse_args()
	return args

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

def add_glos(sub_word, map_word):
	global glos
	if sub_word in glos.keys():
		if not (map_word in glos[sub_word]):
			glos[sub_word].append(map_word)
	else:
		glos[sub_word] = [map_word];

def make_glos_equal(sub_lines, inp_lines):
	global glos
	for j in range(0,len(inp_lines)):
		inp_line = inp_lines[j].strip()
		sub_line = sub_lines[j].strip()
		if(also_has(sub_line,'en') or also_has(sub_line,'num')):
			add_glos(sub_line, inp_line)

def make_glos_not_equal(sub_lines, inp_lines):
	global glos
	#print(sub_lines)
	#print(inp_lines)
	min_len = min(len(sub_lines),len(inp_lines))
	if min_len == 0:
		#print(glos)
		return 0
	if (sub_lines[0].strip() == inp_lines[0].strip()):
		make_glos_not_equal(sub_lines[1:len(sub_lines)], inp_lines[1:len(inp_lines)])
	else:
		if(also_has(sub_lines[0],'en') or also_has(sub_lines[0],'num')):
			glos_words = []
			map_words = []
			j_flag = 0
			k_flag = 0
			for j in range(0,len(sub_lines)):
				if(also_has(sub_lines[j],'en') or also_has(sub_lines[j],'num')):
					glos_words.append(sub_lines[j])
				else:
					glos_word = ' '.join(glos_words)
					j_flag = 1
					break
			#print(glos_word)
			#print(sub_lines[j])
			for k in range(0,len(inp_lines)):
				if (sub_lines[j] != inp_lines[k]):
					map_words.append(inp_lines[k])
				else:
					map_word = ' '.join(map_words)
					add_glos(glos_word, map_word)
					k_flag = 1
					break
			#print(map_word)
			#print(inp_lines[k])
			if j_flag == 1:
				j_flag = 0
				sub_data = sub_lines[j:len(sub_lines)]
			else:
				sub_data = sub_lines[j+1:len(sub_lines)]
			if k_flag == 1:
				k_flag = 0
				inp_data = inp_lines[k:len(inp_lines)]
			else:
				inp_data = inp_lines[k+1:len(inp_lines)]
			make_glos_not_equal(sub_data, inp_data)
		else:
			print(inp_lines)
			print(sub_lines)
			sys.exit('Error!!')

# Main function
def main():
	global glos

	args = parse_args()
	inp = args.inp
	sub = args.sub
	out = args.out

	inp_file = open(inp,'r');
	inp_data = inp_file.readlines()
	inp_file.close()
	sub_file = open(sub,'r');
	sub_data = sub_file.readlines()
	sub_file.close()

	if (len(inp_data) == len(sub_data)):
		for i in range(0,len(inp_data)):
			if(also_has(sub_data[i],'en') or also_has(sub_data[i],'num')):
				inp_lines = inp_data[i].split(' ')
				sub_lines = sub_data[i].split(' ')
				if (len(inp_lines) == len(sub_lines)):
					make_glos_equal(sub_lines, inp_lines)
				else:
					make_glos_not_equal(sub_lines, inp_lines)
	else:
		sys.exit('Mismatch of number of lines in file.')
	
	out_file = open(out,'w')
	for key in glos:
		out_file.write(str(key)+"\t"+str(", ".join(glos[key])+"\n"))
	out_file.close()

	print('\nDone!!')

# Main function
if __name__ == "__main__":
	main()


