import runpy
import sys

sys.argv = ['','--input='+path, '--output='+w_path,"--wimage=./media/filigranes/"+id_img+".jpg","--wpos=LD","--wposm=10","--verbose"]
runpy.run_path('./watermarkingApp/utils/watermarker.py', run_name='__main__')

