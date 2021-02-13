import cv2
import numpy as np
# Basic ioperations

def crop(input_, **kwargs):

  (h, w) = input_.shape[:2]

  y0 = kwargs.get('y0', 0)
  y1 = kwargs.get('y1', h)
  x0 = kwargs.get('x0', 0)
  x1 = kwargs.get('x1', w)
  
  output_ = input_[y0:y1, x0:x1]

  return output_


def flip(input_, **kwargs):
  direction = kwargs.get('drct', 1)

  output_ = cv2.flip(input_, direction) 
  
  return output_


def mask(input_, **kwargs):
  # rectangle 0
  # circle 1
  (h, w) = input_.shape[:2]

  type = kwargs.get('type', 0)
  y0 = kwargs.get('y0', 0)
  y1 = kwargs.get('y1', h)
  x0 = kwargs.get('x0', 0)
  x1 = kwargs.get('x1', w)
  cx = kwargs.get('cx', w / 2)
  cy = kwargs.get('cy', h / 2)
  rad = kwargs.get('rad', min(h / 2, w /2))
  
  # Masking allows us to focus only on parts of an image that interest us.
  # A mask is the same size as our image, but has only two pixel values,
  # 0 and 255. Pixels with a value of 0 are ignored in the orignal image,
  # and mask pixels with a value of 255 are allowed to be kept.
  mask = np.zeros(input_.shape[:2], dtype="uint8")

  if type == 0:
    # Construct a rectangular mask
    cv2.rectangle(mask, (x0, y0), (x1, y1), 255, -1)
  else:
    # Make a circular mask
    cv2.circle(mask, (cx, cy), rad, 255, -1)

  # Apply out mask
  output_ = cv2.bitwise_and(input_, input_, mask=mask)   

  return output_



def resize(input_, **kwargs):
  return input_


def rotate(input_, **kwargs):  

  # grab the dimensions of the image and calculate the center of the image
  (h, w, n) = input_.shape
  (cx, cy) = (w / 2, h / 2)

  # calculate rotation matrix
  angle = kwargs.get('angle', 0)
  M = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)
  
  # rotation calculates the cos and sin, taking absolutes of those.
  abs_cos = abs(M[0,0]) 
  abs_sin = abs(M[0,1])
  # find the new width and height bounds
  bound_w = int(h * abs_sin + w * abs_cos)
  bound_h = int(h * abs_cos + w * abs_sin)
  # subtract old image center (bringing image back to original relative position) and adding the new image center coordinates
  M[0, 2] += bound_w/2 - cx
  M[1, 2] += bound_h/2 - cy

  # rotate without a cropping
  output_ = cv2.warpAffine(input_, M, (bound_w, bound_h))

  return output_


def translate(input_, **kwargs):
  return input_
