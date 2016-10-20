# UnitTest.py
# About:
#    This program is to be used for all unit testing of code


# Usage:
# Run from command prompt
# python UnitTest.py


# CODE CHANGES
# ==============================================================================
# Date            Developer        Notes
# ==============================================================================
# Jul 24, 2016    Venkata B        Initial Version
# Jul 26, 2016    Venkata B        Added program scalability by reading data 
#                                  from the config files

# ==============================================================================

# --- TESTING Engine/PageRender---
# from engine import PageRender
import sys
g_overlord_path = r'D:\bitnami\apache2\htdocs\overlord'

g_engine_path   = g_overlord_path + '\\engine'
g_meta_path     = g_overlord_path + '\\meta\\'


# Add engine path to the sys path
sys.path.insert(0, sys.path.insert(0, g_engine_path))


from PageRender import PageRender

# Create a PageRender Object
prUTest = PageRender("python", g_meta_path);

# Test buildBreadCrumb
# print(prUTest.buildBreadCrumb("PYTHON/STRINGS"))

    
    
print(prUTest.MenuBuilder("python", g_meta_path))

# Test headerSec
# prUTest.headerSec("Welcome", "Venkata B", "TjjhkshlHis;sHis","Venkkk")
