#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = []
        
        for element in row:
            formatted_element = "{:d}".format(element)
            formatted_row.append(formatted_element)
        
        row_string = " ".join(formatted_row)
        
        print(row_string)
