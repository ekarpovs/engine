import cv2

def empty(**kwargs):
  return kwargs

def store(**kwargs):

  image = kwargs.get('image', None)
  ffn = kwargs.get('ffn', '')

  if image is not None:
    cv2.imwrite(ffn, image)

  return kwargs

def clean(**kwargs):
  const_keys = ['exec', 'image', 'brk', 'show']
  for key in [k for k in kwargs if k not in const_keys]: kwargs.pop(key, None)

  return kwargs

def printkwargs(**kwargs):
  [print(k, v) for k, v in kwargs.items() if k != "image"]
  
  return kwargs

