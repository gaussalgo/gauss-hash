#!/bin/bash

python -m pytest --cov=gauss_hash
coverage report -m
# coverage html && xdg-open htmlcov/index.html > /dev/null  2>&1

