string=`cut -d"'" -f2 unified-parser/wordpronunciation | sed 's/ //g' | sed 's/(//g' | sed 's/)//g' | sed 's/0//g' | sed 's/"//g'`
echo $string > unified-parser/wordpronunciation_4_transliteration
