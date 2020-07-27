def find_match(svg,dim):
    for i in range(9):
        if svg[i] == dim:
            return (i+1)


svg=[
    [12,30], #1
    [20,31], #2
    [21,32], #3
    [24,30], #4
    [21,31], #5
    [22,32], #6
    [20,30], #7
    [22,32], #8
    [23,32], #9
    ]

dim=[12,30]
aux2='M10.964'
print('M10.964' == aux2 )