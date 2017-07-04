#!/usr/bin/python
# loop-over-files.py
# Created Tue Jul  4 09:56:46 AKDT 2017
# Copyright (C) 2017 by Raymond E. Marcil <marcilr@gmail.com>
#
# Loop over files in current working dirctory
# and print filenames.
#
import os
indir = '.'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        print(f)
