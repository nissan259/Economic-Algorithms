import numpy as np
import cvxpy as cp

def equilibrium(vals, money):
    if len(vals) != len(money):
        raise ValueError("Mismatch in agents and budget sizes.")
    for row in vals:
        if any(val < 0 for val in row):
            raise ValueError("No negative preferences allowed.")

    n_agents = len(vals)
    n_items = len(vals[0])
    vals_arr = np.array(vals, dtype=float)
    budgets_arr = np.array(money, dtype=float)

    alloc = cp.Variable((n_agents, n_items), nonneg=True)
    logs = []
    for a_idx in range(n_agents):
        expr = 0
        for i_idx in range(n_items):
            expr += alloc[a_idx, i_idx] * vals_arr[a_idx, i_idx]
        logs.append(budgets_arr[a_idx] * cp.log(expr))

    cons = []
    for i_idx in range(n_items):
        cons.append(cp.sum(alloc[:, i_idx]) == 1)

    prob = cp.Problem(cp.Maximize(cp.sum(logs)), cons)
    prob.solve()

    if prob.status not in ["optimal", "optimal_inaccurate"]:
        raise RuntimeError("No optimal solution found.")

    final = alloc.value
    prices = []
    eps = 1e-6
    for i_idx in range(n_items):
        p_i = 0
        for a_idx in range(n_agents):
            if final[a_idx, i_idx] > eps:
                s = 0
                for i2 in range(n_items):
                    s += final[a_idx, i2] * vals_arr[a_idx, i2]
                if s > 0:
                    p_i = (budgets_arr[a_idx] * vals_arr[a_idx, i_idx]) / s
                    break
        prices.append(p_i)

    return {"allocation": final, "prices": prices}

def print_results_in_table(result):
    allocation = result["allocation"]
    prices = result["prices"]
    n_agents, n_items = allocation.shape

    print("=== ALLOCATION TABLE ===")
    hdr = ["Agent\\Item"] + [f"Item_{j+1}" for j in range(n_items)]
    print("  ".join(f"{col:>12}" for col in hdr))

    for a_idx in range(n_agents):
        row_vals = [f"{allocation[a_idx, i_idx]:>12.3f}" for i_idx in range(n_items)]
        print(f"{'Agent_' + str(a_idx+1):>12}  " + "  ".join(row_vals))

    print("\n=== PRICES ===")
    for i_idx, p_val in enumerate(prices):
        print(f"Item_{i_idx+1}: {p_val:.3f}")
    print()
