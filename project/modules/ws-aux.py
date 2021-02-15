import cv2

def empty(**kwargs):
  return kwargs

def store(**kwargs):

  image = kwargs.get('image', None)
  ffn = kwargs.get('ffn', '')

  if image is not None:
    cv2.imwrite(ffn, image)

  return kwargs
