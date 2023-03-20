import pysrt
import sys
srtfile = sys.argv[1]
outfile = sys.argv[2]
subs = pysrt.open(srtfile)
f = open(outfile,'w')
for sub in subs:
	#print(sub.text)
    f.write(sub.text+'\n')
