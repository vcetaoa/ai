# Algorithm Collection

This repository contains implementations of classical algorithms and problem-solving techniques in Python and Prolog, demonstrating different programming paradigms for artificial intelligence applications.

### 🔍 Search Algorithms  
| File | Algorithm | Description |  
|------|-----------|-------------|  
| `01_dfs.py` | Depth-First Search | Uninformed graph traversal |  
| `02_bfs.py` | Breadth-First Search | Shortest path finder |  
| `03_A_star.py` | A* Search | Heuristic-based pathfinding |  

### 🧩 Puzzle Solvers  
| File | Algorithm | Description |  
|------|-----------|-------------|  
| `04_Eight_Puzzle.py` | A* Algorithm | 8-tile sliding puzzle solver |  
| `05_Tower_Hanoi.py` | Recursive Solution | Classic tower puzzle |  

### 🤖 Logic Programming  
| File | Type | Description |  
|------|------|-------------|  
| `06_knowledge_base.pl` | Prolog KB | Rule-based knowledge system |  
| `07_diagnosis.pl` | Prolog | Diagnostic expert system |  

### 🌦️ Weather Prediction  
| File | Language | Approach |  
|------|----------|----------|  
| `08_Weather_Prediction.pl` | Prolog | Logic-based prediction |  
| `09_Weather_Prediction.py` | Python | Data-driven prediction |  

### 🎮 Game AI  
| File | Language | Algorithm |  
|------|----------|-----------|  
| `09_Tic_tac_toe.pl` | Prolog | Rule-based AI |  
| `09_Tic_tac_toe.py` | Python | Minimax algorithm |  

---


## Table of Contents
- [Search Algorithms](#search-algorithms)
- [Classic Problems](#classic-problems)
- [Knowledge Representation & Reasoning](#knowledge-representation--reasoning)
- [Applications](#applications)
- [Implementation Differences](#implementation-differences)
- [Usage](#usage)
- [Requirements](#requirements)

## Search Algorithms

### 1. Depth-First Search (DFS) - `01_dfs.py`
**Algorithm:**  
- Recursive/stack-based graph traversal
- Explores deepest nodes first

**Complexity:**  
- Time: O(V + E)
- Space: O(V)

**Applications:**  
- Maze solving
- Topological sorting
- Cycle detection

### 2. Breadth-First Search (BFS) - `02_bfs.py`
**Algorithm:**  
- Queue-based graph traversal
- Explores nearest nodes first

**Complexity:**  
- Time: O(V + E)
- Space: O(V)

**Applications:**  
- Shortest path in unweighted graphs
- Web crawling
- Social network analysis

### 3. A* Search - `03_A_star.py`
**Algorithm:**  
- Informed search using heuristic h(n)
- Combines g(n) (path cost) and h(n) (heuristic)

**Complexity:**  
- Time: O(b^d)
- Space: O(b^d)

**Applications:**  
- Pathfinding in games
- Robotics navigation
- Puzzle solving

## Classic Problems

### 4. Eight Puzzle - `04_Eight_Puzzle.py`
**Solution:**  
- A* search with Manhattan distance heuristic
- State space representation

**Key Aspects:**  
- Sliding tile puzzle
- Heuristic evaluation
- Move generation

### 5. Tower of Hanoi - `05_Tower_Hanoi.py`
**Solution:**  
- Recursive divide-and-conquer
- Minimal move solution (2^n - 1 moves)

**Complexity:**  
- Time: O(2^n)
- Space: O(n)

## Knowledge Representation & Reasoning

### 6. Knowledge Base - `06_knowledge_base.pl`
**Features:**  
- Facts and rules representation
- Logical inference engine
- Query answering system

### 7. Diagnosis System - `07_diagnosis.pl`
**Features:**  
- Rule-based reasoning
- Symptom-cause relationships
- Backward chaining

## Applications

### 8. Weather Prediction
| File | Approach |
|------|----------|
| `08_Weather_Prediction.pl` | Rule-based system |
| `09_Weather_Prediction.py` | Machine learning |

### 9. Tic Tac Toe
| File | Algorithm |
|------|-----------|
| `09_Tic_Tac_Toe.pl` | Rule-based AI |
| `09_Tic_Tac_Toe.py` | Minimax with alpha-beta pruning |

## Implementation Differences

| Aspect | Python | Prolog |
|--------|--------|--------|
| Paradigm | Imperative/OOP | Declarative/Logic |
| Strengths | Numerical computation, ML | Knowledge representation |
| Data Structures | Rich collections | Term-based |
| Search | Explicit implementation | Built-in backtracking |

## Usage

**Python files:**
```bash
python3 filename.py

