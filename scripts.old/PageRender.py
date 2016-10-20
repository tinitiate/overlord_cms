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

# ==============================================================================
import CodeFileParser
import configparser as cfp

#
class PageRender:


    # Actual render webpage
    g_web_page                 = "";

    g_overlord_config_path     = "D:\\bitnami\\apache2\\htdocs\\overlord\\meta\\overlord.config";
    # Get Language Render Stuff
    g_icon                     = ""
    g_home_icon                = ""
    g_theme_background_color   = ""
    g_theme_text_color         = ""
    g_host_name                = ""
    

    g_languages = {"PYTHON":"SCRIPTING-LANGUAGE", "PERL":"SCRIPTING-LANGUAGE", "LUA":"SCRIPTING-LANGUAGE", "RUBY":"SCRIPTING-LANGUAGE",
    "JAVA":"PROGRAMMING-LANGUAGE", "CS":"PROGRAMMING-LANGUAGE", "CPP":"PROGRAMMING-LANGUAGE", "SCALA":"PROGRAMMING-LANGUAGE",
    "ORACLE":"DATABASE", "MYSQL":"DATABASE", "POSTGRESQL":"DATABASE", "MS SQL SERVER":"DATABASE"}

    
    def __init__(self):
        self.ConfigData = cfp.ConfigParser()
        self.ConfigData.read(self.g_overlord_config_path)

    
        # Get host name for all URL usage
        self.g_host_name = self.ConfigData['HOST']['hostname']
        self.g_icon      = self.ConfigData['PYTHON']['icon']
        self.g_home_icon   = self.ConfigData['HOST']['home_icon']
    
    # Convert Space to HTML &nbsp;
    def Space2NBSP(self, i_data):
        return i_data.replace("","&nbsp;")


    # This will be  the
    def mainPage(self):

        return 1;

    
    # Get the Config Details    
    def getLanguageDetails(self, p_cfg_obj, p_lang):
        
        self.g_icon                     = p_cfg_obj[p_lang]['icon']
        self.g_theme_background_color   = p_cfg_obj[p_lang]['theme_background_color']
        self.g_theme_text_color         = p_cfg_obj[p_lang]['theme_text_color']



    # Function to Generate the BreadCrumb
    def buildBreadCrumb(self, p_breadcrumb):

        l_breadcrumb_str = ""
        l_stg_str        = ""
        l_url            = ""
        
        
        # BreadCrumb Stuff
        C_BREADCRUMB_TEMPLATE    = """                        <!-- BreadCrumb Start -->
                        <ol itemscope itemtype="http://schema.org/BreadcrumbList" class="breadcrumb">
__INNER_CONTENT__
                        </ol>
                        <!-- BreadCrumb End -->"""


        C_BREADCRUMB_LINK_ITEM   = """                            <li itemprop="itemListElement" itemscope
                                itemtype="http://schema.org/ListItem">
                                    <a itemprop="item" href="__LINK__">
                                        <span itemprop="name">__ICON__ __LABEL__</span>
                                         <span itemprop="position" content="__NUM__"></span>
                                    </a>
                            </li>"""


        # generate the Home Link
        l_home_link = (C_BREADCRUMB_LINK_ITEM.replace('__LABEL__','HOME')).replace("__ICON__",self.g_home_icon)
        l_home_link = (l_home_link.replace('__LINK__',self.g_host_name)).replace("__NUM__","1")


        # Generate the BreadCrumb String
        l_breadcrumb_str = l_breadcrumb_str+l_home_link


        # print(l_home_link)

        C_BREADCRUMB_ACTIVE_ITEM = """                            <li itemprop="itemListElement" itemscope
                                itemtype="http://schema.org/ListItem">
                                    <span itemprop="name">__LABEL__</span>
                                       <span itemprop="position" content="__NUM__"></span>
                            </li>"""

        #  Build the URL string
        l_url = l_url + self.g_host_name
        
        # Seperator Character
        bCrumbList = p_breadcrumb.split("/")
        


        l_ctr = 1
        for l_item in bCrumbList:
            
            l_ctr = l_ctr+1
            
            if (bCrumbList[-1] != l_item):
                l_url = l_url + "/" + l_item.lower()
                l_stg_str = C_BREADCRUMB_LINK_ITEM.replace('__LABEL__',l_item)
                l_stg_str = (l_stg_str.replace('__LINK__',l_url)).replace("__NUM__",str(l_ctr))
                
                if (l_item in self.g_languages):
                    l_stg_str = l_stg_str.replace("__ICON__",self.g_icon)
                else:
                    l_stg_str = l_stg_str.replace("__ICON__","")

                l_breadcrumb_str = l_breadcrumb_str + l_stg_str
                
            else:
                l_breadcrumb_str = l_breadcrumb_str + (C_BREADCRUMB_ACTIVE_ITEM.replace("__LABEL__",l_item.upper())).replace("__NUM__",str(l_ctr))
                # l_breadcrumb_str = l_breadcrumb_str + C_BREADCRUMB_ACTIVE_ITEM.replace("__LABEL__",l_item.upper())

        l_breadcrumb_str = C_BREADCRUMB_TEMPLATE.replace("__INNER_CONTENT__",l_breadcrumb_str)
       
        # print(l_breadcrumb_str)
        return l_breadcrumb_str
    # BreadCrumb Generator Function END     

3 Unit Testing Script
# --- TESTING ---
lobb = PageRender();

# lobb.buildBreadCrumb("PYTHON/STRINGS")
# lobb.headerSec("Welcome", "Venkata B", "TjjhkshlHis;sHis","Venkkk")


