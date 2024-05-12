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
cd src
python3 main.py
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