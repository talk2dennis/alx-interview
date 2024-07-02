# Lockboxes

This repository contains a solution for the Lockboxes task. The task is to implement a function that determines whether all the boxes in a given list can be unlocked.

## Function Signature

```python
def canUnlockAll(boxes: List[List[int]]) -> bool:
    pass
```

## Parameters

- `boxes`: A list of lists representing the lockboxes. Each inner list contains the - - `keys` that the corresponding box holds.
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`

## Return Value

- `True` if all the boxes can be unlocked, `False` otherwise.

## Example

```python
boxes = [[1], [2], [3], []]
print(can_unlock_all(boxes))  # Output: True

boxes = [[1, 2], [3], [4, 5, 6], []]
print(can_unlock_all(boxes))  # Output: False
```
