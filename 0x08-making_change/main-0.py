#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([25, 10, 5, 1], 47))

print(makeChange([1256, 54, 48, 16, 102], 1453))
