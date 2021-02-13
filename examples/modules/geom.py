import cv2

def rotate(input_, **kwargs):  
  # grab the dimensions of the image and calculate the center of the image
  (h, w, n) = input_.shape
  (cX, cY) = (w / 2, h / 2)

  # calculate rotation matrix
  angle = kwargs.get('angle', 0)
  M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
  
  # rotation calculates the cos and sin, taking absolutes of those.
  abs_cos = abs(M[0,0]) 
  abs_sin = abs(M[0,1])
  # find the new width and height bounds
  bound_w = int(h * abs_sin + w * abs_cos)
  bound_h = int(h * abs_cos + w * abs_sin)
  # subtract old image center (bringing image back to original relative position) and adding the new image center coordinates
  M[0, 2] += bound_w/2 - cX
  M[1, 2] += bound_h/2 - cY

  # rotate without a cropping
  rotated = cv2.warpAffine(input_, M, (bound_w, bound_h))

  return rotated
