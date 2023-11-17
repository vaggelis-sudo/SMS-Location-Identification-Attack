#"Copyright Notice and Disclaimer. 
#© NORHEASTERN UNIVERSITY 2023 SW-24013 used with permission. All rights reserved."

#!/bin/bash

# Define the path to your interpreter
PYTHON_PATH="/usr/bin/python3"

# Define the path to your script
SCRIPT_PATH="/path/to/your/script.py"

# Define the arguments to pass to the script
DEVICE_STRING="your_device_code"
PHONE_NUM="receiver's_phone_number"
ITERATIONS="number_of_iterations"

# Check if the script exists
if [ -f "$SCRIPT_PATH" ]; then
    # Execute the script with the arguments
    $PYTHON_PATH $SCRIPT_PATH $DEVICE_STRING $PHONE_NUM $ITERATIONS
else
    echo "Error: Script not found at $SCRIPT_PATH"
    exit 1
fi
