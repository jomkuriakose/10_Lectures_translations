import pysrt
import sys
txtfile = sys.argv[1]
srtfile = sys.argv[2]
outfile = sys.argv[3]
subs = pysrt.open(srtfile)
i = open(txtfile,'r')
f = open(outfile,'w')
text = i.readlines()
if (len(subs) != len(text)):
	sys.exit("Number of lines not matching!! Exit!!")
for sub_idx in len(subs):
    subs[sub_idx].text = text[sub_idx]
	subs.save(outfile, encoding='utf-8')
