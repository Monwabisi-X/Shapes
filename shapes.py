def solid_rectangle(rows, cols):
    """
    Constructs a solid rectangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The number of rows in the rectangle.
    cols (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings, each representing a row of the rectangle.
    """
    pass

def hollow_rectangle(rows, cols):
    """
    Constructs a hollow rectangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The number of rows in the rectangle.
    cols (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings, each representing a row of the hollow rectangle.
    """
    pass

def right_angled_triangle(rows):
    """
    Constructs a right-angled triangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the triangle.
    """
    pass

def inverted_right_angled_triangle(rows):
    """
    Constructs an inverted right-angled triangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the inverted triangle.
    """
    pass

def pyramid(rows):
    """
    Constructs a pyramid pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the pyramid.
    
    Returns:
    list: A list of strings, each representing a row of the pyramid.
    """
    pass

def inverted_pyramid(rows):
    """
    Constructs an inverted pyramid pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the inverted pyramid.
    
    Returns:
    list: A list of strings, each representing a row of the inverted pyramid.
    """
    pass

def diamond(rows):
    """
    Constructs a diamond pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the diamond's upper half.
    
    Returns:
    list: A list of strings, each representing a row of the diamond.
    """
    shape = []
    for row in range(rows):
        string = " " * (rows - row - 1) + "*" * (2 * row + 1)
        shape.append(string)
    
    for row in reversed(range(rows - 1)):
        string = " " * (rows - row - 1) + "*" * (2 * row + 1)
        shape.append(string)
    
    return shape

def hollow_diamond(rows):
    """
    Constructs a hollow diamond pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the diamond's upper half.
    
    Returns:
    list: A list of strings, each representing a row of the hollow diamond.
    """
    shape = []
    for row in range(rows):
        spaces =  " " * (2 * (row - 1) + 1)
        if row != 0:
            string = " " * (rows - row - 1) + "*" + spaces + "*"
        else:
            string = " " * (rows - row - 1) + "*" * (2 * row + 1)
        shape.append(string)
    
    for row in reversed(range(rows - 1)):
        spaces =  " " * (2 * (row - 1) + 1)
        if row != 0:
            string = " " * (rows - row - 1) + "*" + spaces + "*"
        else:
            string = " " * (rows - row - 1) + "*" * (2 * row + 1)
        shape.append(string)
    
    return shape

def number_triangle(rows):
    """
    Constructs a triangle pattern composed of numbers.
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the number triangle.
    """
    shape = []
    for row in range(rows):
        string = ""
        for i in range(row + 1):
            string += str(row + 1)
            if i != row:
                string += " "
        shape.append(string)
    
    return shape

sh = number_triangle(5)
for i in sh:
    print(i)

def floyds_triangle(rows):
    """
    Constructs Floyd's triangle pattern composed of consecutive numbers.
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of Floyd's triangle.
    """
    pass

def alphabet_pyramid(rows):
    """
    Constructs an alphabet pyramid pattern.
    
    Parameters:
    rows (int): The height of the pyramid.
    
    Returns:
    list: A list of strings, each representing a row of the alphabet pyramid.
    """
    pass

def mirrored_right_angled_triangle(rows):
    """
    Constructs a mirrored right-angled triangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the mirrored triangle.
    """
    pass

def hourglass(rows):
    """
    Constructs an hourglass pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The total height of the hourglass.
    
    Returns:
    list: A list of strings, each representing a row of the hourglass.
    """
    pass

def pascals_triangle(rows):
    """
    Constructs Pascal's triangle pattern composed of numbers.
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of Pascal's triangle.
    """
    pass

def diamond_number_pattern(rows):
    """
    Constructs a diamond pattern composed of numbers.
    
    Parameters:
    rows (int): The height of the diamond's upper half.
    
    Returns:
    list: A list of strings, each representing a row of the diamond number pattern.
    """
    pass
