"""
This code was written with the assistance of ChatGPT (OpenAI).
Checks using max-flow whether a budget is decomposable.
Determines if it is possible to split the budget and the citizens' preferences so that:
(a) Each topic receives its allocated amount,
(b) Each citizen pays their equal share of the total sum,
(c) No one pays for a topic they do not wish to support.
"""

import networkx as nx

def is_decomposable_flow(budget, preferences):
    """
    Determines whether the budget is decomposable given the citizens' preferences.

    Parameters
    ----------
    budget : list[float]
        budget[j] is the allocated amount for topic j.
    preferences : list[set[int]]
        preferences[i] is the set of topics citizen i is willing to support.

    Returns
    -------
    (bool, dict)
        - True and a flow dictionary if a decomposition exists.
        - False and the flow dictionary otherwise.
    """
    n = len(preferences)
    m = len(budget)
    total = sum(budget)
    if n == 0 or m == 0 or total == 0:
        # Trivial case: zero budget, or no topics/citizens – always decomposable
        return True, {}

    G = nx.DiGraph()
    src, sink = 'src', 'sink'

    # Source -> Citizens
    for i in range(n):
        G.add_edge(src, f'citizen_{i}', capacity=total/n)

    # Citizens -> Topics (only if allowed)
    for i, prefs in enumerate(preferences):
        for j in prefs:
            G.add_edge(f'citizen_{i}', f'topic_{j}', capacity=float('inf'))

    # Topics -> Sink
    for j in range(m):
        G.add_edge(f'topic_{j}', sink, capacity=budget[j])

    # Compute max-flow
    flow_value, flow_dict = nx.maximum_flow(G, src, sink)
    return flow_value >= total, flow_dict

########################
#        TESTS         #
########################

def pretty_print_flow(flow_dict, n, m):
    for i in range(n):
        out = []
        for j in range(m):
            amt = flow_dict.get(f'citizen_{i}', {}).get(f'topic_{j}', 0)
            if amt > 1e-6:
                out.append(f"topic {j}: {amt}")
        if out:
            print(f"citizen {i}: " + ", ".join(out))

def run_tests():
    # Test 1: Classic example - should be decomposable
    budget = [400, 50, 50, 0]
    preferences = [
        {0, 1},
        {0, 2},
        {0, 3},
        {1, 2},
        {0}
    ]
    possible, flow = is_decomposable_flow(budget, preferences)
    print("Test 1:", "Pass" if possible else "Fail")
    pretty_print_flow(flow, len(preferences), len(budget))
    print("-" * 40)

    # Test 2: No preferences at all - impossible (budget > 0)
    budget = [10, 20]
    preferences = [set(), set()]
    possible, flow = is_decomposable_flow(budget, preferences)
    print("Test 2:", "Pass" if not possible else "Fail")
    print("-" * 40)

    # Test 3: All topics covered, but only one citizen likes both
    budget = [50, 50]
    preferences = [{0, 1}, {0}, {1}]
    possible, flow = is_decomposable_flow(budget, preferences)
    print("Test 3:", "Pass" if possible else "Fail")
    pretty_print_flow(flow, len(preferences), len(budget))
    print("-" * 40)

    # Test 4: Not enough coverage - topic 1 has nobody supporting
    budget = [20, 30]
    preferences = [{0}, {0}]
    possible, flow = is_decomposable_flow(budget, preferences)
    print("Test 4:", "Pass" if not possible else "Fail")
    print("-" * 40)

    # Test 5: Trivial case, zero budget
    budget = [0, 0, 0]
    preferences = [set(), set()]
    possible, flow = is_decomposable_flow(budget, preferences)
    print("Test 5:", "Pass" if possible else "Fail")
    print("-" * 40)

    # Test 6: Example from the question (should be Pass)
    budget = [400, 50, 50, 0]
    preferences = [
        {0, 1},
        {0, 2},
        {0, 3},
        {1, 2},
        {0}
    ]
    print("Test 6: Example from question (should be Pass)")
    possible, flow = is_decomposable_flow(budget, preferences)
    print("Result:", "Pass" if possible else "Fail")
    if possible:
        pretty_print_flow(flow, len(preferences), len(budget))
    print("-" * 40)

if __name__ == "__main__":
    run_tests()
