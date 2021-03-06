import sys, os
import argparse
# import markdown

from lib import readJson
import modules


# Construct the argument parser and parse the arguments
def parseArgs():
  ap = argparse.ArgumentParser(description="WorkShop")
  ap.add_argument("-o", "--output", required = False,
  default='../../data/tmp/1.md',
	help = "path to the output file(s)")
  
  args = ap.parse_args()   
  kwargs = dict((k,v) for k,v in vars(args).items() if k!="message_type")
  
  return kwargs


def trim(docstring):
  if not docstring:
      return ''
  # Convert tabs to spaces (following the normal Python rules)
  # and split into a list of lines:
  lines = docstring.expandtabs().splitlines()
  # Determine minimum indentation (first line doesn't count):
  maxint = 4
  indent = maxint
  for line in lines[1:]:
      stripped = line.lstrip()
      if stripped:
          indent = min(indent, len(line) - len(stripped))
  # Remove indentation (first line is special):
  trimmed = [lines[0].strip()]
  if indent < maxint:
      for line in lines[1:]:
          trimmed.append(line[indent:].rstrip())
  # Strip off trailing and leading blank lines:
  while trimmed and not trimmed[-1]:
      trimmed.pop()
  while trimmed and not trimmed[0]:
      trimmed.pop(0)
  # Return a single string:
  return '\n'.join(trimmed)


def make_doc(path):
  doc = []
  doc.append("# WorkSheet: {}\n".format(path))
  mods = modules.list(path)
  for mod, funcs in mods.items():
    # print("Module:", mod.__name__, mod.__doc__)
    doc.append("## Module: {}".format(mod.__name__))
    doc.append("{}\n".format(mod.__doc__))
    for func in funcs:
      # print("Function:", func.__name__, func.__doc__) 
      doc.append("### Function: {}".format(func.__name__))
      doc.append("{}\n\n".format(func.__doc__))

  return doc

def make_md(doc):
  # htmlmarkdown = markdown.markdown(doc)

  return 


def store_doc(ffn, doc):
  with open(ffn, "w") as outfile: 
    for line in doc:
      outfile.write(line)

  return

# Main function
def main(**kwargs): 
  paths = readJson('./config.json')

  # local collection
  lpath = paths['local']
  sys.path.append(lpath)

  # external collection
  mpath = paths['modules']
  sys.path.append(mpath)
 
  doc = make_doc(lpath)
  doc += make_doc(mpath)

  store_doc(kwargs['output'], doc)

  # htmlmarkdown = make_md(doc)
 
  return

# Entry point
if __name__ == "__main__":
  # kwargs = parseArgs()
  kwargs = parseArgs()
  main(**kwargs) 
