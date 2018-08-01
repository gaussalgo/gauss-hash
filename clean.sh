#!/bin/bash

rm -rf gauss_hash.egg-info
rm -rf .cache .coverage htmlcov
find -type d -name '__pycache__' | xargs rm -fr
find -type f -name '*.pyc' | xargs rm -f
