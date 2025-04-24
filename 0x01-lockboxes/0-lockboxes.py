#!/usr/bin/python3
"""
Determine if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    This function determines if all boxes can be opened

    Args:
        boxes (list of lists): Each box contains keys to other boxes.

    Return:
        bool: True if all boxes can be opened, otherwise False.
    """

    num_boxes = len(boxes)
    opened = {0}
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < num_boxes and key not in opened:
            opened.add(key)
            keys.update(boxes[key])

    return len(opened) == num_boxes
