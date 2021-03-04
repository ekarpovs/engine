import os, types
from importlib import import_module

def get(module_name):
  func_name = ''
  try:
    if '.' in module_name:
        module_name, func_name = module_name.rsplit('.', 1)
    else:
        module_name = module_name

    module = import_module(module_name, package=__name__)
    executor = getattr(module, func_name)

  except (AttributeError, ModuleNotFoundError):
    raise ImportError('{} is not part of our modules collection!'.format(module_name))

  return executor

def list(dir_path):
  # dir_path = os.path.dirname(os.path.abspath(__file__))
  files_in_dir = [f[:-3] for f in os.listdir(dir_path)
                  if f.endswith('.py') and f != '__init__.py']
  mods = {}
  for f in files_in_dir:
    mod = import_module(f, package=__name__)
    funcs = []
    for key, value in mod.__dict__.items():
      if type(value) is types.FunctionType:
        fnname = value.__name__
        if fnname[0] != '_': # private functions
          funcs.append(value)
    mods[mod] = funcs

  return mods