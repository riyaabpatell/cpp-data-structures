# C++ Data Structures

A collection of C++ data structure implementations focused on
understanding memory management, pointer manipulation, sorting,
and algorithmic efficiency.

This repository documents my work with fundamental data structures
and provides automated tests to verify correctness.

## Projects

### Dual-Sorted Doubly Linked List

**Location:** `linked-lists/dual-sorted-list.cpp`

A custom linked list that maintains two independent sorted
orderings of the same collection of records.

Each record contains a name and a weight. Rather than storing
two separate copies of the data, each node maintains two sets
of pointers, allowing the list to be traversed in either order.

**Key Features**
- Implemented in C++ using classes and pointers
- Maintains alphabetical ordering by name
- Maintains numerical ordering by weight
- Uses separate next and previous pointers for each ordering
- Supports insertion while preserving both sorted orderings
- Handles duplicate names and weights
- Includes automated tests for sorting and data integrity

**Concepts Demonstrated**
- Object-oriented programming
- Doubly linked lists
- Dynamic memory allocation
- Pointer manipulation
- Custom sorting logic
- Algorithm analysis
- Automated testing

## Technologies

- C++17
- Python 3 (automated testing)
- Clang++ compiler
- Python unittest framework
- Git and GitHub

## How to Run

Clone the repository:

```bash
git clone https://github.com/riyaabpatell/cpp-data-structures.git
cd cpp-data-structures
```

Compile the program:

```bash
clang++ -std=c++17 -Wall -Wextra -pedantic \
linked-lists/dual-sorted-list.cpp -o dual-sorted-list
```

Run the program:

```bash
./dual-sorted-list
```

The program prompts for 15 name-weight records and displays
the records sorted alphabetically and numerically.

## Automated Testing

The project includes three automated tests covering:

1. Correct alphabetical and numerical sorting
2. Handling duplicate names and weights
3. Preserving name-weight associations across both orderings

Run all tests from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

## Complexity Analysis

| Operation | Time Complexity |
|-----------|-----------------|
| Insert a record | O(n) |
| Traverse by name | O(n) |
| Traverse by weight | O(n) |
| Additional pointer storage per node | O(1) |

Each insertion searches for the correct position in both
sorted orderings. Traversal visits each node once.

## Project Background

This implementation was reconstructed and expanded from
data structures coursework to revisit fundamental C++
concepts and practice software testing.

The repository is intended to grow as I continue developing
and documenting additional data structure implementations.
