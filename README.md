# TypePaste #

Pastes clipboard data to the current active window by emulating actual keypresses (using PyAutoGUI).

## Requirements ##
- Python 3
- pip
- virtualenv

## Installation ##

1. Install virtualenv and create a virutalenv in the `venv` folder:
    ```
    virtualenv venv
    ```
2. Activate virtualenv and install dependencies:
    ```
    . venv/bin/activate
    pip install -r requirements.txt
    ```
3. Edit `typepaste.applescript` and set `LOCATION` to where the main folder is found:
    ```
    do shell script "/bin/bash -s <<'EOF'
        LOCATION=~/Projects/typepaste/
        . ${LOCATION}/venv/bin/activate && ${LOCATION}/typepaste.py
    EOF"
    ```
4. Open `typepaste.applescript` in Mac OS Script Editor and in `Preferences` tick `Show script menu in menu bar`.
5. In Menu bar click `Open Scripts Folder` -> `Open User Scripts Folder` and copy `typepaste.applescript` here.

You can run TypePaste from the menu bar.
