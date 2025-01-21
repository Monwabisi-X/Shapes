def solid_rectangle(rows, cols):
    """
    Constructs a solid rectangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The number of rows in the rectangle.
    cols (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings, each representing a row of the rectangle.
    """
    pattern = []
    for _ in range(rows):
        pattern.append('*' * cols)
    return pattern

def hollow_rectangle(rows, cols):
    """
    Constructs a hollow rectangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The number of rows in the rectangle.
    cols (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings, each representing a row of the hollow rectangle.
    """
    pattern = []
    if rows == 1:
        pattern.append('*' * cols)
    else:
        pattern.append('*' * cols)
        for _ in range(rows - 2):
            pattern.append('*' + ' ' * (cols - 2) + '*')
        pattern.append('*' * cols)
    return pattern

def right_angled_triangle(rows):
    """
    Constructs a right-angled triangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the triangle.
    """
    pattern = []
    for i in range(1, rows + 1):
        pattern.append('*' * i)
    return pattern

def inverted_right_angled_triangle(rows):
    """
    Constructs an inverted right-angled triangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the inverted triangle.
    """
    pattern = []
    for i in range(rows, 0, -1):
        pattern.append('*' * i)
    return pattern

def pyramid(rows):
    """
    Constructs a pyramid pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the pyramid.
    
    Returns:
    list: A list of strings, each representing a row of the pyramid.
    """
    pattern = []
    for i in range(rows):
        pattern.append(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    return pattern

def inverted_pyramid(rows):
    """
    Constructs an inverted pyramid pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the inverted pyramid.
    
    Returns:
    list: A list of strings, each representing a row of the inverted pyramid.
    """
    pattern = []
    for i in range(rows):
        pattern.append(' ' * i + '*' * (2 * (rows - i) - 1))
    return pattern

def diamond(rows):
    """
    Constructs a diamond pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the diamond's upper half.
    
    Returns:
    list: A list of strings, each representing a row of the diamond.
    """
    upper_part = pyramid(rows)
    lower_part = inverted_pyramid(rows)[1:]
    return upper_part + lower_part

def hollow_diamond(rows):
    """
    Constructs a hollow diamond pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the diamond's upper half.
    
    Returns:
    list: A list of strings, each representing a row of the hollow diamond.
    """
    upper_part = []
    for i in range(rows):
        upper_part.append(' ' * (rows - i - 1) + '*' + ' ' * (2 * i - 1) + '*' * (i > 0))
    lower_part = []
    for i in range(1, rows):
        lower_part.append(' ' * i + '*' + ' ' * (2 * (rows - i - 1) - 1) + '*' * (i < rows - 1))
    return upper_part + lower_part

def number_triangle(rows):
    """
    Constructs a triangle pattern composed of numbers.
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the number triangle.
    """
    pattern = []
    for x in range(1, rows + 1):
        pattern.append(' '.join([str(x)] * x))
    return pattern

def floyds_triangle(rows):
    """
    Constructs Floyd's triangle pattern composed of consecutive numbers.
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of Floyd's triangle.
    """
    num = 1
    result = []
    for i in range(1, rows + 1):
        line = []
        for j in range(i):
            line.append(str(num))
            num += 1
        result.append(' '.join(line))
    return result

def alphabet_pyramid(rows):
    """
    Constructs an alphabet pyramid pattern.
    
    Parameters:
    rows (int): The height of the pyramid.
    
    Returns:
    list: A list of strings, each representing a row of the alphabet pyramid.
    """
    pattern = []
    for i in range(rows):
        line = ' ' * (rows - i - 1)
        for j in range(i + 1):
            line += chr(65 + j) + ' '
        pattern.append(line.rstrip())
    return pattern

def mirrored_right_angled_triangle(rows):
    """
    Constructs a mirrored right-angled triangle pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of the mirrored triangle.
    """
    pattern = []
    for i in range(rows):
        pattern.append(' ' * (rows - i - 1) + '*' * (i + 1))
    return pattern

def hourglass(rows):
    """
    Constructs an hourglass pattern composed of asterisks ('*').
    
    Parameters:
    rows (int): The total height of the hourglass.
    
    Returns:
    list: A list of strings, each representing a row of the hourglass.
    """
    pattern = []
    for i in range(rows // 2 + 1):
        spaces = ' ' * i
        stars = '*' * (rows - 2 * i)
        pattern.append(spaces + stars + spaces)
    for i in range(rows // 2 - 1, -1, -1):
        spaces = ' ' * i
        stars = '*' * (rows - 2 * i)
        pattern.append(spaces + stars + spaces)
    return pattern

def pascals_triangle(rows):
    """
    Constructs Pascal's triangle pattern composed of numbers.
    
    Parameters:
    rows (int): The height of the triangle.
    
    Returns:
    list: A list of strings, each representing a row of Pascal's triangle.
    """
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    max_width = len(' '.join(map(str, triangle[-1])))
    result = []
    for row in triangle:
        result.append(' '.join(map(str, row)).rjust((max_width + len(' '.join(map(str, row)))) // 2))
    return result

def diamond_number_pattern(rows):
    """
    Constructs a diamond pattern composed of numbers.
    
    Parameters:
    rows (int): The height of the diamond's upper half.
    
    Returns:
    list: A list of strings, each representing a row of the diamond number pattern.
    """
    upper_part = []
    for i in range(rows):
        line = ' ' * (rows - i - 1)
        line += ''.join(str(j) for j in range(1, i + 2))
        line += ''.join(str(j) for j in range(i, 0, -1))
        upper_part.append(line)
    lower_part = upper_part[::-1]
    return upper_part + lower_part[1:]
