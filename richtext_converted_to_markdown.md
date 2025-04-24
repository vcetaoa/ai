\# Algorithm Collection

This repository contains implementations of various classical algorithms and problem-solving techniques in both Python and Prolog. Below is a comprehensive overview of each algorithm and its implementation.

\## Search Algorithms

\### 1. Depth-First Search (DFS) - \`01\_dfs.py\`

Depth-First Search is a graph traversal algorithm that explores as far as possible along each branch before backtracking.

\*\*Key Characteristics:\*\*

\- Uses a stack (or recursion) for traversal

\- Memory efficient compared to BFS

\- Not guaranteed to find the shortest path

\- Time Complexity: O(V + E) where V is vertices and E is edges

\- Space Complexity: O(V) in worst case

\*\*Applications:\*\*

\- Topological sorting

\- Finding connected components

\- Maze generation and solving

\- Cycle detection in graphs

\### 2. Breadth-First Search (BFS) - \`02\_bfs.py\`

Breadth-First Search is a graph traversal algorithm that explores all neighbors at the present depth prior to moving to nodes at the next depth level.

\*\*Key Characteristics:\*\*

\- Uses a queue for traversal

\- Guaranteed to find the shortest path in unweighted graphs

\- Time Complexity: O(V + E)

\- Space Complexity: O(V)

\*\*Applications:\*\*

\- Shortest path in unweighted graphs

\- Peer-to-peer networks

\- Web crawlers

\- Social networking features (e.g., "friends of friends")

\- GPS navigation systems

\### 3. A\* Search - \`03\_A\_star.py\`

A\* (A-Star) is an informed search algorithm that finds the shortest path from a start node to a goal node. It uses heuristics to guide the search process.

\*\*Key Characteristics:\*\*

\- Combines features of Dijkstra's algorithm and greedy best-first search

\- Uses f(n) = g(n) + h(n) where:

\- g(n) is the cost from start node to current node

\- h(n) is the heuristic estimate from current node to goal

\- Complete and optimal when using admissible heuristics

\- Time and Space Complexity: O(b^d) where b is branching factor and d is depth

\*\*Applications:\*\*

\- Pathfinding in games

\- Robot navigation

\- Route planning in maps

\- Puzzle solving

\## Classic Problems

\### 4. Eight Puzzle - \`04\_Eight\_Puzzle.py\`

The Eight Puzzle is a sliding puzzle consisting of a frame of numbered tiles in random order with one tile missing.

\*\*Algorithm Used:\*\*

\- A\* search with Manhattan distance or misplaced tiles heuristic

\- State space search

\*\*Key Concepts:\*\*

\- State representation

\- Goal state definition

\- Move generation

\- Heuristic evaluation

\### 5. Tower of Hanoi - \`05\_Tower\_Hanoi.py\`

Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes.

\*\*Algorithm Used:\*\*

\- Recursive solution

\- Divide and conquer approach

\*\*Key Characteristics:\*\*

\- Optimal solution requires 2^n - 1 moves for n disks

\- Time Complexity: O(2^n)

\- Space Complexity: O(n) for the recursive call stack

\## Knowledge Representation & Reasoning (Prolog)

\### 6. Knowledge Base - \`06\_knowledge\_base.pl\`

Implementation of a knowledge base system in Prolog for logical reasoning and inference.

\*\*Key Concepts:\*\*

\- Facts and rules representation

\- Logical inference

\- Query answering

\- Knowledge representation

\*\*Applications:\*\*

\- Expert systems

\- Semantic web

\- Rule-based systems

\- Automated reasoning

\### 7. Diagnosis System - \`07\_diagnosis.pl\`

A logical diagnosis system implemented in Prolog that can identify causes based on symptoms or observations.

\*\*Key Concepts:\*\*

\- Backward chaining

\- Rule-based reasoning

\- Symptom-disease relationships

\- Probabilistic reasoning (if implemented)

\*\*Applications:\*\*

\- Medical diagnosis

\- System troubleshooting

\- Fault detection

\- Decision support systems

\## Weather & Game Implementations

\### 8. Weather Prediction - \`08\_Weather\_Prediction.pl\` & \`08\_Weather\_Prediction.py\`

Weather prediction implementations in both Prolog and Python, demonstrating different paradigms for the same problem.

\*\*Algorithms Used:\*\*

\- Rule-based systems (Prolog)

\- Machine learning techniques (Python):

\- Decision trees

\- Neural networks

\- Statistical methods

\*\*Key Concepts:\*\*

\- Feature extraction

\- Pattern recognition

\- Time series analysis

\- Probabilistic forecasting

\### 9. Tic Tac Toe - \`09\_Tic\_Tac\_Toe.pl\` & \`09\_Tic\_Tac\_Toe.py\`

Implementation of the Tic Tac Toe game in both Prolog and Python.

\*\*Algorithms Used:\*\*

\- Minimax algorithm

\- Alpha-beta pruning

\- Game state evaluation

\- Move generation

\*\*Key Concepts:\*\*

\- Game theory

\- Adversarial search

\- State space representation

\- Perfect information games

\## Implementation Differences

\### Python vs Prolog Approaches

\*\*Python:\*\*

\- Imperative and object-oriented

\- Enhanced visualization capabilities

\- Better for numerical computations and machine learning

\- More straightforward for algorithm implementation with complex data structures

\*\*Prolog:\*\*

\- Declarative and logic-based

\- Natural fit for knowledge representation and rule-based systems

\- Built-in backtracking and unification

\- Succinct for certain AI problems like rule-based reasoning

\## Usage

Each file can be run independently. Python files can be executed with Python interpreter:

\`\`\`bash

python 01\_dfs.py

\`\`\`

Prolog files can be consulted in a Prolog interpreter like SWI-Prolog:

\`\`\`bash

swipl -s 06\_knowledge\_base.pl

\`\`\`

\## Requirements

\- Python 3.x

\- SWI-Prolog (for Prolog implementations)