#!/usr/bin/env python
import os
import time
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

