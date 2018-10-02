do shell script "/bin/bash -s <<'EOF'

LOCATION=~/Projects/typepaste/
. ${LOCATION}/venv/bin/activate && ${LOCATION}/typepaste.py --batch-size 10 --base32-encode

EOF"