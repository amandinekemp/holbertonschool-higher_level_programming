#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = []
        
        for col in row:
            formatted_element = "{:d}".format(col)
            
            if col != row[-1]:
                formatted_element += " "
            
            formatted_row.append(formatted_element)
        
        row_string = "".join(formatted_row)
        
        print(row_string)
