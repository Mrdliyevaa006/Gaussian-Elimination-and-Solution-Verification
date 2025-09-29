# Gaussian Elimination and Solution Verification 📈

## Purpose of the Project

In machine learning models, each feature is assigned a weight, which indicates how much that feature influences the model’s output. For example, in tabular data, a feature could be anything – in a dataset about house prices, it could be the number of rooms, the location, etc. These weights are unknown, and we find them by solving the system (Ax = b).

**Note:** The Gaussian Elimination method is implemented from scratch in this project to fully understand the step-by-step process of solving linear systems.

---
## Part 1: Gaussian Elimination from Scratch

### Steps:

1. **Form the Augmented Matrix** – Combine the coefficient matrix (A) with the constants vector (b) → ([A|b]).
2. **Forward Elimination** – Transform the matrix into an upper triangular form by selecting pivot elements, swapping rows if a pivot is zero, and eliminating the entries below each pivot.
3. **Back Substitution** – Start from the last row, solve for each variable, and substitute the found values into the rows above to determine all unknowns.
4. **Special Cases** –

   * If a row has all zeros in the coefficient part but a non-zero constant → No solution.
   * If there are fewer pivots than variables → Infinite solutions.

### Explanation of the Python Code

* The augmented matrix is created by appending each element of (b) to its corresponding row in (A) using the `enumerate` function.
* **Forward Elimination:**

  * Iterate over each row, select the diagonal element as the pivot.
  * If the pivot is zero, swap with a row below having a non-zero element.
  * Normalize the pivot row by dividing all elements by the pivot.
  * Eliminate all values below the pivot by subtracting multiples of the pivot row.
* **Back Substitution:**

  * Check for “No Solution” (0 = non-zero) and “Infinite Solutions” (fewer pivots than variables).
  * Solve unique solutions starting from the last row and moving upward.

**Example Output:**

```
Upper triangular matrix:
[[1.0, 1.0, 1.75, 0.25],
 [0.0, 1.0, 3.0, 1.0],
 [-0.0, -0.0, 1.0, 0.04]]

Solution (from scratch): ([-0.7, 0.88, 0.04], 3)
```

---

## Part 2: NumPy Verification

* Using NumPy arrays instead of Python lists, we solve the system with `np.linalg.solve`.
* This checks the solution efficiently and confirms that the scratch implementation is correct.

**Example Output:**

```
Solution (NumPy): [-0.7  0.88  0.04]
```

