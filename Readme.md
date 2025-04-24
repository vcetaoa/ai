# Algorithm Compendium

This document summarizes key graph traversal, search, and problem-solving algorithms with their characteristics, use cases, and comparisons.

## Table of Contents
1. [Depth-First Search (DFS)](#depth-first-search-dfs)
2. [Breadth-First Search (BFS)](#breadth-first-search-bfs)
3. [A* Search](#a-search)
4. [8-Puzzle Solver](#8-puzzle-solver)
5. [Tower of Hanoi](#tower-of-hanoi)
6. [Bayesian Classifier](#bayesian-classifier)
7. [Tic-Tac-Toe AI](#tic-tac-toe-ai)

---

## Depth-First Search (DFS)

### Core Concept
Explores a graph by moving as deep as possible down one path before backtracking.

### Key Characteristics
- **Data Structure**: Stack (LIFO)
- **Approach**: "Go deep first"
- **Memory**: O(depth) - efficient for deep graphs
- **Completeness**: Yes (for finite graphs)
- **Optimality**: No (doesn't guarantee shortest path)

### When to Use
- ✔ Maze solving
- ✔ Topological sorting
- ✔ Cycle detection
- ✔ Puzzle games (e.g., Sudoku)
- ✖ Finding shortest paths

### Time Complexity
**Worst Case**: O(V + E)  
*(V = vertices, E = edges)*

---

## Breadth-First Search (BFS)

### Core Concept
Explores a graph level by level, visiting all neighbors at the present depth before moving deeper.

### Key Characteristics
- **Data Structure**: Queue (FIFO)
- **Approach**: "Explore wide first"
- **Memory**: O(width) - stores all nodes at current level
- **Completeness**: Yes (for finite graphs)
- **Optimality**: Yes (finds shortest path in unweighted graphs)

### When to Use
- ✔ Shortest path finding (unweighted graphs)
- ✔ Web crawling
- ✔ Social network analysis
- ✔ GPS navigation
- ✖ Deep graph exploration (memory intensive)

### Time Complexity
**Worst Case**: O(V + E)

---

## A* Search

### Core Concept
Informed search algorithm that finds the shortest path by combining:
- Actual path cost from start (g(n))
- Heuristic estimate to goal (h(n))

### Key Characteristics
- **Data Structure**: Priority Queue (min-heap)
- **Optimality**: Yes (with admissible heuristic)
- **Completeness**: Yes (if solution exists)
- **Memory**: O(b^d) - stores all explored nodes

### When to Use
- ✔ Pathfinding in games/maps
- ✔ Robot navigation
- ✔ Puzzle solving (8-puzzle)
- ✔ Route planning
- ✖ When no good heuristic exists

### Heuristic Requirements
- **Admissible**: Never overestimates true cost
- **Consistent**: h(n) ≤ cost(n→n') + h(n')

### Comparison Table

| Algorithm | Optimal | Complete | Uses Heuristic | Best For |
|-----------|---------|----------|----------------|----------|
| A*        | Yes     | Yes      | Yes            | Informed pathfinding |
| Dijkstra  | Yes     | Yes      | No             | Weighted graphs |
| BFS       | Yes*    | Yes      | No             | Unweighted graphs |
| DFS       | No      | Yes      | No             | Deep graphs |

*Only optimal for unweighted graphs

---

## 8-Puzzle Solver

### Implementation Details
- Uses A* algorithm with Manhattan distance heuristic
- **g(n)**: Actual moves from start
- **h(n)**: Sum of tile displacements
- Visualizes search tree with solution path

### Why A*?
- Guarantees shortest path
- Efficient heuristic guidance
- Complete (finds solution if exists)

---

## Tower of Hanoi

### Algorithm Used
**Recursive Backtracking**  
- **Time Complexity**: O(2ⁿ)
- **Space Complexity**: O(n) (recursion stack)

### Why This Approach?
- Solves in minimal moves (2ⁿ - 1)
- Classic recursion example
- Clear divide-and-conquer logic

---

## Bayesian Classifier

### Method
**Naive Bayes Classifier**  
Predicts probabilities using:
P(Weather | Evidence) ∝ P(Evidence | Weather) * P(Weather)

### Advantages
- Handles multiple evidence sources
- Clear probabilistic reasoning
- Easily extendable

### Complexity
- **Time**: O(n) for n evidence variables
- **Space**: O(1) (fixed probability tables)

---

## Tic-Tac-Toe AI

### Algorithm Components
| Component       | Algorithm                     | Key Feature                          |
|-----------------|-------------------------------|--------------------------------------|
| Win Check       | Brute-force pattern matching  | Checks all 8 winning combinations    |
| AI Move         | Greedy heuristic              | Win-block-random priority            |
| Game Flow       | Recursive state management    | Alternates turns                     |
| Player Input    | Input validation              | Ensures legal moves                  |

### Strategy
- Immediate win/block decisions
- One-step lookahead
- Recursive game state management
