#!/usr/bin/env python
import os
import time
import random 
import requests
time.time()
time.time()
time.time()
time.time()
time.time()
time.time()
reciver=(int(input('enter the victim phone number :')))
text = input("Enter Message to send : ")
resp = requests.post('https://textbelt.com/text',{
			'phone' : reciver,
			'message' : text , 
			'key' : 'textbelt'
		})
		
print(resp.json())
num=(int(input('press 1 to use our new tools or press 2 for exit')))
if (num==1): 
	os.system('xdg-open https://github.com/Danish-1122')
else:
	print('thaks for using our tool')
