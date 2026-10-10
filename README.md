
# Dual-Sorted Doubly Linked List (C++)

A C++ implementation of a custom linked-list data
structure that maintains records in two independent
sorted orders without duplicating the underlying nodes.

## Overview

Each node stores a name and a weight, along with
four pointers:

- `namePrev` and `nameNext`
- `weightPrev` and `weightNext`

These pointers allow the same records to be traversed
alphabetically by name or numerically by weight.

## Features

- Dynamically allocates nodes
- Maintains two sorted doubly linked chains
- Supports insertion in both sorted orders
- Traverses and prints records by name or weight
- Releases dynamically allocated memory
- Prevents accidental copying of owning pointers

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Insert record | O(n) |
| Traverse by name | O(n) |
| Traverse by weight | O(n) |
| Store n records | O(n) space |

## Technologies

- C++
- Pointers and dynamic memory management
- Doubly linked lists
- Object-oriented programming

## How to Run

Compile:

```bash
clang++ -std=c++17 -Wall -Wextra -pedantic dual-sorted-list.cpp -o dual-sorted-list
```

Run:

```bash
./dual-sorted-list
```

Enter 15 name-and-weight pairs when prompted.

## Background

Based on a data structures coursework assignment, with the implementation reconstructed and reviewed for this repository.
