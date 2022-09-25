#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:30:23 2022

@author: melissahuynh-
"""
from tabulate import tabulate
import lexer
import re
from collections import OrderedDict


def open_file(filename):
    """
    Returns file to be read

    """
    data = open(filename, 'r').read()
    return data


def addAllDict(new_Dict, key, values):
    """
    Adds all dictionaries from all 
    Token Objects in a single dictionary

    """
    if key not in new_Dict:
        new_Dict[key] = list()
        
    new_Dict[key].extend(values)
    return new_Dict


def removeDup(new_Dict):
    """
    Removes duplicate values in list from dictionary

    """
    for k, v in new_Dict.items():
        values = list(OrderedDict.fromkeys(v))
        new_Dict[k] = values


if __name__ == '__main__':
    text = open_file('input_sourcecode.txt')
    
    lines = re.sub(r'//.*',' ',text)
    lines = lines.splitlines()
    
    new_Result = {}
    
    for i in lines:
        result = lexer.run(i)
        #print(result) <--prints dictionary for each line in file
        for k, v in result.items():
            addAllDict(new_Result, k, v)
            
    removeDup(new_Result)
    
    headers = ["Token", "Lexeme"]
    table = (tabulate([(k, v) for k, v in new_Result.items()],headers = headers))
    print(table)
    
    with open('output.docx', 'w') as f:
        f.write(table)
    
    
