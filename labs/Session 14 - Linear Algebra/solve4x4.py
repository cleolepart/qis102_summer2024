# solve4x4.py
# This script solves the given system of linear equations using NumPy.

import numpy as np

def main():
    # Coefficient matrix
    A = np.array([
        [1, 2, 1, -1],
        [3, 2, 4, 4],
        [4, 4, 3, 4],
        [2, 0, 1, 5]
    ])
    
    # Constant terms
    b = np.array([5, 16, 22, 15])
    
    # Solve the system of equations using NumPy LinAlg package's solver
    x = np.linalg.solve(A, b)
    
    # Display the solution, start the counting from 1 instead of the default value of 0.
    print("Solution to the system of equations:")
    for i, val in enumerate(x, start=1):
        print(f"x{i} = {val}")

if __name__ == "__main__":
    main()
