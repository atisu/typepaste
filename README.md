# TypePaste #

Pastes clipboard data into the current active window by emulating actual keypresses (using PyAutoGUI).

Assumes US Keyboard layout.

## Requirements ##
- Python 3 (for typepaste.py, base32e.py)
- Python 2 (for base32d.py -- target environment assumed to have older Python)
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
    Repeat for `typepaste-base32.applescript`, `typepaste-base32-lowercase.applescript`.
    You can also increase the number of characters printed at once via adjusting `--batch-size 10`.

4. Open `typepaste.applescript` in Mac OS Script Editor and in `Preferences` tick `Show script menu in menu bar`.
5. In Menu bar click `Open Scripts Folder` -> `Open User Scripts Folder` and copy `typepaste.applescript`, `typepaste-base32.applescript` and `typepaste-base32-lowercase.applescript` there.

You can run TypePaste from the menu bar.

## Methods for transferring files ##

### Copy file contents ###

1. Copy file contents to clipboard.
2. Use the `typepaste-base32.applescript` or if you are a bit more paranoid the `typepaste-base32-lowercase.applescript` script to paste the data as base32 encoded string.
3. Use the provided `base32d.py` or any other base32 decoder to decode the contents. For other decoders make sure all characters are uppercase and remove white space.

### Copy multiple files ###

1. Create an archive (e.g., tar.gz).
2. Base32 encode the archive, e.g., by using the provided `base32e.py`.
3. Use split to split the files, e.g., `split -b 2000 files.tar.gz.b32`.
4. Copy contents to clipboard, e.g., `cat xaa | pbcopy`.
5. Use `typepaste.applescript` to copy to the end of an open file at the destination.
6. Repeat for all parts (e.g., `xaa`, `xab`, `xac`,...).
7. Base32 decode the resulting file (e.g., with the provided `base32d.py`).
8. Extract the archive.

## Troubleshooting ##

1. Check target content for invalid characters:

```
cat files.tar.gz.b32| sed 's/[0-9A-Z=]//g'
```
