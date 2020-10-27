#! /bin/bash
# Bash Script to download large google drive files with wget

FILE_ID="1yPWiPyOmIpVFdqU41ENRYD_tY6Nvsuw1"
FILE_NAME="export.pkl"

echo "Downloading Google drive file $FILE_ID as $FILE_NAME..."

CONFIRM=$(wget --quiet --save-cookies /tmp/cookies.txt \
--keep-session-cookies --no-check-certificate \
'https://docs.google.com/uc?export=download&id='$FILE_ID -O- \
| sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')

wget --no-check-certificate --load-cookies /tmp/cookies.txt \
"https://docs.google.com/uc?export=download&confirm="$CONFIRM"&id="$FILE_ID \
-O $FILE_NAME \
&& rm -rf /tmp/cookies.txt
