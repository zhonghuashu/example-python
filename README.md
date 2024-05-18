example-python
=================================
# Introduction
Example python programming

# Build and test
- Install Python vscode extension
- Select Debug -> Add Configuration to add custom debug configuration (`.vscode/launch.json`).
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```
- Debug current opened file (F5)
- Run python in linux command terminal
```shell
$ cd src
# Run usage function.
$ python3 main.py

# Run unit test.
$ cd test
$ export PYTHONPATH=~/github/example-python/src:$PYTHONPATH
$ python3 test_name_function.py
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

# Run csv file test.
$ pip3 install matplotlib --user
$ phthon3 usage_csv.py

# Run json file test.
$ pip3 install plotly.express

```
# pygame
```python
$ pip3 install pygame
$ python3
>>> import pygame
>>> pygame.init()
(5, 0)
>>> pygame.display.set_mode((640, 480))

```

# matplotlib
```python
$ python3 -m pip install matplotlib --user

```