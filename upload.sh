#! /bin/bash
rm dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
cd ..
python3 -m pip install --upgrade win-cat
