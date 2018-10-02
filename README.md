# TypePaste #

Pastes clipboard data into the current active window by emulating actual keypresses (using PyAutoGUI).

Assumes US Keyboard layout.

## Requirements ##
- Python 3
- pip
- virtualenv

## Installation ##

0. Clone the repository.
1. Create a virutalenv named `venv` in the folder:
    ```
    virtualenv venv
    ```
2. Activate virtualenv and install dependencies:
    ```
    . venv/bin/activate
    pip install -r requirements.txt
    ```
3. Edit `typepaste.applescript` and set `LOCATION` to where the TypePaste repo was checked out:
    ```
    do shell script "/bin/bash -s <<'EOF'
        LOCATION=~/Projects/typepaste/
        . ${LOCATION}/venv/bin/activate && ${LOCATION}/typepaste.py --batch-size 10
    EOF"
    ```

    You can also increase the number of characters printed once via adjusting `--batch-size 10`.

4. Open `typepaste.applescript` in Mac OS Script Editor and in `Preferences` tick `Show script menu in menu bar`.
5. In Menu bar click `Open Scripts Folder` -> `Open User Scripts Folder` and copy `typepaste.applescript` here.

You can run TypePaste from the menu bar.
