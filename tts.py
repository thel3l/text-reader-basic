import pycurl
import json 
import os
from StringIO import StringIO

ble = "python pdf2txt.py -o /root/Desktop/5.txt /root/Desktop/5.pdf"
#hard-coded file names. Adapt them to your requirements.
os.system(ble)

ble2 = "python realtts.py > 5.ogg"
os.system(ble2)
