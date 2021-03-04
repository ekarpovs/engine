'''
Local module, contains common utilites
'''
import cv2

import sys
import types

def empty(**kwargs):
  '''
  It is an operation's implementation boilerplate.
  Gets kwargs, do nothing and returns the kwargs as is.
  '''  

  return kwargs

def store(**kwargs):
  '''
  Stores an image into file.
  Gets via kwargs: 
    - image that will be stored;
    - full file name, where the image will be stored
  Returns the kwargs as is.
  '''  

  image = kwargs.get('image', None)
  ffn = kwargs.get('ffn', '')

  if image is not None:
    cv2.imwrite(ffn, image)

  return kwargs

def clean(**kwargs):
  '''
  Cleans kwargs dictionary from items.
  Returns the kwargs with only 'exec', 'image', 'brk' and 'show' items.
  '''  

  const_keys = ['exec', 'image', 'brk', 'show']
  for key in [k for k in kwargs if k not in const_keys]: kwargs.pop(key, None)

  return kwargs

def printkwargs(**kwargs):
  '''
  Prints  kwargs and returns the kwargs as is.
  '''  
  [print(k, v) for k, v in kwargs.items() if k != "image"]
  
  return kwargs

