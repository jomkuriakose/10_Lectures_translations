#!/usr/bin/python3

import os
import sys
import re
import argparse

# Print comment header
def code_head_print():
	code_head_str='Compare transcription file and transcription_sub file and make dictionary file in other languages.\n\n'
	code_head_str+='Author: Jom Kuriakose\n'
	code_head_str+='email: jom@cse.iitm.ac.in\n'
	code_head_str+='Date: 13/12/2021\n\n'
	return code_head_str

# Print example command
def ex_cmd_print():
	ex_cmd_str='\nExample: python3 getDictFromSubFile.py -i <input-file> -s <input-sub-file> -o <output-file>\n'
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

# Main function
def main():
	args = parse_args()
	inp = args.inp
	sub = args.sub
	out = args.out
	glos = {};

	inp_file = open(inp,'r');
	inp_data = inp_file.readlines()
	inp_file.close()
	sub_file = open(sub,'r');
	sub_data = sub_file.readlines()
	sub_file.close()

	if (len(inp_data) == len(sub_data)):
		for i in range(0,len(inp_data)):
			inp_lines = inp_data[i].split(' ')
			sub_lines = sub_data[i].split(' ')
			if (len(inp_lines) == len(sub_lines)):
				for j in range(0,len(inp_lines)):
					inp_line = inp_lines[j].strip()
					sub_line = sub_lines[j].strip()
					if(also_has(sub_line,'en') or also_has(sub_line,'num')):
						if(only_has(sub_line,'en') or only_has(sub_line,'num')):
							if sub_line in glos.keys():
								if not (inp_line in glos[sub_line]):
									glos[sub_line].append(inp_line)
							else:
								glos[sub_line] = [inp_line];
						else:
							print("\nCheck word '"+sub_line+"' in line no: "+str(i)+" and add to dictionary, if not already present")
			else:
				if(also_has(sub_data[i],'en') or also_has(sub_data[i],'num')):
					print('\nWord Number Mismatch!! Check line number '+str(i+1)+' and add English words to dictionary, if not already present')
					print('Inp File (Line No.'+str(i+1)+'): '+inp_data[i].strip())
					print('Sub File (Line No.'+str(i+1)+'): '+sub_data[i].strip())
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


