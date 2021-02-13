# Usage:
#   python driver.py -f <worksheet name> -i <input file name> 
# 

import cv2
import argparse
import sys
import random
from lib import readJson

import modules

# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="WorkShop")
  ap.add_argument("-f", "--flow", required = True,
	help = "name of a worksheet without extension.")
  ap.add_argument("-i", "--input", required = True,
	help = "path to the input file(s)")
  ap.add_argument("-o", "--output", required = False,
	help = "path to the output file(s)")
  
  args = ap.parse_args()   
  kwargs = dict((k,v) for k,v in vars(args).items() if k!="message_type")
  
  return kwargs

# Read configuration file
def readConfig():
  paths = readJson('./config.json')

  images_path = paths['images']
  worksheets_path = paths['worksheets']
  modules_path = paths['modules']
  results_path = paths['results']

  return images_path, worksheets_path, modules_path, results_path


# Set paths for the module loader
def setModulesPath(mpath):
  # the engine's local collection
  sys.path.append('./modules')
  # external collection
  sys.path.append(mpath)


def showDecorator(executor):
  def executorWrapper(input_, **kwargs):
    cv2.imshow("before", input_)
    cv2.waitKey(0)

    output_ = executor(input_, **kwargs)
    
    cv2.imshow("after", output_)
    cv2.waitKey(0)
        
    return output_

  return executorWrapper


# A break point decorator
def brkDecorator(executor):
  def executorWrapper(input_, **kwargs):
    prompt = "parameter {}: "
    cv2.imshow("before", input_)
    cv2.waitKey(0)
    while True:
      print("breakpoint")
      output_ = executor(input_, **kwargs)
      cv2.imshow("after", output_)
      key = cv2.waitKey(0) & 0xFF    
      if key == ord("q"):
        print("break point - quit")
        break
      cv2.destroyWindow('after')
      for key, value in kwargs.items():
        if key != 'exec' and key != 'brk':
          print(key, value)
          # TODO: implement input of new values for parameters
        
    return output_

  return executorWrapper

# Flow runner with steps input/output pipe
def runFlow(input_, flow):  
  for step in flow:
    # run the current step and pass the output to the input for the next one (pipe it)
    brk = step.get('brk', None)
    show = step.get('show', None)
    if brk is not None:
      print("tuning break point is defined", step['exec'])
      # before running, wrapp the step executor
      input_ = brkDecorator(step['exec'])(input_, **step)
    elif show is not None:
      print("show break point is defined", step['exec'])
      # before running, wrapp the step executor
      input_ = showDecorator(step['exec'])(input_, **step)   
    else:
      input_ = step['exec'](input_, **step)

  return input_


# Flow builder
def buildFlow(worksheet_file_name):
  # get the flow worksheet
  steps = readJson(worksheet_file_name)["steps"]

  flow = []
  for step in steps:  
    step['exec'] = modules.get(step['exec'])
    flow.append(step)  

  return flow



# Main function
def main(**kwargs): 

  images_path, worksheets_path, modules_path, results_path = readConfig()

  setModulesPath(modules_path)

  worksheet_file_name = "{}/{}.json".format(worksheets_path, kwargs['flow'])
  flow = buildFlow(worksheet_file_name)

  # get input and run the flow 
  image_file_name = "{}/{}".format(images_path, kwargs["input"])
  image = cv2.imread(image_file_name)
  print("The image will be processed", image_file_name)

  result = runFlow(image, flow)

  result_file = "{}/result-{}".format(results_path, kwargs["input"])
  print("Result saved to", result_file)
  cv2.imwrite(result_file, result)

  cv2.destroyAllWindows()


# Entry point
if __name__ == "__main__":
    kwargs = parseArgs()
    main(**kwargs) 
