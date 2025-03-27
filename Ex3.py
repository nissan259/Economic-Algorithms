import cvxpy as cp
import numpy as np

def alloc(mat):
    mat = np.array(mat, dtype=float)
    n, m = mat.shape
    x = cp.Variable((n, m))
    t = cp.Variable()

    cons = []
    for j in range(m):
        cons.append(cp.sum(x[:, j]) == 1)
    cons.append(x >= 0)
    for i in range(n):
        cons.append(mat[i, :] @ x[i, :] >= t)

    prob = cp.Problem(cp.Maximize(t), cons)
    prob.solve()

    res = []
    for i in range(n):
        row = [round(x.value[i, j], 2) for j in range(m)]
        res.append(row)
    return res

def show(res):
    for i in range(len(res)):
        s = ", ".join([f"{res[i][j]:.2f} of resource #{j+1}" for j in range(len(res[i]))])
        print(f"Agent #{i+1} gets {s}.")

def get_input():
    try:
        n = int(input("Enter number of agents (rows): "))
        m = int(input("Enter number of resources (columns): "))
    except ValueError:
        raise ValueError("Please enter valid integers.")

    mat = []
    print("Enter each row of values separated by spaces:")
    for i in range(n):
        row_input = input(f"Row #{i+1}: ")
        row = list(map(float, row_input.strip().split()))
        if len(row) != m:
            raise ValueError("Number of values doesn't match number of columns.")
        mat.append(row)
    return mat
