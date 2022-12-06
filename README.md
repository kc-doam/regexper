## Install on Ubuntu 22.04

``` sh
pip install --user pyqt5
sudo apt install python3-pyqt5 pyqt5-dev-tools qtcreator
# Test
pyuic5
# Error: one input ui-file must be specified
```


### Hotkeys `qt-designer`

|Key|Action
|:--|:--
|<kbd>Ctrl</kbd>+<kbd>R</kbd>|Preview
|<kbd>Ctrl</kbd>+<kbd>2</kbd>|Lay out vertically

### Convert ui to qt.py

``` sh
pyuic5 -x regexper/ui/mainwindow.ui -o regexper/mainwindow.py
```

### Run

``` sh
python3 run.py
```


## Convert to exe

``` sh
python3 -m pip install --upgrade pip

~/.local/bin/pyinstaller --onefile run.py
```

## Manual Links

* https://tproger.ru/translations/python-gui-pyqt/
* https://python-scripts.com/pyqt5
