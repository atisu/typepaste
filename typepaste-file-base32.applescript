set myFile to (choose file with prompt "Please select a file:")

display dialog "After clicking Continue, please make the target window active. There is a 3 seconds delay before starting to paste.

You can abort pasting anytime by moving the mouse pointer to the upper left corner of the screen.
" buttons {"Continue"} default button 1

delay 3

do shell script "/bin/bash -s <<'EOF'
MYFILE=$(echo '/Volumes/" & myFile & "' | sed -e 's/:/\\//g')
LOCATION=~/Projects/typepaste/
. ${LOCATION}/venv/bin/activate && ${LOCATION}/typepaste.py --batch-size 250 --base32-encode --lowercase --source-file \"${MYFILE}\"
EOF"
