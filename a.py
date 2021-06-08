#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random 
import requests
reciver=(int(input('enter the victim phone number :')))
text = input("Enter Message to send : ")
resp = requests.post('https://textbelt.com/text',{
			'phone' : reciver,
			'message' : text ,
			'key' : 'textbelt'
		})
		
print(resp.json())
os.system('xdg-open https://github.com/Danish-1122')

