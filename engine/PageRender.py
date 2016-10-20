# PageRender.py
# About:
#    This program generates the HTML file of the code


# Usage:
#


# CODE CHANGES
# ==============================================================================
# Date            Developer        Notes
# ==============================================================================
# Jul 19, 2016    Venkata B        Initial Version
# Jul 24, 2016    Venkata B        BreadCrumb logic
# Aug 01, 2016    Venkata B        Formal Fixes
# Aug 13, 2016    Venkata B        Calls for all Page Items for Page Render
#

# ==============================================================================
from engine.CodeFileParser import CodeFileParser as cpa
from engine.PageBuilder    import PageBuilder    as pgb
import configparser                              as cfp
import os


# Inherit the CodeFileParser and MenuRender
class PageRender(cpa, pgb):

    # Actual render webpage
    g_web_page                 = "";

    # Host 
    # Get Language Render Stuff
    g_host_name                = ""
    g_home_icon                = ""

    # language Specific Data
    g_language_name            = ""
    g_lang_config_file         = ""
    g_lang_icon                = ""    
    g_theme_background_color   = ""
    g_theme_text_color         = ""
    g_languages                = ["python"]
    g_index_file               = ""
    
    g_root_code_gen_folder     = ""
    g_lang_code_folder         = ""

    # Menu Variables

    def __init__(self, p_language, p_meta_path, p_code_file_path_name):

        # Sanitise Inputs for Data Case Immunity
        # Change all to lower case
        l_language           = p_language.lower()
        self.g_language_name = p_language


        # Get the config data for the 
        self.ConfigData = cfp.ConfigParser()
        self.ConfigData.read(p_meta_path + "overlord.config")


        # Get host name for all URL usage
        self.g_host_name        = self.ConfigData['HOST']['hostname']
        self.g_home_icon        = self.ConfigData['CODE-PAGE']['home_icon']
        self.g_stg_folder_name  = self.ConfigData['HOST']['stg_folder_name']


        # Get language speecific data from the config files
        self.g_language_name    = l_language
        self.g_lang_config_file = p_meta_path + l_language + ".config"
        

        # print(self.g_lang_config_file)
        # Read Language specific data
        self.LangConfigData = cfp.ConfigParser()
        self.LangConfigData.read(self.g_lang_config_file)

        
        self.g_index_file             = self.LangConfigData['INDEXFILE']['index_file']

        self.g_lang_icon              = self.LangConfigData['WEB_FILE_GENERATION']['icon']
        self.g_course_type            = self.LangConfigData['WEB_FILE_GENERATION']['course_type']
        self.g_theme_background_color = self.LangConfigData['WEB_FILE_GENERATION']['theme_background_color']
        self.g_theme_text_color       = self.LangConfigData['WEB_FILE_GENERATION']['theme_text_color']


        self.stg_web_folder_name       = self.LangConfigData['STG_FILE_DIR_SETTINGS']['stg_web_folder_name']
        self.stg_code_folder           = self.LangConfigData['STG_FILE_DIR_SETTINGS']['stg_code_folder']
        self.stg_images_folder         = self.LangConfigData['STG_FILE_DIR_SETTINGS']['stg_images_folder']

        # Parse the file
        cpa.FileParser(self, p_code_file_path_name);

        # Pass the Page Web Data Element List to the Render Program
        self.folderBuilder()
        self.buildGoverner(cpa.g_page_block_data_list)



    # Create Folders and Files
    def folderBuilder(self):

        # Create all folders as per the config file
        # Root folder for all website data
        # print(self.g_stg_folder_name)
        # print(self.g_stg_folder_name + self.stg_web_folder_name)
        # print(self.g_stg_folder_name + self.stg_code_folder)
        # print(self.g_stg_folder_name + self.stg_images_folder)


        if not os.path.exists(self.g_stg_folder_name):
            os.makedirs(self.g_stg_folder_name)

        # Language specific folders
        # Staging Folder for webpages
        if not os.path.exists(self.g_stg_folder_name + self.stg_web_folder_name):
            os.makedirs(self.g_stg_folder_name + self.stg_web_folder_name)

        # Staging folder for Code    
        if not os.path.exists(self.g_stg_folder_name + self.stg_code_folder):
            os.makedirs(self.g_stg_folder_name + self.stg_code_folder)

        # Staging folder for images
        if not os.path.exists(self.g_stg_folder_name + self.stg_images_folder):
            os.makedirs(self.g_stg_folder_name + self.stg_images_folder)



    def buildGoverner(self, p_page_block_data_list):

        # Create the PageBuilder object
        pgBuildObj      = pgb()
        l_final_page    = ""

        l_author        = ""
        l_file_name     = ""
        l_author_filename_data = ""


        # Group Function Calls acrosss code blocks
        # BreadCrumbs
        l_breadcrumbs     = ""
        l_breadcrumb_data = ""

        # Header Parameters
        lrv_header      = 0   # Target is 3
        l_title         = ""
        l_desc          = ""
        l_keywords      = ""

        # Code Notes Parameters
        lrv_code_notes  = 0
        l_code_title    = ""
        l_code_notes    = ""

        # Code Block Parameters
        lrv_code_block  = 0
        l_code          = ""
        l_language      = ""

        # Points
        lrv_points      = 0


        # Code Output Parameters
        lrv_code_output = 0
        l_code_output   = ""

        lrv_tags_block  = 0
        l_tags          = ""

        lrv_cons_block  = 0
        l_cons          = ""

        lrv_pros_block  = 0
        l_pros          = ""


        # Loop Thru the List of page item data list
        # print(p_page_block_data_list)

        # for j in p_page_block_data_list:
        #    print(j[0])



        for i in p_page_block_data_list:

            # ==============
            # HEADER BUILDER
            # ==============
            # Check for all HEADER conditions here
            if i[0] ==  '>>TITLE - ': 
                l_title    = i[1]
                lrv_header += 1

            elif i[0] == '>>DESC<<': 
                l_desc     = i[1]
                lrv_header += 1

            elif i[0] == '>>KEYWORDS<<':
                l_keywords = i[1]
                lrv_header += 1

            elif i[0] == '>>AUTHOR - ':
                l_author = i[1]
                lrv_header += 1

            elif i[0] == '>>FILE-NAME - ':
                l_file_name = i[1]
                lrv_header += 1

            elif i[0] == '>>BREADCRUMB - ':
                l_breadcrumbs     = i[1]
                l_breadcrumb_data = pgBuildObj.buildBreadCrumb(l_breadcrumbs, self.g_home_icon, self.g_host_name, self.g_lang_icon)
                lrv_header       += 1


            # Build Header Block
            if lrv_header == 6:

                # 
                l_author_filename_data = pgBuildObj.authorFilename(l_author, l_file_name)
                l_topic_header         = pgBuildObj.TopicHeader(self.g_theme_background_color, l_title)
                l_side_bar             = pgBuildObj.SideMenuBuilder(self.g_language_name, self.g_index_file, self.g_host_name)


                # print(pgBuildObj.headerSec(l_title, l_desc, l_keywords, l_author) + pgBuildObj.StaticTopMenu())
                l_final_page +=  pgBuildObj.headerSec( l_title
                                                      ,l_desc
                                                      ,l_keywords
                                                      ,l_author
                                                      ,self.g_lang_icon
                                                      ,self.g_theme_background_color
                                                      ,self.g_theme_text_color
                                                      ,l_side_bar
                                                      ,self.g_language_name
                                                      ,l_breadcrumb_data
                                                      ,l_topic_header
                                                      ,l_author_filename_data)           

                # l_final_page +=  pgBuildObj.jTron(self.g_lang_icon, l_title, self.g_theme_background_color, self.g_theme_text_color)
                l_final_page +=  pgBuildObj.StaticTopMenu()

                lrv_header    =  0    
                # print(l_final_page)


            # ================
            # BREADCRUMB BLOCK
            # ================    
            # Build Header Block
            # if i[0] ==  '>>BREADCRUMB - ':
            #    l_breadcrumbs  =  i[1]
            #    l_final_page  +=  "\n" + pgBuildObj.buildBreadCrumb(l_breadcrumbs, self.g_home_icon, self.g_host_name, self.g_lang_icon)


            # ================
            # POINTS BLOCK
            # ================    
            # Build Points Block
            if i[0] ==  '>>POINTS<<':
                l_points   =  i[1]
                lrv_points += 1

            if lrv_points == 1:
                l_final_page  +=  "\n" + pgBuildObj.pageBlog(self.g_lang_icon, l_title, l_points)
                lrv_points = 0


            # ================
            # CODE NOTES BLOCK
            # ================
            # Code Blog Builder
            if i[0] ==  '>>CODE-TITLE - ':
                lrv_code_notes += 1
                l_code_title    = i[1]

            elif i[0] == '>>CODE-NOTES<<':
                lrv_code_notes += 1
                l_code_notes    = i[1]

            # Build Code Notes Block
            if lrv_code_notes == 2:
                # print(pgBuildObj.CodeBlog(l_code_title, l_code_notes, l_author))
                # l_final_page   +=  "\n" + pgBuildObj.CodeBlog(l_code_title, l_code_notes, l_author)
                l_final_page   +=  "\n" + pgBuildObj.CodeBlog(self.g_lang_icon, l_code_title, l_code_notes, l_keywords, l_author)
                lrv_code_notes  =  0
                # print(l_final_page)




            # ==========
            # CODE BLOCK
            # ==========
            # Code Builder
            if i[0] ==  '>>CODE-ALL-OS<<': 
                lrv_code_block += 1
                l_code          = i[1]

            if lrv_code_block == 1:
                # print(pgBuildObj.CodeBlock(self.g_language_name, l_code))
                l_final_page   +=  "\n" + pgBuildObj.CodeBlock(self.g_language_name, l_code)
                lrv_code_block  =  0


            # =================
            # CODE OUTPUT BLOCK
            # =================
            # Code Output Builder
            if i[0] ==  '>>OUTPUT<<': 
                lrv_code_output += 1
                l_code_output    = i[1]

            if lrv_code_output == 1:
                # print(pgBuildObj.CodeOutput(l_code_output))
                l_final_page    +=  "\n" + pgBuildObj.CodeOutput(l_code_output) + "<br><br>"
                lrv_code_output  =  0


            # ==========
            # TAGS BLOCK
            # ==========
            # Tags Builder
            if i[0] ==  '>>TAGS - ': 
                lrv_tags_block += 1
                l_tags          = i[1]

            if lrv_tags_block == 1:
                l_final_page   +=  "\n" + pgBuildObj.PageTags(l_tags)
                lrv_tags_block  =  0


            # ==========
            # CONS BLOCK
            # ==========
            # Cons Builder
            if i[0] ==  '>>CONS<<': 
                lrv_cons_block += 1
                l_cons          = i[1]

            if lrv_cons_block == 1:
                l_final_page   +=  "\n" + pgBuildObj.CodeCons(l_cons)
                lrv_cons_block  =  0


            # ==========
            # PROS BLOCK
            # ==========
            # Pro Builder
            if i[0] ==  '>>PROS<<': 
                lrv_pros_block += 1
                l_pros          = i[1]

            if lrv_pros_block == 1:
                l_final_page   +=  "\n" + pgBuildObj.CodePros(l_pros)
                lrv_pros_block  = 0    


        # Print the final page output
        l_final_page += pgBuildObj.footerSec()
        
        # Working with the final rendered page
        # print(l_final_page)
        
        # Write the web file data, with the generated filename
        l_web_file_name = l_title.replace(" ","-")
        fObj = open(self.g_stg_folder_name + self.stg_web_folder_name + l_web_file_name+'.html', "w")
        fObj.write(l_final_page);
        fObj.close()
