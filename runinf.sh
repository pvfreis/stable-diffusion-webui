#!/bin/bash

# Run webui.sh in the background
./webui.sh -f 

# Wait 5 minutes to let the service start
sleep 300

# Run the Python script
python3 test-api.py
echo "Inference ran successfully."

