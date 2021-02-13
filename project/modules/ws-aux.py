import cv2

def empty(input_, **kwargs):
  return input_

def store(input_, **kwargs):
  ffn = kwargs.get('ffn', '')
  cv2.imwrite(ffn, input_)

  return input_
