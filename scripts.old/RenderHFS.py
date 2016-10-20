class RenderHFS():


    def SideBar():

        l_sidebar = """
            """
        return l_sidebar;


    def staticPageMenu():

        return """        <div id="container">
            <!-- Navbar Start -->
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
                    <li><a href="#">Databases</a></li>
                    <li><a href="#about">Programming Languages</a></li>
                    <li><a href="#contact">Scripting Languages</a></li>
                    <li><a href="#contact">Web Programming</a></li>
                    <!-- TopBar Content End -->
                    </ul>
                </div>
            </div>

        """;



    def jTron(p_jtron_text, p_jtron_bgcolor, p_txt_color):

        return """            <!-- JumboTron Content Start -->
            <p class="jumbotron subhead" id="overview" align="center" style="background-color:""" + p_jtron_bgcolor +"""; color:""" + p_txt_color""";">
            """ + p_jtron_text + """
            </p>
            <!-- JumboTron Content Start -->"""




    # Web Page Header section
    def headerSec(self, p_title, p_desc, p_keywords, p_author):

        l_header = """    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content=\"""" + p_desc + """\">
        <meta name="keywords" content=\"""" + p_keywords + """\">
        <meta name="author" content=\"""" + p_author + """\">

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

        <title>""" + p_title + """</title>
    </head>""";

        return(l_header);



    # Web Page Footer section
    def footerSec(self):

        l_footer = """            <div class="bs-docs-header" id="content1" tabindex="3" style="background-color:#DD4814; color:white">
                <div class="container">
                    <br><br>
                    <div class="row">
                        <div class="col-md-4">
                            <h4>UPCOMING PROJECTS</h4>
                            <hr>
                            <p>TETL Tinitiate ETL System<br>
                            WAMP Apps<br>
                            tincss.css<br>
                            </p>
                        </div>
                        <div class="col-md-4">
                            <h4>ABOUT US</h4><hr>
                            <p>+ We are IT professionals who write code for hobby.<br>
                               + Code examples syntax variations and concepts.<br>
                               + Code in a detail and to the point notes.<br>
                               + Please bookmark tinitiate.com
                            </p>
                        </div>
                        <div class="col-md-4"><h4>FOLLOW US</h4><hr>
                            <a href="https://www.facebook.com/tinitiate"><img src="http://www.tinitiate.com/radius/images/social/facebook.png" alt="facebook tinitiate"></a><br><br>
                            <b>&copy; tinitiate.com 2015</b>
                        </div>
                    </div>
                    <br><br>
                </div>
            </div>""";

        return(l_footer)
