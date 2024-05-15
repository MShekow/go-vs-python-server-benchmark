#!/bin/bash

if [[ $NUITKA -eq 1 ]]; then
    echo "Running with Nuitka"
    ./main.bin
else
    python main.py
fi
