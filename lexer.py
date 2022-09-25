#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:22:02 2022

@author: melissahuynh
"""
from sys import*
import string

#Constants
DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGIT = LETTERS + DIGITS
KEYWORDS = ['while','for', 'cout', 'return']
OPERATOR = ['+', '<', '>', '=']
DOPERATOR = ['<=', '>=', '==', '<<']
SEPARATOR = ["\"", "(", ")", "{", "}"]
BLANKSPACE = ' \n\t'

"""---------
    Errors
    --------"""
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
        
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class illegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character',details)
        
"""---------
    TOKENS
   ---------"""

TT_INT	= 'INT'
TT_FLOAT	= 'REAL'
TT_OPERATOR = 'OPERATOR'
TT_QUOTE    = 'SEPARATOR'
TT_LPAREN	= 'SEPARATOR'
TT_RPAREN	= 'SEPARATOR'
TT_SEMICOL	= 'PUNCTUATION'
TT_EXCLAIM	= 'PUNCTUATION'
TT_OCBRAC	= 'SEPARATOR'
TT_CCBRAC	= 'SEPARATOR'
TT_DQUOTE	= 'PUNCTUATION'
TT_FSLASH   = 'PUNCTUATION'
TT_ASSIGN = 'EQUALS'
TT_IDENTIFIER = 'IDENTIFIER'
TT_KEYWORD = 'KEYWORD'


class Token: 
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
        
    def __repr__(self):
        if self.value: return self.type, self.value
        return f'{self.type}'
    
"""----------
    LEXER
   ----------"""
class Lexer:   
   def __init__(self, text):
       self.text = text
       self.pos = 0
       self.current_char = None
       self.advance()

   def advance(self):
        """
        Move position of current_char += 1

        """
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
            
        self.pos += 1
        
            
   def make_Num(self):
       """
       Return Token Object of Type Integer or Float with value
       
       """
       num_str = ""
       dec_bool = 0
       
       while self.current_char != None and (self.current_char in DIGITS 
                                            or self.current_char == '.'):
            if self.current_char == '.':
                dec_bool += 1
                if dec_bool > 1:
                    break
            num_str += self.current_char
            self.advance()
               
       if dec_bool == 0:
          return Token(TT_INT,(num_str))
       else:
          return Token(TT_FLOAT, float(num_str))
      
   def make_Identifier(self):
       """
       Return Token Object of type Identifier with value
  
       """
       id_str = ""
       #pos_start = self.pos.copy()
       
       while self.current_char != None and (self.current_char in LETTERS 
                                            or self.current_char == '_'):
           id_str += self.current_char
           self.advance()
           if id_str in KEYWORDS:
               tok_type = TT_KEYWORD
           else:
               tok_type = TT_IDENTIFIER
            
       return Token(tok_type,id_str)
   
   def make_Operator(self):
        """
       Return Token Object of type Operator with value

        """
        id_op = ""
        tok_type = TT_OPERATOR
        
        while self.current_char != None and self.current_char in OPERATOR:
            id_op += self.current_char
            self.advance()
            if id_op in DOPERATOR: 
                return Token(tok_type, id_op)
        return Token(tok_type, id_op)
        
   
   def make_tokens(self):
       """
       Returns a list of Token Objects

       """
       tokens = []
       
       while self.current_char != None:
           if self.current_char.isspace():
               self.advance()
           elif self.current_char in BLANKSPACE:
               self.advance()
           elif self.current_char in DIGITS:
               tokens.append(self.make_Num())
               
           elif self.current_char in OPERATOR:
               tokens.append(self.make_Operator())
               
           elif self.current_char == '"':
               tokens.append(Token(TT_DQUOTE, '"'))
               self.advance()
           elif self.current_char == '(':
               tokens.append(Token(TT_LPAREN, '('))
               self.advance()
           elif self.current_char == ')' :
               tokens.append(Token(TT_RPAREN, ')'))
               self.advance()
           elif self.current_char == ';':
               tokens.append(Token(TT_SEMICOL, ';'))
               self.advance()
           elif self.current_char == '!':
               tokens.append(Token(TT_EXCLAIM, '!'))
               self.advance()
           elif self.current_char == '{':
               tokens.append(Token(TT_OCBRAC, '{'))
               self.advance()
           elif self.current_char == '}':
               tokens.append(Token(TT_CCBRAC, '}'))
               self.advance()
           elif self.current_char in LETTERS:
               tokens.append(self.make_Identifier())
               
           else:
               char = self.current_char
               self.advance()
               return [], illegalCharError("'" + char + "'")
       return tokens
   
    
def run(data):
    sample_dict = {}
    lexers = Lexer(data)
    token = lexers.make_tokens()
    
    for i in token:
        addToken(sample_dict, i.type,i.value)
    
    return sample_dict
   
            
def addToken(sample, key, values):
    if key not in sample:
        sample[key] = list()
    sample[key].append(values)
    return sample

 
