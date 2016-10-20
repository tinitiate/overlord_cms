# overlord.py
# About:
#    This program calls the config files and generates the data code and webpages
#    as per the context (first 5 characters) of the index file


# Usage:
#    overlord.py <.config filename>


# CODE CHANGES
# ===================================================================================
# Date            Developer        Notes
# ===================================================================================
# Apr 07, 2016    Venkata B        Initial version
# Apr 10, 2016    Venkata B        Handling exceptions, Changes to config file.

# ===================================================================================

# All imports
import sys
import configparser
#import stageProcessor
#import liveProcessor


# Global Variables to handle config data
# Initialize the variables for reference
g_index_file          = ""

g_stg_web_folder      = ""
g_stg_code_folder     = ""
g_stg_images_folder   = ""

g_live_web_folder     = ""
g_live_code_folder    = ""
g_live_images_folder  = ""


# This function reads all the vital data from config.
def overlord():
    # read the arguments to run the program
    l_config_filename = sys.argv[1];
    
    
    # Exceptions for missing vital config data
    class missing_index_file_exception(Exception):pass
    
    class missing_stg_web_folder_exception(Exception):pass
    class missing_stg_code_folder_exception(Exception):pass
    class missing_stg_images_folder_exception(Exception):pass
    
    class missing_live_web_folder_exception(Exception):pass
    class missing_live_code_folder_exception(Exception):pass
    class missing_live_images_folder_exception(Exception):pass
    
    
    # Read Contents from file
    ConfigData = configparser.ConfigParser()
    ConfigData.read(l_config_filename)
    
    
    # Check all vital config parameters of the config file that is being read.
    # Raise exceptions as found
    
    # Check Index File
    try:
        if ConfigData['INDEXFILE']['index_file'] == "":
            raise missing_index_file_exception
        else:
            # Assign value to global var
            g_index_file = ConfigData['INDEXFILE']['index_file']
    except missing_index_file_exception:
        print("Index file is missing !!")
        
    
    # Check Staging Data Vitals
    try:
        if ConfigData['STG_FILE_DIR_SETTINGS']['stg_web_folder'] == "":
            raise  missing_stg_web_folder_exception
        else:
            # Assign value to global var
            g_stg_web_folder = ConfigData['STG_FILE_DIR_SETTINGS']['stg_web_folder']
    except missing_stg_web_folder_exception:
        print("stg_web_folder is missing !!")
    
    try:
        if ConfigData['STG_FILE_DIR_SETTINGS']['stg_code_folder'] == "":
            raise missing_stg_code_folder_exception
        else:
            # Assign value to global var
            g_stg_code_folder = ConfigData['STG_FILE_DIR_SETTINGS']['stg_code_folder']
    except missing_stg_code_folder_exception:
        print("stg_code_folder is missing !!")

    try:
        if ConfigData['STG_FILE_DIR_SETTINGS']['stg_images_folder'] == "":
            raise missing_stg_images_folder_exception
        else:
            # Assign value to global var
            g_stg_images_folder = ConfigData['STG_FILE_DIR_SETTINGS']['stg_images_folder']
    except missing_stg_images_folder_exception:
        print("stg_images_folder is missing !!")


    # Check Live Data Vitals
    try:
        if ConfigData['LIVE_FILE_DIR_SETTINGS']['live_web_folder'] == "":
            raise missing_live_web_folder_exception
        else:
            # Assign value to global var
            g_live_web_folder = ConfigData['LIVE_FILE_DIR_SETTINGS']['live_web_folder']
    except missing_live_web_folder_exception:
        print("live_web_folder is missing !!")
    
    try:
        if ConfigData['LIVE_FILE_DIR_SETTINGS']['live_code_folder'] == "":
            raise missing_live_code_folder_exception
        else:
            # Assign value to global var
            g_live_code_folder = ConfigData['LIVE_FILE_DIR_SETTINGS']['live_code_folder']
    except missing_live_code_folder_exception:
        print("live_code_folder is missing !!")
    
    try:
        if ConfigData['INDEXFILE']['live_images_folder'] == "":
            raise missing_live_images_folder_exception
        else:
            # Assign value to global var
            g_live_images_folder = ConfigData['LIVE_FILE_DIR_SETTINGS']['live_images_folder']
    except missing_live_images_folder_exception:
        print("live_images_folder is missing !!")



# This Function Parses the index file to generate the Coce Template files and Web Index Files`
def indexFileParser(p_indexFileNamePath ):
    l_title
    pass



def test():
    print("hello")

# Run Code Start
# overlord()
