from IPython.display import display, Math
import numpy as np
import sympy as sp

# Convert to symbolic expressions for nicer formatting
def format_complex_array(complex_num):
    # Handle common quantum values like 1/sqrt(2)
    if abs(abs(complex_num) - 1/np.sqrt(2)) < 1e-8:
        if complex_num.real > 0 and abs(complex_num.imag) < 1e-8:
            return "\\frac{1}{\\sqrt{2}}"
        elif complex_num.real < 0 and abs(complex_num.imag) < 1e-8:
            return "-\\frac{1}{\\sqrt{2}}"
        # Add cases for imaginary components if needed
    
    # Handle zero values
    if abs(complex_num) < 1e-8:
        return "0"
    
    # Handle ones
    if abs(complex_num - 1) < 1e-8:
        return "1"
    if abs(complex_num + 1) < 1e-8:
        return "-1"
    
    # Default case - use sympy to format nicely
    return sp.latex(sp.sympify(complex(complex_num)))

# Apply formatting to the entire matrix
def unitary_to_latex(matrix, prefix="Unitary = "):
    rows, cols = matrix.shape
    
    # Start LaTeX matrix
    latex_str = "\\begin{bmatrix}\n"
    
    # Format each row
    for i in range(rows):
        row_str = " & ".join([format_complex_array(matrix[i, j]) for j in range(cols)])
        latex_str += row_str
        
        # Add line break for all but the last row
        if i < rows - 1:
            latex_str += " \\\\\n"
    
    # End LaTeX matrix
    latex_str += "\n\\end{bmatrix}"
    
    # Display with prefix
    return Math(f"\\text{{{prefix}}} {latex_str}")
