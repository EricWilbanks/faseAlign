#!/bin/bash

# Overwrite old file with new
if mv "/usr/local/bin/bpm-update-2016-summer.tmp" "/usr/local/bin/bpm-update-2016-summer"; then
  echo 'Done. Update of "/usr/local/bin/bpm-update-2016-summer" complete.'
else
  echo 'Failed to update "/usr/local/bin/bpm-update-2016-summer"!'
fi
# Remove overwrite_bpm-update.sh and return to specified directory.
rm $0
cd "$1"
