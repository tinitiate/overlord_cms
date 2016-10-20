# leader.py
# About:
#    Overlord CMS system for tintiate.com
#    TINITIATE.COM / VENKATA BHATTARAM (C) 2016

# CODE CHANGES
# ==============================================================================
# Date            Developer        Notes
# ==============================================================================
# May 26, 2016    Venkata B        Initial Version, Code Page parser Changes
# May 27, 2016    Venkata B        Block Reading Process start
# May 27, 2016    Venkata B        Basic (Single Multi) Block code
# Jun 02, 2016    Venkata B        Block (Single and Multi) Construction
# Jul 16, 2016    Venkata B        Created a DICT to store Single and Multi block
#                                  in the order of creation
# Aug 01, 2016    Venkata B        Formal Fixes
#
# ==============================================================================



# Reads the .config file with context and values
# Generates Folders and Files
# import overlord
from engine.PageRender import PageRender
# import time

# print()


# Generate a single code
obj_PageRender = PageRender( "python"
                            ,'d:\\code\\python\\overlord\\meta\\'
                            ,'d:\\tinitiate\\python-code\\python_overlord_test.py');

print("File is ready")

# Generate Webpage Menu Data
# Mention Language in the object creation part.
# obj_PageRender = PageRender("python", 'd:\\code\\python\\overlord\\meta\\');
# obj_PageRender.FileParser('D:\\code\\python\\python-advanced\\python-custom-decorators.py');
