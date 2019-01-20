import markovify
import sys
import random
r=random.random

with open("txtin/x-down.txt") as f:
    txta1 = f.read()
    
with open("txtin/x-up.txt") as f:
    txta2 = f.read()
    
with open("txtin/y-down.txt") as f:
    txtb1 = f.read()

with open("txtin/y-up.txt") as f:
    txtb2 = f.read()
        
with open("txtin/z-down.txt") as f:
    txtc1 = f.read()
    
with open("txtin/z-up.txt") as f:
    txtc2 = f.read()
 
def norm(x) : return (x - -512)/ (512 - -512)

def combo(x,y,z):
  txta = txta1 if x < 0 else txta2
  txtb = txtb1 if y < 0 else txtb2
  txtc = txtc1 if z < 0 else txtc2

  model_a = markovify.Text(txta)
  model_b = markovify.Text(txtb)
  model_c = markovify.Text(txtc)
  model_combo = markovify.combine([ model_a, model_b, model_c ], [ 1, 1, 1 ])
  
  sentence = model_combo.make_short_sentence(140)
  print sentence
  return sentence

#while True:
   #x = -512 + r() * (512 - -512)
   #y = -512 + r() * (512 - -512)
   #z = -512 + r() * (512 - -512)
   #combo(x,y,z)
   #raw_input()