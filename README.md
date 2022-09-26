# Project 1 Lexers


## Option 1: group work (up to 3 persons)  
 
Write a lexer from scratch by designing and implementing FSA that returns the tokens from the simple source code in C++ in the given file “input_soucecode.txt”. In your final build, at least you need design and implement FSA for tokens identifier and integer, the rest can be written ad-hoc. Otherwise, there will be a deduction of 5 points! 
 
• Requirement  of  design  part:  you  need  to  provide  lexical  specification  using  REs  and draw state-transition diagrams using FSA that is implemented in the Lexer for the above required tokens (at least): identifier and integer and wrap them into a document named as 
“myDesign.doc”. 

• Requirement of implementation part: the implementation of your design is an executable program, and it is expected to write in C/C++ or Python. In your program, name a function as lexer() to read and return the next token.   

• Requirement  of  output  part:  you  need  to  print  out  the  result  in  the  form  of  Two  (2) columns,  one  column  for  tokens  and  the  other  for  lexemes,  and  save  it  into  a  document named as “output” (see an example I/O as below). 

• Requirement of user manual part: you need write a “readme” file to briefly specify how to setup/run your program. 

• Requirement  of  submission  part:  your  final  submission  to  Canvas  must  have  Five  (5) files: the given “input_soucecode.txt”, design file, your program, output file, and a readme file. 

**Example:** Lexer splits the source text into a sequence of tokens, skipping blanks, newlines, and comments. See the I/O as below. **Note:** you can customize your token classes and names, and then attach with the corresponding lexemes. 

**Input (source code text):**

                   while (x > 1)   y = 23.00; 
  
**Output:**
 
                   token                                      lexeme
                   -----------------------------------------------------------
                   keyword                                    while 
                   separator                                      (, )            
                   identifier                                       x, y 
                   operator                                        >, = 
                   integer                                        1 
                   real                                             23.00  
                   punctuation                                   ; 

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

## lexer.py
This file contains the tokens and lexer class, along with some error exception handling. 

## shell.py
This is the main file to run. 
Make sure lexer.py, shell.py, “input_sourcecode.txt” are all in the same folder location otherwise the main file will run an error. 
Running main on shell.py will create output.docx with a table of Tokens and corresponding Lexeme in list. May need to install imported modules in shell.py before running main.
