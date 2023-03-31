#!/bin/bash

# Replace 'your_script.sh' with the name of your .sh file

temp_file="output.txt"
success_pattern="127.0.0.1"

./webui.sh -f 2>&1 | tee "$temp_file"
output=$(cat "$temp_file")
rm "$temp_file"

# Replace 'success_pattern' with a string or pattern that indicates success in the output


if echo "$output" | grep -q "$success_pattern"; then
    echo "Service enabled."
    # Replace 'your_python_script.py' with the name of your Python script
    python3 test-api.py
    echo "Inference ran successfully."
else
    echo "Script did not run successfully."
fi