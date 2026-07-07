# Island Perimeter

## Description

This project contains a Python function that calculates the perimeter of an island represented in a grid.

The grid is made of:

* `0` representing water
* `1` representing land

Each cell is a square with a side length of 1. The function returns the total perimeter of the island.

---

## Requirements

* Ubuntu 14.04 LTS
* Python 3.4.3
* PEP 8 style (version 1.7)
* No external modules or imports allowed
* All files must be executable
* All Python files must start with:

```python
#!/usr/bin/python3
```

---

## Files

| File                    | Description                              |
| ----------------------- | ---------------------------------------- |
| `0-island_perimeter.py` | Contains the `island_perimeter` function |
| `README.md`             | Project documentation                    |

---

## Function Prototype

```python
def island_perimeter(grid):
```

### Parameters

* `grid`: A list of lists of integers representing the map.

  * `0` represents water.
  * `1` represents land.

### Return

Returns an integer representing the perimeter of the island.

---

## Example

Input:

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))
```

Output:

```text
12
```

---

## Algorithm

The algorithm scans every cell in the grid.

For each land cell (`1`):

1. Add `4` to the perimeter because every land cell has four sides.
2. If the cell has a land neighbor on the right, subtract `2` because they share one side.
3. If the cell has a land neighbor below, subtract `2` because they share one side.

Only checking the right and bottom neighbors avoids counting shared edges twice.

---

## Author

Holberton School Student Rawan

