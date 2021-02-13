from importlib import import_module

def get(module_name):
  func_name = ''
  try:
    if '.' in module_name:
        module_name, func_name = module_name.rsplit('.', 1)
    else:
        module_name = module_name

    module = import_module(module_name, package='modules')
    executor = getattr(module, func_name)

  except (AttributeError, ModuleNotFoundError):
    raise ImportError('{} is not part of our modules collection!'.format(module_name))

  return executor
