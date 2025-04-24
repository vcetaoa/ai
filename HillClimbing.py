import copy
import random

def get_possible_moves(state):
    # Generate all valid moves possible from current state
    moves = []
    for from_peg in range(3):
        if not state[from_peg]:
            continue
        for to_peg in range(3):
            if from_peg != to_peg and (not state[to_peg] or state[from_peg][-1] < state[to_peg][-1]):
                new_state = copy.deepcopy(state)
                disk = new_state[from_peg].pop()
                new_state[to_peg].append(disk)
                moves.append((new_state, (from_peg, to_peg, disk)))
    return moves

def heuristic(state, num_disks):
    # Heuristic taken as the number of misplaced disks
    target_peg = state[2]
    misplaced = num_disks
    if len(target_peg) > 0:
        correct = 0
        for i in range(len(target_peg) - 1, -1, -1):  # Check from bottom to top
            if target_peg[i] == num_disks - i:
                correct += 1
            else:
                break
        misplaced -= correct
    return misplaced

def steepest_ascent_hill_climbing(num_disks, max_iterations=1000):
    initial_state = [list(range(num_disks, 0, -1)), [], []]
    goal_state = [[], [], list(range(num_disks, 0, -1))]
    current_state = initial_state
    best_state = current_state
    best_heuristic = heuristic(current_state, num_disks)
    solution_path = [(current_state, None)]
    plateau_count = 0
    iterations = 0

    while current_state != goal_state and iterations < max_iterations:
        current_heuristic = heuristic(current_state, num_disks)
        possible_moves = get_possible_moves(current_state)
        if not possible_moves:
            break

        # Calculate heuristics for all possible moves
        move_scores = [(heuristic(state, num_disks), state, move_info) for state, move_info in possible_moves]
        move_scores.sort()

        # Increases as we stay on plateau, decreases as we make progress
        bad_move_probability = min(0.3, (plateau_count / 50.0))

        # Either take the best move or make a random move based on probability
        if random.random() >= bad_move_probability:
            best_neighbor_heuristic, best_neighbor, move_info = move_scores[0]
            if best_neighbor_heuristic <= current_heuristic:
                current_state = best_neighbor
                plateau_count = 0
            else:
                plateau_count += 1
        else:
            _, random_neighbor, move_info = random.choice(move_scores)
            current_state = random_neighbor
            plateau_count = 0

        current_heuristic = heuristic(current_state, num_disks)
        if current_heuristic < best_heuristic:
            best_state = current_state
            best_heuristic = current_heuristic

        solution_path.append((current_state, move_info))

        if plateau_count > 30:
            current_state = copy.deepcopy(best_state)
            plateau_count = 0

        iterations += 1

    return solution_path, best_state, iterations

def print_solution(solution_path, num_disks):
    print("\nSolution path:")
    for i, (state, move_info) in enumerate(solution_path):
        h = heuristic(state, num_disks)
        if move_info:
            from_peg, to_peg, disk = move_info
            print(f"Step {i}: Move disk {disk} from peg {from_peg} to peg {to_peg}")
        print(f"State: {state}")
        print(f"Heuristic value: {h}\n")

def main():
    num_disks = 3
    solution_path, best_state, iterations = steepest_ascent_hill_climbing(num_disks)
    print_solution(solution_path, num_disks)
    print(f"Search completed in {iterations} iterations")
    print(f"Final heuristic value: {heuristic(best_state, num_disks)}")
    goal_state = [[], [], list(range(num_disks, 0, -1))]
    if best_state == goal_state:
        print("Solution found successfully!")
    else:
        print("Failed to find complete solution")

if __name__ == "__main__":
    main()


# ALgo:
# Core Algorithm: Modified Hill Climbing
# Primary Technique:
# Steepest Ascent Hill Climbing (greedy local search)
# With random restart capabilities to escape plateaus

# Why This Approach?
# Balance between greedy optimization and exploration
# Efficient for small disk counts (n ≤ 5)
# Demonstrates fundamental local search concepts

# Time Complexity: O(b·n) per iteration (b = branching factor)
# Space Complexity: O(n) (stores current path)

# Algorithm	                    Why Not Used        	        Why This Was Better
# BFS/DFS	                 Exponential space/time	            More memory efficient
# A*	                    Requires perfect heuristic	        Simpler to implement
# Genetic Algorithms	    Overkill for small problem          Faster convergence
# Minimax	                  No opponent in puzzle	             Unnecessary complexity