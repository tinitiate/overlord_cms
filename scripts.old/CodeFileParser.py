# CodeFileParser.py
# About:
#    This program parses the code file to generate tutorial code web file


# Usage:
#


# CODE CHANGES
# ==============================================================================
# Date            Developer        Notes
# ==============================================================================
# May 26, 2016    Venkata B        Initial Version, Code Page parser Changes
# May 27, 2016    Venkata B        Block Reading Process start
# May 27, 2016    Venkata B        Basic (Single Multi) Block code
# Jun 02, 2016    Venkata B        Block (SIngle and Multi) Construction
# Jul 16, 2016    Venkata B        Created a DICT to store Single and Multi block
#                                  in the order of creation
#  
# ==============================================================================


import os
import re

class CodeFileParser:

    g_render_page  = "";


    # Language Specific Data
    g_comment_char      = "";
    g_language          = "";
    g_multi_block_stage = "";


    # This Dict will handle the BlockName and the BlockData and the Order 
    # in which the block data is received.
    g_page_block_data_list   = [];
    

    def __init__(self):
        self.g_render_page  = "";



    def SingleLineBlockBuilder(self,p_block_name,p_data):
        
        # Remove Comment Character, a`nd Single Block Name
        l_data       = re.sub('^'+self.g_comment_char+" "+p_block_name, '', p_data).strip()
        l_block_list = [p_block_name,l_data];

        self.g_page_block_data_list.append(l_block_list)

        # Process Block
        # self.g_render_page = self.g_render_page + "\n" + l_data



    def MultiLineBlockBuilder(self,p_block_name,p_data,p_block_state):       

        # Get Data and Block information
        l_data       = p_data.strip()       
        l_block_list = [];

        
        # print(p_block_state)

        if (p_block_state > 1):
            # print(p_block_name,p_block_state,p_data)
            self.g_multi_block_stage  = self.g_multi_block_stage + p_data;
            # g_render_page = g_render_page + "<br>" + p_data;
            # print(p_block_name," ",p_block_state)

        # End Block processing
        elif (p_block_state == -1):
            self.g_render_page=self.g_render_page + self.g_multi_block_stage;
            # print(p_block_name," ",p_block_state)
            # Add to local list
            # l_block_list = [p_block_name,self.g_multi_block_stage]
            # print(g_multi_block_stage)
            self.g_page_block_data_list.append(self.g_multi_block_stage)

        

    def FileParser(self, p_file_name_path):

        # Get the Programming Language 
        l_file_name = os.path.basename(p_file_name_path)
        # print(l_file_name)


        l_st_index      = int((len(l_file_name) - (len(l_file_name) - (l_file_name.find(".")))) + 1)
        l_ed_index      = int(len(l_file_name))      
        self.g_language = l_file_name[l_st_index:l_ed_index]


        # BLOCK STATE VALUES
        # 1=BLOCK START, 1+=BLOCK MIDDLE, -1=BLOCK END
        # Block Detectors
        l_curr_block        = ""
        l_curr_block_state  = 2


        # Overlord Supported Formats
        l_single_line_block     = ('>>TITLE - ','>>BREADCRUMB - '
                                    ,'>>HEADLINE - ','>>AUTHOR - '
                                    ,'>>DATEPUBLISHED - ','>>FILE-NAME - '
                                    ,'>>DEPENDANT-FILES - ','>>CODE-TITLE -');



        l_multi_line_block      = ('>>DESC<<','>>KEYWORDS<<','>>ABOUT<<','>>NOTES<<',
                                   '>>POINTS<<','>>CODE-NOTES<<','>>CODE-ALL-OS<<',
                                   '>>CODE-WIN<<','>>CODE-OSX<<','>>CODE-LIN<<',
                                   '>>OUTPUT<<','>>TAGS<<','>>PROS<<','>>CONS<<',
                                   '>>RELATED-TOPICS<<');


        l_end_multi_line_block  = '>><<';


        fileHandle = open(p_file_name_path,"r")


        # Read the file line by line
        while True:
            # Read line by line, to variable current line
            curr_line = fileHandle.readline()


            # Read the Comment Char and assign to global var , only if unassigned.
            if (self.g_comment_char == ""):
                self.g_comment_char = curr_line[0:2].strip()


            # Block Reading
            
            # Single Block Reading
            # --------------------

            # Check if the Line is part of any Block5
            for l_sb in l_single_line_block:

                if ( curr_line.find(l_sb) != -1):
                    l_curr_single_block = l_sb
                    self.SingleLineBlockBuilder(l_curr_single_block,curr_line);


            # Multi Block Reading
            # -------------------
            # Check if the Line is part of any Block
            for l_mb in l_multi_line_block:
            

                if (curr_line.find(l_mb) != -1 ):
                    l_curr_block       = l_mb
                    
                    l_curr_block_state = 1
                    # print(l_curr_block)

                elif (curr_line.find(">><<") > 0):
                    l_curr_block_state = -1
                
                # elif (l_curr_block_state == 1):


            # Block Prep
            # print(l_curr_block,l_curr_block_state,curr_line)
            if (l_curr_block_state == 1):
                l_curr_block_state=l_curr_block_state+1

            elif (l_curr_block_state > 1 and
                  l_multi_line_block.count(l_curr_block) == 1):

                self.MultiLineBlockBuilder(l_curr_block,curr_line,l_curr_block_state)
            
            elif (l_curr_block_state == -1 and
                  l_multi_line_block.count(l_curr_block) == 1):

                self.MultiLineBlockBuilder(l_curr_block,curr_line,l_curr_block_state)
                l_curr_block       = ""
                l_curr_block_state = 0


            # Break if there is no line to readm
            if not curr_line:
                break


            # Parse the Line and split into the variables 
            # FileSegmentParser(curr_line)       # Print the current line


        # Close the File stream handler
        fileHandle.close()
        
        # print(self.g_comment_char)
        # print(self.g_language)
        # print(self.g_render_page)
        print(self.g_page_block_data_list)
