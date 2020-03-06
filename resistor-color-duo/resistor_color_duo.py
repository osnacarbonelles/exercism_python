def value(colors):
    colors_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
                   'yellow': 4, 'green': 5, 'blue': 6,
                   'violet': 7, 'grey': 8, 'white': 9}
    return int(str(colors_code[colors[0]])+str(colors_code[colors[1]]))
