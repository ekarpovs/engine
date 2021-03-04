import sys, os
import markdown


from lib import readJson
import modules


def make_doc(path):
  doc = []
  mods = modules.list(path)
  for mod, funcs in mods.items():
    # print("Module:", mod.__name__, mod.__doc__)
    doc.append("Module: {}".format(mod.__name__))
    doc.append("{}{}".format(mod.__doc__, '\n'))
    for func in funcs:
      # print("Function:", func.__name__, func.__doc__) 
      doc.append("Function: {}".format(func.__name__))
      doc.append("{}{}".format(func.__doc__, '\n'))

  return doc

def make_md(doc):
  # htmlmarkdown = markdown.markdown(doc)

  return 


def store_doc(doc):
  with open('../../data/tmp/1.md', "w") as outfile: 
    for line in doc:
      outfile.write(line)

  return

# Main function
def main(**kwargs): 
  paths = readJson('./config.json')
  # the engine's local collection
  lpath = paths['local']
  sys.path.append(lpath)

  mpath = paths['modules']
  # external collection
  sys.path.append(mpath)
 
  doc = make_doc(lpath)
  # doc = make_doc(mpath)
  store_doc(doc)

  # htmlmarkdown = make_md(doc)
 
  return

# Entry point
if __name__ == "__main__":
  # kwargs = parseArgs()
  kwargs = {}
  main(**kwargs) 
