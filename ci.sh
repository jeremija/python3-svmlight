#!/bin/bash
set -e

rm -rf env
python3 -m venv env
./env/bin/python3 setup.py install
./env/bin/python3 examples/simple.py
