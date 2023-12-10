#!/bin/bash
python3 -c "import dcpim;help(dcpim.dcpim)" > USAGE.txt
python3 dcpim/test.py
python3 setup.py sdist
twine upload dist/*
rm -rf dist
