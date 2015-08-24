import pycurl
import json 
import os
from StringIO import StringIO

with open ("5.txt", "r") as myfile:
    readfile=myfile.readlines()

string = ''.join(readfile)

data = json.dumps({"text":string})
c = pycurl.Curl()
c.setopt(pycurl.URL, "https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize")
c.setopt(pycurl.HTTPHEADER, ['Content-type: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.USERPWD, "username:password") 
c.setopt(pycurl.POSTFIELDS, data)
c.perform()
