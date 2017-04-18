#!/usr/bin/python

import unicodedata
import time
import serial
import tweepy
from keys import keys # you need keys.py for your oauth credentials

ser = serial.Serial('/dev/cu.LightBlue-Bean', 57600)
message = ser.readline()

# Starts the twitter api and auth
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Creates the post and logs to a file
def generate_post(lst):

    output_text = (' '.join(lst))

    # Write the status to a file, for logging
    with open('txtout/words.txt', 'a') as f:
        f.write(output_text + '\n')

    return output_text
  
import sys,random,combine

# For tweeting
def sometimes(lst):
    try:
    	api.update_status(status=generate_post(lst))
    	print("posting")
    except: 
    	True
    	print("something happened")
    

#for text display
def goodInt(x):
   tmp = ''.join([i for i in x  if i.isdigit() or i=="-"])
   return int(tmp if tmp else '0')
   

def alot(n):
    message = ser.readline()              
    tmp =((message).decode())
    tmp=unicodedata.normalize('NFKD', tmp).encode('ascii','ignore')

    #print the accelerometer data
    lst = tmp.split(" ")
    #print(">",lst)
    lst = [goodInt(x) for x in lst]
    #print("<",lst)
    if not lst or len(lst) != 3:
       lst = ['0','0','0']
    
    #x-axis
    a0=["forward","spin","twist"]
    b0=["back","ply","reverse"]
    lst[0] = random.choice(a0 if lst[0]<0 else b0)
    
    #y-axis
    a1=["up","raise","zenith"]
    b1=["down","descend","nadir"]
    lst[1] = random.choice(a1 if lst[1]<0 else b1)
    
    #z-axis
    a2=["clotho","lachesis","atropos"]
    b2=["hazelnut","juliet","eli"]
    lst[2] = random.choice(a2 if lst[2]<0 else b2)
    
    #print the resulting three word string
    print(' '.join(lst))
    return lst
	
def looping(pause=8,post=60):
   b4 = time.time()
   n=1 
   lst=None
   while True:
        message = ser.readline()              
        n += 1
        now= time.time()
        if lst and n % post == 0:
        	sometimes(lst)
        if now - b4 > pause: 
           lst = alot(n)
           sys.stdout.flush()
           b4 = now

looping(pause=2,post=60)