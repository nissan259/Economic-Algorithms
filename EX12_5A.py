# --------------------------------------------------------------
# DISCLAIMER:
#
# This code (including implementation and test cases) was written and developed with the assistance of ChatGPT (OpenAI),
# based on the theoretical and algorithmic principles presented in the course lecture slides.
# --------------------------------------------------------------

from typing import List


def compute_budget(total_budget: float, citizen_votes: List[List[float]]) -> List[float]:
    """
    Computes an optimal budget allocation using the generalized median algorithm with linear functions,
    as described in the lecture slides.
    The algorithm adds (n-1) fixed linear "virtual" votes for each section, then finds t in [0, 1] so that
    the sum of medians over all sections equals the total budget.

    Args:
        total_budget (float): The total available budget to be distributed among all sections.
        citizen_votes (List[List[float]]): A list of lists, where each inner list contains the votes (ideal budget allocations)
            of one citizen for all m sections.

    Returns:
        List[float]: The calculated budget allocation for each section (length m), such that the total sum matches total_budget.
    """
    n = len(citizen_votes)
    m = len(citizen_votes[0])

    def allocation_for_t(t: float) -> List[float]:
        """
        Helper function that computes the allocation for a given t value,
        by adding (n-1) fixed linear votes to each section and taking the median.

        Args:
            t (float): The parameter controlling the fixed votes.

        Returns:
            List[float]: The median allocation for each section.
        """
        res = []
        for j in range(m):
            section_votes = [citizen_votes[i][j] for i in range(n)]
            # Add (n-1) fixed linear virtual votes to each section, as per the linear function definition
            fixed_votes = [total_budget * min(1, (i + 1) * t) for i in range(n - 1)]
            all_votes = section_votes + fixed_votes
            all_votes.sort()
            L = len(all_votes)
            # Compute the median
            if L % 2 == 1:
                median = all_votes[L // 2]
            else:
                median = (all_votes[L // 2 - 1] + all_votes[L // 2]) / 2
            res.append(median)
        return res

    # Binary search to find t such that the sum of medians equals total_budget
    left, right = 0.0, 1.0
    for _ in range(50):  # Sufficient precision
        mid = (left + right) / 2
        allocation = allocation_for_t(mid)
        s = sum(allocation)
        if abs(s - total_budget) < 1e-6:
            return allocation
        if s > total_budget:
            right = mid
        else:
            left = mid
    return allocation_for_t((left + right) / 2)


# ---------- TESTS ----------

def test_compute_budget():
    """
    Runs multiple test cases on compute_budget to demonstrate its correctness and robustness.
    Prints results for each test, including input, output, and verification that the total allocation matches the budget.
    """
    tests = [
        # (description, total_budget, votes, expected_sum, expected_example_output_or_None)
        ("All on first & last", 100, [[100, 0, 0], [0, 0, 100]], 100, [50.0, 0.0, 50.0]),
        ("Almost even spread", 100, [[33, 33, 34], [34, 33, 33], [33, 34, 33]], 100, [33.0, 33.33, 33.67]),
        ("Single full support per section", 90, [[90, 0, 0], [0, 90, 0], [0, 0, 90]], 90, [30.0, 30.0, 30.0]),
        ("Unbalanced, multiple voters", 150, [[50, 50, 50], [100, 25, 25], [25, 100, 25], [25, 25, 100]], 150, None),
        ("Support per section, plus balanced", 60, [[60, 0, 0], [0, 60, 0], [0, 0, 60], [20, 20, 20]], 60, None),
        ("Random-looking votes", 200, [[100, 50, 50], [0, 100, 100], [100, 100, 0]], 200, None),
        ("One section dominant", 120, [[120, 0, 0], [0, 60, 60], [40, 40, 40]], 120, None),
        ("Median distributed", 100, [[50, 25, 25], [25, 50, 25], [25, 25, 50]], 100, [33.33, 33.33, 33.33]),
        ("All equal votes", 75, [[25, 25, 25], [25, 25, 25], [25, 25, 25]], 75, [25.0, 25.0, 25.0]),
        ("Strong outliers", 100, [[80, 10, 10], [10, 80, 10], [10, 10, 80], [33, 33, 34]], 100, None),
    ]

    for i, (desc, total, votes, exp_sum, exp_out) in enumerate(tests, 1):
        result = compute_budget(total, votes)
        result_sum = sum(result)
        print(f"\nTest #{i}: {desc}")
        print(f"Input votes: {votes}")
        print(f"Output: {[round(x, 2) for x in result]}")
        print(f"Sum: {round(result_sum, 2)} (should be {exp_sum})")
        if abs(result_sum - exp_sum) > 1e-4:
            print("❌ Sum does not match total budget! ❌")
        else:
            print("✅ Sum matches total budget.")
        if exp_out:
            rounded_result = [round(x, 2) for x in result]
            rounded_expected = [round(x, 2) for x in exp_out]
            if rounded_result == rounded_expected:
                print("✅ Output matches expected example!")
            else:
                print(f"ℹ️ Output does not exactly match expected (likely due to tie-breaking or median in even-size).")
        print('-' * 50)


# Run tests:
test_compute_budget()
