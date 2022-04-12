import runpy
import sys

#you must set these variables

#image à watermarker
input_path=

#chemin du résultat
output_path=
#chemin du filigrane
watermark_path=

sys.argv = ['','--input='+input_path, '--output='+output_path,"--wimage="+watermark_path,"--wpos=LD","--wposm=10","--verbose"]
runpy.run_path('./watermarker.py', run_name='__main__')

