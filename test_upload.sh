#! /bin/bash
rm dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
cd ..
python3 -m pip install --index-url https://test.pypi.org/simple/ --upgrade win-cat
