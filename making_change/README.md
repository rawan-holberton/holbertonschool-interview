# Making Change

## Description

This project contains a Python solution to the **Making Change** problem. The goal is to determine the fewest number of coins needed to make a given total using an unlimited supply of the provided coin denominations.

If it is impossible to make the exact total with the available coins, the function returns `-1`.

---

## Requirements

* Ubuntu 14.04 LTS
* Python 3.4.3
* PEP 8 (version 1.7.x)
* All files must be executable
* The first line of every Python file must be:

```python
#!/usr/bin/python3
```

---

## Files

| File                 | Description                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| `0-making_change.py` | Contains the `makeChange` function that returns the minimum number of coins required to reach a given total. |
| `README.md`          | Project documentation.                                                                                       |

---

## Function Prototype

```python
def makeChange(coins, total):
```

### Parameters

* `coins`: A list of positive integer coin denominations.
* `total`: The target amount.

### Returns

* The fewest number of coins needed to make `total`.
* `0` if `total` is less than or equal to `0`.
* `-1` if the total cannot be reached using the given coins.

---

## Example

```python
#!/usr/bin/python3

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
```

**Output**

```
7
-1
```

---

## Algorithm

The solution uses **Dynamic Programming**.

A table is created where each index represents an amount from `0` to `total`. Each entry stores the minimum number of coins required to make that amount.

For every amount, the algorithm checks every available coin and updates the minimum number of coins needed.

### Time Complexity

**O(n × total)**

* `n` = number of coin denominations

### Space Complexity

**O(total)**

---

## Author

Holberton School Student Rawan

