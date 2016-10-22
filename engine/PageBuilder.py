# PageBuilder.py
# About:
#    This program Builds the HTML components for the Code page

# Usage:
#

# CODE CHANGES
# ==============================================================================
# Date            Developer        Notes
# ==============================================================================
# Aug 01, 2016    Venkata B        Initial Version
# Aug 07, 2016    Venkata B        Code Block Builder
# Aug 09, 2016    Venkata B        Modular changes to builder

# ==============================================================================
import time

class PageBuilder:

    g_list_languages = ['PYTHON']

    # Fixed Code Content
    def StaticTopMenu(self):
        
        return """            <!-- Navbar Start -->
            <div class="navbar navbar-inverse navbar-fixed-top">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    </button>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                    <!-- TopBar Content Start -->
                    <li class="active"><a href="#">TINITIATE.COM</a></li>
                    <li><a href="#"><i class="fa fa-database"></i> DATABASES</a></li>
                    <li><a href="#about"><i class="fa fa-code"></i> PROGRAMMING LANGUAGES</a></li>
                    <li><a href="#contact"><i class="fa fa-terminal"></i> SCRIPTING LANGUAGES</a></li>
                    <li><a href="#contact"><i class="fa fa-laptop"></i> WEB PROGRAMMING</a></li>
                    <!-- TopBar Content End -->
                    </ul>
                </div>
            </div>
            <!-- Navbar End -->""";



    # Function to display page blog
    def pageBlog(self, p_lang_icon, p_page_title, p_page_notes):
        
        # return """                        <div class=\"panel panel-info\" style=\"margin-bottom: 2px;\">
        #                    <div class=\"panel-heading panel-heading-sm\">&nbsp;&nbsp;""" + p_lang_icon + """&nbsp;&nbsp; """ + p_page_title + """</div>
        #                    <div class=\"panel-body panel-body-sm\"><pre>""" + p_page_notes + """</pre></div>
        #                </div>"""

        return """                        <div class=\"panel panel-info\" style=\"margin-bottom: 2px;\">
                            <div class=\"panel-heading panel-heading-sm\">&nbsp;&nbsp;""" + p_lang_icon + """&nbsp;&nbsp; """ + p_page_title + """</div>
                            <pre style=\"background-color:white; border:0px\">""" + p_page_notes + """</pre>
                        </div><br>"""


    # Function to Generate the BreadCrumb
    def buildBreadCrumb(self, p_breadcrumb, p_home_icon, p_host_name, p_lang_icon):

        l_breadcrumb         = p_breadcrumb.lower()
        
        l_breadcrumb_str     = ""
        l_stg_str            = ""
        l_url                = ""
    
        
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
        l_home_link = (C_BREADCRUMB_LINK_ITEM.replace('__LABEL__','HOME')).replace("__ICON__",p_home_icon)
        l_home_link = (l_home_link.replace('__LINK__',p_host_name)).replace("__NUM__","1")


        # Generate the BreadCrumb String
        l_breadcrumb_str = l_breadcrumb_str+l_home_link


        # print(l_home_link)

        C_BREADCRUMB_ACTIVE_ITEM = """                            <li itemprop="itemListElement" itemscope
                                itemtype="http://schema.org/ListItem">
                                    <span itemprop="name">__LABEL__</span>
                                       <span itemprop="position" content="__NUM__"></span>
                            </li>"""

        #  Build the URL string
        l_url = l_url + p_host_name
        
        # Seperator Character
        bCrumbList = l_breadcrumb.split("/")
        


        l_ctr = 1
        for l_item in bCrumbList:
            
            l_ctr = l_ctr+1
            
            if (bCrumbList[-1] != l_item):
                l_url     = l_url + "/" + l_item.lower()
                l_stg_str = C_BREADCRUMB_LINK_ITEM.replace('__LABEL__',l_item.upper())
                l_stg_str = (l_stg_str.replace('__LINK__',l_url)).replace("__NUM__",str(l_ctr))

                if (l_item in self.g_list_languages):
                    l_stg_str = l_stg_str.replace("__ICON__",p_lang_icon)
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



    # ########################
    # This Builds the SideMenu
    # ########################
    def SideMenuBuilder(self, p_language, p_meta_path, p_host_name):

        readlines_file = open(p_meta_path + p_language + ".index", "r")
        
        l_menu_head  = ""
        l_menu_body  = ""
        l_panel_body = ""

        l_menu_item  = """
                <div id="sidebar" class="sidebar-offcanvas">
                    <div class="col-md-12" style="background-color:white">
                        <br><br><br>
                        __MENU_ITEMS__
                    </div>
                </div>"""


        l_unit_panel = """<div class="panel panel-primary">
                    <div class="panel-heading panel-heading-sm">
                        __PANEL_HEADING__
                    </div>
                    <div class="panel-body panel-body-sm">
                        __PANEL_BODY__
                    </div>
                </div>"""


        # Loop Thru each line
        while True:
            l_line = readlines_file.readline().lower().replace('\n', '').replace('\r', '') # Read line by line, to variable current line
            if not l_line:
                break                          # Break if there is no line to read


            if( l_line[0] == "+" ):
                
                if (l_menu_head != ""):
                    
                    l_panel_body = l_panel_body + l_unit_panel.replace('__PANEL_HEADING__',l_menu_head).replace('__PANEL_BODY__',l_menu_body)
                    
                    #print(l_menu_head)
                    #print(l_menu_body)
                
                
                l_menu_head = l_line.replace('+','').upper()
                l_menu_body = ""

            elif( l_line[0] == "*" ):

                l_menu_body = l_menu_body + "<a href=\"" + p_host_name + p_language + "//" + (l_line.replace('*','')).replace(' ','-') + ".html\">" + l_line.replace('*','') + "</a>" + "<br>" + "\n"
       
        readlines_file.close()
        
        return(l_menu_item.replace('__MENU_ITEMS__',l_panel_body))



    # #######################
    # Web Page Header section
    # #######################
    def headerSec(self, p_title, p_desc, p_keywords, p_author, p_lang_icon, p_jtron_bgcolor,
                  p_txt_color, p_side_menu, p_language, p_static_top_menu, 
                  p_breadcrumb_data, p_topic_header, p_author_filename):

        print("HeaderSec")
        l_header = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content=\" __DESC__ \">
        <meta name="keywords" content=\"__KEYWORDS__\">

        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
        <!-- Custom CSS -->
        <link rel="stylesheet" href="commons/tinitiate.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-mfizz/2.3.0/font-mfizz.min.css">
        <!-- jQuery library -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
        <!-- Latest compiled JavaScript -->
        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
        <script src="commons/tinitiate.js"></script>
        <!-- Syntax Highlight -->
        <link rel="stylesheet" href="commons/syntax/styles/xcode.css">
        <script src="commons/syntax/highlight.pack.js"></script>
        <script>hljs.initHighlightingOnLoad();</script>

        <title>__TITLE__</title>
    </head>
    <body>
        <!-- Main Container START -->
        <div id="container"> 
        __STATIC_TOP_MENU__
        <!-- JumboTron Content Start -->            
        <div class=\"jumbotron subhead\" id=\"overview\" align=\"center\" style=\"background-color:__BG_COLOR__;\">
        <h1 style=\"color:__TEXT_COLOR__\">__LANG_ICON__&nbsp;&nbsp; __LANG_NAME__ TUTORIALS </h1>
        </div>        
        <div class=\"row-offcanvas row-offcanvas-left\"> __SIDE_MENU__
        <!-- Main Body START -->
                <div id="main">

                    <!-- MD-12 START -->
                    <div class="col-md-12">
                        <p class="visible-xs">
                        <button type="button" class="btn btn-link btn-xs" data-toggle="offcanvas"><i class="fa fa-arrow-circle-o-left fa-2x"></i> MENU</button>
                        </p>__BREADCRUMB_DATA__ __TOPIC_HEADER__ __AUTHOR_FILENAME__"""
 

        l_header = l_header.replace("__DESC__", p_desc)
        l_header = l_header.replace("__KEYWORDS__", p_keywords)
        l_header = l_header.replace("__LANG_NAME__", p_language.upper())
        l_header = l_header.replace("__BG_COLOR__", p_jtron_bgcolor)
        l_header = l_header.replace("__TEXT_COLOR__", p_txt_color)
        l_header = l_header.replace("__LANG_ICON__", p_lang_icon)
        l_header = l_header.replace("__TITLE__", p_title)
        # l_header = l_header.replace("__NAV_BAR__", p_nav_bar)
        # l_header = l_header.replace("__LANG_JUMBOTRON__", p_lang_jumbotron)
        l_header = l_header.replace("__SIDE_MENU__", p_side_menu)
        l_header = l_header.replace("__TOPIC_HEADER__", p_topic_header)
        l_header = l_header.replace("__BREADCRUMB_DATA__", p_breadcrumb_data)
        l_header = l_header.replace("__TOPIC_HEADER__", p_topic_header)
        l_header = l_header.replace("__AUTHOR_FILENAME__", p_author_filename)
        l_header = l_header.replace("__STATIC_TOP_MENU__", p_static_top_menu)

        return(l_header);



    # Web Page Footer section
    def footerSec(self):

        l_footer = """                    <!-- MD-12 END -->
                    </div>

                    <br><br>

                <!-- Main Body END -->
                </div>
            <!--/row-offcanvas END -->
            </div>

        <!-- Container END -->
        </div>
    </body>

</html>""";

        return(l_footer)



    # Build the Author FileName block    
    def authorFilename(self, p_author, p_file_name):

        l_data = """                        <br>
                            <dl class="dl-horizontal" style="padding-bottom: 0;">
                            <dt>Author</dt>
                            <dd>__AUTHOR__</dd>
                            <dt>File Name</dt>
                            <dd>__FILE_NAME__</dd></dl>
                            <br>"""

        return l_data.replace("__AUTHOR__",p_author).replace("__FILE_NAME__",p_file_name)



    # Header Data
    def TopicHeader(self, p_txt_color, p_data):
        
        return "<h2 style=\"color:" + p_txt_color + "\">" + p_data + "</h2>"



    # Build the Code Blog Post
    def CodeBlog(self, p_lang_icon, p_code_title, p_codeblog_data, p_keywords, p_author):

        # Article Created Date
        # l_date_published  = datetime.datetime.today.strftime("%d-%b-%Y")
        l_date_published  = time.strftime("%d-%b-%Y")

        l_page_content    = ""

        l_blog_block  = """                        <div itemscope itemtype=\"http://schema.org/blog\" class=\"panel panel-default\" style=\"margin-bottom: 2px;\">
                            <meta itemprop=\"author\" content=\" """ + p_author + """ \"/>
                            <meta itemprop=\"datePublished\" content=\" """ + l_date_published + """ \"/>
                            <meta itemprop=\"keywords\" content=\" """ + p_keywords + """ \">
                            <div itemprop=\"headline\" class=\"panel-heading panel-heading-sm\"><b>&nbsp;&nbsp; """ + p_lang_icon + """&nbsp;&nbsp; """ + p_code_title + """ </b></div>
                            <div itemprop=\"text\" class=\"panel-body panel-body-sm\"> """ + p_codeblog_data + """
                            </div>
                        </div>"""

        # l_page_content = l_blog_block.replace("__CODE_TITLE__", p_code_title)
        # l_page_content = l_blog_block.replace("__CODE_NOTES__", p_codeblog_data)
        # l_page_content = l_blog_block.replace("__DATE_PUBLISHED__", l_date_published)
        # l_page_content = l_blog_block.replace("__CODE_AUTHOR__", p_author)
        # l_page_content = l_blog_block.replace("__KEYWORDS__", p_code_title)

        # print(l_blog_block)

        # Code Block, Code and Output
        return l_blog_block            



    # Draw the Actual Page
    def CodeBlock(self, p_language, p_code):

        l_page_content    = ""
       
        l_code_block  = """                        <div class="panel panel-default" style="margin-bottom: 2px;">
                            <div class="panel-heading panel-heading-sm"><b>&nbsp;&nbsp;<i class="fa fa-code"></i>&nbsp;&nbsp;code</b></div>
                            <div class="panel-body panel-body-sm" itemscope itemtype="http://schema.org/SoftwareSourceCode"><meta itemprop="programmingLanguage" content="__LANGUAGE__"/>
                            <pre itemprop="text" style="background-color:white; margin-bottom: 0px; margin-top: 0px; border:0px"><code class="__LANGUAGE__">__CODE__</code></pre>
                            </div>
                        </div>"""

        l_page_content = l_code_block.replace("__LANGUAGE__", p_language)
        l_page_content = l_code_block.replace("__CODE__", p_code)

        # Code Block, Code and Output
        return l_page_content            



    # Draw the Actual Page
    def CodeOutput(self, p_output):

        l_page_content    = ""

        l_output_block = """                        <div class="panel panel-default" style="margin-bottom: 10px;">
                            <div class="panel-heading panel-heading-sm"><b>&nbsp;&nbsp;<i class="fa fa-list-alt"></i>&nbsp;&nbsp; output</b></div>
                            <div class="panel-body panel-body-sm">__OUTPUT__
                            </div>
                        </div>"""

        l_page_content =  l_output_block.replace("__OUTPUT__", p_output)

        # Code Block, Code and Output
        return l_page_content            



    # Tags
    def PageTags(self, p_tags):

        l_page_content    = ""
        l_tags_web_string = ""
       
        for ldata in p_tags.strip().split(","):

            l_tags_web_string = l_tags_web_string + "&nbsp;&nbsp;<span class=\"badge\">" + ldata + "</span>"


        # Change the tags
        l_page_content = """
                    <div class="panel panel-warning">
                        <div class="panel-heading panel-heading-sm"><i class="fa fa-tags"></i>""" + l_tags_web_string + """</div>
                    </div>"""


        # Code Block, Code and Output
        return l_page_content



    def CodePros(self, p_pros):

        l_page_content    = ""

        l_output_block = """
                    <div class="panel panel-success">
                        <div class="panel-heading panel-heading-sm"><i class="fa fa-star"></i> PROS</div>
                        <div class="panel-body panel-body-sm">__PROS__</div>
                    </div>"""

        l_page_content =  l_output_block.replace("__PROS__", p_pros)

        # Code Block, Code and Output
        return l_page_content



    def CodeCons(self, p_pros):

        l_page_content    = ""

        l_output_block = """
                    <div class="panel panel-danger">
                        <div class="panel-heading panel-heading-sm"><i class="fa fa-minus-circle"></i> CONS</div>
                        <div class="panel-body panel-body-sm">__CONS__</div>
                    </div>"""

        l_page_content =  l_output_block.replace("__CONS__", p_pros)

        # Code Block, Code and Output
        return l_page_content



    # Draw the Actual Page
    def DrawArticleOLD(self, p_parsed_dict):

        l_code_block = """        <div itemscope itemtype="http://schema.org/blog">
            <h1 itemprop="headline">__CODE_TITLE__</h1>
            <pre itemprop="author">__CODE_AUTHOR__</pre>
            <meta itemprop="datePublished" content="__DATE_PUBLISHED__"/>
            <p itemprop="about">Java Tutorials</p>
            <meta itemprop="keywords" content="__KEYWORDS__">
            <pre itemprop="text">
            __CODE_NOTES__
            </pre>
        </div>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
            <meta itemprop="programmingLanguage" content="__LANGUAGE__"/>
            <pre itemprop="text">
            __CODE__
            </pre>
        </div>"""
