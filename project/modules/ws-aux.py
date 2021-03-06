'''
Local module, contains common utility operations
'''
import cv2

import sys
import types

def empty(**kwargs):
  '''
  It is an operation's implementation boilerplate.

  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs as is.
  '''  

  return kwargs

def store(**kwargs):
  '''
  Stores an image into a file.
  
  Keyword arguments:
  - image: an image that will be stored;
  - ffn: full file name, where the image will be stored.
  
  Returns:
  - the kwargs as is.
  '''  

  image = kwargs.get('image', None)
  ffn = kwargs.get('ffn', '')

  if image is not None:
    cv2.imwrite(ffn, image)

  return kwargs


def restore(**kwargs):
  '''
  Restores an image from a file.
  
  Keyword arguments:
  - ffn: full file name, where from the image will be restored.
  
  Returns:
  - the image.
  '''  

  ffn = kwargs.get('ffn', '')

  kwargs['image'] = cv2.imread(ffn)

  return kwargs


def clean(**kwargs):
  '''
  Cleans kwargs dictionary from items.
  
  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs with only 'exec', 'image', 'brk' and 'show' items.
  '''  

  const_keys = ['exec', 'image', 'brk', 'show']
  for key in [k for k in kwargs if k not in const_keys]: kwargs.pop(key, None)

  return kwargs

def printkwargs(**kwargs):
  '''
  Prints kwargs.

  Keyword arguments:
  - image: an image that will be returned

  Returns:
  - the kwargs as is.
  '''

  [print(k, v) for k, v in kwargs.items() if k != "image"]
  
  return kwargs

