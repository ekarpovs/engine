import cv2
import numpy as np
# Basic ioperations

def crop(**kwargs):

  (h, w) = kwargs['image'].shape[:2]

  y0 = kwargs.get('y0', 0)
  y1 = kwargs.get('y1', h)
  x0 = kwargs.get('x0', 0)
  x1 = kwargs.get('x1', w)

  kwargs['image'] = kwargs['image'][y0:y1, x0:x1]

  return kwargs


def flip(**kwargs):
  direction = kwargs.get('drct', 1)

  kwargs['image'] = cv2.flip(kwargs['image'], direction) 
  
  return kwargs


def mask(**kwargs):
  # rectangle 0
  # circle 1
  (h, w) = kwargs['image'].shape[:2]

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
  mask = np.zeros(kwargs['image'].shape[:2], dtype="uint8")

  if type == 0:
    # Construct a rectangular mask
    cv2.rectangle(mask, (x0, y0), (x1, y1), 255, -1)
  else:
    # Make a circular mask
    cv2.circle(mask, (cx, cy), rad, 255, -1)

  # Apply out mask
  kwargs['image'] = cv2.bitwise_and(kwargs['image'], kwargs['image'], mask=mask)   

  return kwargs



def resize(**kwargs):
  """
  # interpolation methods
	# cv2.INTER_NEAREST
	# cv2.INTER_LINEAR
	# cv2.INTER_AREA
	# cv2.INTER_CUBIC
	# cv2.INTER_LANCZOS4
  # units
  pixel 0
  percent 1
  # rectangle side
  height 0
  width 1
  """
  (h, w) = kwargs['image'].shape[:2]

  method = kwargs.get('meth', cv2.INTER_AREA)
  unit = kwargs.get('unit', 0)
  side = kwargs.get('side', 0)

  #  default value regarding to the side of a rectangle
  def_size = w
  if side == 0:
    def_size = h
  size = kwargs.get('size', def_size)
  if unit == 1:
    # size defined in percents - calculate in pixels
    orig_pixels = w
    if side == 1:
      orig_pixels = h

    size = int((orig_pixels / 100) * size)
  
  #  the ratio of the new image to the old image, regarding to the side of a rectangle
  ratio = size / w
  dim = (size, int(h * ratio))
  if side == 0:
    ratio = size / h
    dim = (int(w * ratio), size)

  kwargs['image'] = cv2.resize(kwargs['image'], dim, interpolation=method) 

  return kwargs


def rotate(**kwargs):  

  # grab the dimensions of the image and calculate the center of the image
  (h, w, n) = kwargs['image'].shape
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
  kwargs['image'] = cv2.warpAffine(kwargs['image'], M, (bound_w, bound_h))

  return kwargs


# Translating (shifting) an image is given by a NumPy matrix in
# the form:
#	[[1, 0, shiftX], [0, 1, shiftY]] 
def translate(**kwargs):

  shiftX = kwargs.get('x', 0)
  shiftY = kwargs.get('y', 0)

  if shiftX == 0 and shiftY == 0:
    return kwargs

  M = np.float32([[1, 0, shiftX], [0, 1, shiftY]])
  kwargs['image'] = cv2.warpAffine(kwargs['image'], M, (kwargs['image'].shape[1], kwargs['image'].shape[0])) 

  return kwargs
