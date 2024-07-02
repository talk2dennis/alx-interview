#!/usr/bin/python3
""" a module to check if all boxes can unlock """

def canUnlockAll(boxes):
    """canUnlockAll
	
	Keyword arguments:
	boxes -- list of list of integers
	Return: true otherwise false
	"""
    n = len(boxes)
    opened = [False] * n # set all to false (unopened)
    opened[0] = True # set the first box to True (opened)
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)
    
    return all(opened)
    