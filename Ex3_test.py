import unittest
from Ex3 import alloc, show, get_input

def round_matrix(mat):
    return [[round(val, 2) for val in row] for row in mat]

class TestAllocation(unittest.TestCase):
    def test_1(self):
        mat = [[81, 19, 1], [70, 1, 29]]
        expected = [
            [0.53, 1.00, 0.00],
            [0.47, 0.00, 1.00]
        ]
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)

    def test_2(self):
        mat = [[1, 1], [1, 1]]
        expected = [
            [0.50, 0.50],
            [0.50, 0.50]
        ]
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)

    def test_3(self):
        mat = [[100, 1], [1, 100]]
        expected = [
            [1.00, 0.00],
            [0.00, 1.00]
        ]
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)

    def test_4(self):
        mat = [[0, 0, 0], [10, 5, 1]]
        expected = [
            [0.88, 0.75, 0.53],
            [0.12, 0.25, 0.47]
        ]
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)

    def test_5(self):
        mat = [[100, 0, 0], [0, 100, 0], [0, 0, 100]]
        expected = [
            [1.00, -0.00, -0.00],
            [-0.00, 1.00, -0.00],
            [-0.00, -0.00, 1.00]
        ]
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)

    def test_6(self):
        mat = [[100, 100, 100], [1, 1, 1], [1, 1, 1]]
        expected = [
            [0.00, 0.00, 0.00],
            [0.50, 0.50, 0.50],
            [0.50, 0.50, 0.50]
        ]
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)

    def test_7(self):
        mat = [[50, 0, 0], [50, 50, 50]]
        expected = [
            [1.00, 0.43, 0.43],
            [-0.00, 0.57, 0.57]
        ]
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    mode = input("Enter 't' to run tests or 'm' for manual input: ").strip().lower()

    if mode == 't':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    elif mode == 'm':
        mat = get_input()
        result = alloc(mat)
        show(result)
    else:
        print("Invalid option selected.")
