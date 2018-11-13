# TypePaste #

Pastes clipboard data into the current active window by emulating actual keypresses (using PyAutoGUI).

Assumes US Keyboard layout.

## Requirements ##
- Python 3 (for typepaste.py, base32e.py)
- Python 2 (for base32lcd.py -- target environment assumed to have older Python)
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
    Repeat for `*.applescript`.
    You can also increase the number of characters printed at once via adjusting `--batch-size 10`.

4. Open `typepaste.applescript` in Mac OS Script Editor and in `Preferences` tick `Show script menu in menu bar`.
5. In Menu bar click `Open Scripts Folder` -> `Open User Scripts Folder` and copy `*.applescript` there.

You can run TypePaste from the menu bar.

## FAILSAFE ##

Move mouse cursor to top left corner of the screen to abort typepasting.

## Methods for transferring files ##

### A.) Use `typepaste-file-base32.applescript`

For larger files you might want to split the file into smaller chunks (see B. and C.).

1. Open a text editor with a new empty file.
2. Start the script. It opens a file selector window to pick a file. Pick a file.
3. Next it displays a dialog that after clicking continue it will wait for 3 seconds, so you have time to make the window active you want to paste. Click continue.
4. Make the window active you want to paste to.
5. _FAILSAFE_: Remember, moving the mouse pointer to the upper left corner of the screen will terminate pasting.
6. Save the file and quit the editor.
7. Use `base32lcd.py` (or its content, main part is 2 lines, plus 2 lines of imports) to decode the file.

### B.) Copy file contents ###

1. Copy file contents to clipboard.
2. Use the `typepaste-base32.applescript` or if you are a bit more paranoid the `typepaste-base32-lowercase.applescript` script to paste the data as base32 encoded string.
3. Use the provided `base32lcd.py` or any other base32 decoder to decode the contents. For other decoders make sure all characters are uppercase and remove white space.

### C.) Copy multiple files ###

1. Create an archive (e.g., tar.gz).
2. Base32 encode the archive, e.g., by using the provided `base32e.py`.
3. Use split to split the files, e.g., `split -b 2000 files.tar.gz.b32`.
4. Copy contents to clipboard, e.g., `cat xaa | pbcopy`.
5. Use `typepaste.applescript` to copy to the end of an open file at the destination.
6. Repeat for all parts (e.g., `xaa`, `xab`, `xac`,...).
7. Base32 decode the resulting file (e.g., with the provided `base32lcd.py`).
8. Extract the archive.

## Troubleshooting ##

1. Check target content for invalid characters:

   ```
   cat files.tar.gz.b32 | sed 's/[0-9A-Z=]//g'
   ```

   or if the file was created with lowercased data:

   ```
   cat files.tar.gz.b32 | sed 's/[0-9a-z=]//g'
   ```


