import os
from sys import sys, platform

from System import System

# Make sure we are on a linux platform, otherwise exit
if not System.check_if_linux(platform):
    print("ERROR: Must be on a linux platform!")
    sys.exit(1)