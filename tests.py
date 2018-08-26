# coding=utf-8

from two_sum import Solution as twoSumSolution
import unittest


class TestPython(unittest.TestCase):

    def test_list(self):
        self.assertEqual(range(1, 10), range(0, 10)[1:])

    def test_list_index(self):
        self.assertEqual(4, ([0, 0, 1, 1, 2, 2].index(2)))
        self.assertEqual(3, ([0, 0, 1, 1, 2, 2].index(1, 3)))

    def test_list_in(self):
        self.assertTrue(2 in [0, 0, 1, 1, 2, 2])


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.ts = twoSumSolution()

    def test_two_sum(self):
        self.assertEqual([0, 1], self.ts.twoSum([2, 7, 9, 11, 15], 9))
        self.assertEqual([1, 2], self.ts.twoSum([2, 0, 9, 11, 15], 9))
        self.assertEqual([1, 4], self.ts.twoSum([2, 0, 0, 11, 9], 9))
        self.assertEqual([1, 2], self.ts.twoSum([3, 2, 4], 6))
        self.assertEqual([None, None], self.ts.twoSum([], 9))
        self.assertEqual([None, None], self.ts.twoSum([9], 9))

    def test_two_sum_performance(self):
        self.assertEqual(
            [0, 1], self.ts.twoSumPerformance([2, 7, 9, 11, 15], 9))
        self.assertEqual(
            [1, 2], self.ts.twoSumPerformance([2, 0, 9, 11, 15], 9))
        self.assertEqual(
            [1, 4], self.ts.twoSumPerformance([2, 0, 0, 11, 9], 9))
        self.assertEqual([1, 2], self.ts.twoSumPerformance([3, 2, 4], 6))
        self.assertEqual([None, None], self.ts.twoSumPerformance([], 9))
        self.assertEqual([None, None], self.ts.twoSumPerformance([9], 9))
        self.assertEqual([0, 3], self.ts.twoSumPerformance([0, 4, 3, 0], 0))
        self.assertEqual(
            [2, 4], self.ts.twoSumPerformance([-1, -2, -3, -4, -5], -8))

        nums = filter(lambda num: num % 2 == 0, range(0, 25197))
        nums[8012], target = -1, 16021
        self.assertEqual([8011, 8012], self.ts.twoSumPerformance(nums, target))


if __name__ == "__main__":
    unittest.main()