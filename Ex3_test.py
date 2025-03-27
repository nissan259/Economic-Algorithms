import unittest
from Ex3 import alloc, show, get_input
from colorama import init, Fore, Style

init(autoreset=True)

def round_matrix(mat):
    return [[round(val, 2) for val in row] for row in mat]

class TestAllocation(unittest.TestCase):
    def assertAllocEqual(self, mat, expected):
        result = round_matrix(alloc(mat))
        self.assertEqual(result, expected)

    def test_1(self):
        self.assertAllocEqual([[81, 19, 1], [70, 1, 29]],
                              [[0.53, 1.00, 0.00], [0.47, 0.00, 1.00]])

    def test_2(self):
        self.assertAllocEqual([[1, 1], [1, 1]],
                              [[0.50, 0.50], [0.50, 0.50]])

    def test_3(self):
        self.assertAllocEqual([[100, 1], [1, 100]],
                              [[1.00, 0.00], [0.00, 1.00]])

    def test_4(self):
        self.assertAllocEqual([[0, 0, 0], [10, 5, 1]],
                              [[0.88, 0.75, 0.53], [0.12, 0.25, 0.47]])

    def test_5(self):
        self.assertAllocEqual([[100, 0, 0], [0, 100, 0], [0, 0, 100]],
                              [[1.00, -0.00, -0.00], [-0.00, 1.00, -0.00], [-0.00, -0.00, 1.00]])

    def test_6(self):
        self.assertAllocEqual([[100, 100, 100], [1, 1, 1], [1, 1, 1]],
                              [[0.00, 0.00, 0.00], [0.50, 0.50, 0.50], [0.50, 0.50, 0.50]])

    def test_7(self):
        self.assertAllocEqual([[50, 0, 0], [50, 50, 50]],
                              [[1.00, 0.43, 0.43], [-0.00, 0.57, 0.57]])


def run_tests_with_style():
    print(Fore.CYAN + Style.BRIGHT + "\n📊 Running Allocation Tests...\n" + "-" * 40)
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(TestAllocation))
    print("-" * 40)
    if result.wasSuccessful():
        print(Fore.GREEN + Style.BRIGHT + "✅ All tests passed successfully!\n")
    else:
        print(Fore.RED + Style.BRIGHT + f"❌ {len(result.failures)} test(s) failed.\n")


if __name__ == "__main__":
    print(Fore.YELLOW + "Welcome to the Allocation Program!")
    mode = input("Enter 't' to run tests or 'm' for manual input: ").strip().lower()

    if mode == 't':
        run_tests_with_style()
    elif mode == 'm':
        mat = get_input()
        result = alloc(mat)
        show(result)
    else:
        print(Fore.RED + "Invalid option selected.")
