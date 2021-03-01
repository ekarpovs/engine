# Image Processing Workshop Engine

## Documentation

### The Engine File system structure

_____
    | 
    |__ /engine/
    |    |
         |__ /doc/
         |     |
         |     |__ README.md - this file
         |
         |__ /examples/
         |     |__ /modules/
         |     |     |
         |     |     |__ geom.py - an module and an opration example
         |     |
         |     |__ /worsheets/
         |           |
         |           |__ demo.json - a worksheet example
         |
         |__ /project/    
         |      |__ /lib/ __ various utilites
                |    |
                |    |__ fsut.py - file system operations 
                |    
                |__ /modules/ __ modules and operations loader, varios common operations for usage in a flow
                |    |
                |    |__ __init__.py - the 'modules' package declaration, and operations loader
                |    |
                |    |__ ws-aux.py - module provides common operations
                |
                |__ driver.py __ main script for run different flows (worksheets)
                |
                |__ config.json __ data for setup the engine working environment
                |
                |__ .gitignore __ Git ignore patterns
                |
                |__ requirements.txt __ versioning requirements
                |
                |__ README.md __ Breaf descriptions
                |
                |__ LICENSE __ MIT License
                |

### Setup (config) the engine environment

Edit the config.json file from the root ('project') folder, regarding real modules, worksheets and images locations
```yaml
{
  "modules": "<external path>/modules",
  "worksheets": "<external path>/worksheets",
  "images": "<external path>",
  "results": "<external path>",
}
```

### Add a new module

Implement a new python script inside an external 'module' folder, with at least one function, regarding the template
```yaml
import cv2

def <function_name>(**kwargs):  
  # 1. parse kwards

  # 2. do something with the input image

  # 3. assign the result to kwargs['xxx'] and

  return kwargs
```

### Add a new operation

Add a new fuction, regarding the above pattern, into an existing module script

### Compose new batch flow (worksheet)

Create a new json file, inside an external 'worksheets' folder, regarding the pattern
```yaml

{
  "steps":[ 
    {"exec": "<module name>.<operatoion name>"[, "brk": <number>] [, "parameter name": "parameter value", ...]},
    ...
    {"exec": "<module name>.<operatoion name>"[, "parameter name": "parameter value", ...]},
  ]
}
```
