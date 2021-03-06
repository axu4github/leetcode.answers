# coding=utf-8

from two_sum import Solution as twoSumSolution
from longest_common_prefix import Solution as LongestCommonPrefix
from reverse import Solution as Reverse
from is_palindrome import Solution as IsPalindrome
from is_valid import Solution as IsValid
from merge_two_lists import Solution as MergeTwoLists
from three_sum import Solution as ThreeSum
from transpose_matrix import Solution as TransposeMatrix
from array_partition_i import Solution as ArrayPartitionI
from pascals_triangle import Solution as PascalsTriangle
from reshape_the_matrix import Solution as ReshapeTheMatrix
from toeplitz_matrix import Solution as ToeplitzMatrix
from majority_element import Solution as MajorityElement
from move_zeroes import Solution as MoveZeroes
from max_area_of_island import Solution as MaxAreaOfIsland
from reverse_string import Solution as ReverseString
from nim_game import Solution as NimGame
from reverse_words_in_a_string_iii import Solution as ReverseWordsIII
from delete_node_in_a_linked_list import Solution as DeleteNode
from reverse_linked_list import Solution as ReverseList
from single_number import Solution as SingleNumber
from commons.utils import Utils
import unittest

IGNORE_OTHER_PERFORMANCE_TESTS = True


class TestSingleNumber(unittest.TestCase):

    def setUp(self):
        self.sn = SingleNumber()

    def test_single_number(self):
        self.assertEqual(1, self.sn.singleNumber([2, 2, 1]))
        self.assertEqual(4, self.sn.singleNumber([4, 1, 2, 1, 2]))


class TestReverseList(unittest.TestCase):

    def setUp(self):
        self.rl = ReverseList()

    def test_reverse_list(self):
        self.assertEqual(
            [None, 5, 4, 3, 2, 1],
            Utils.listnode_to_list(
                self.rl.reverseList(
                    Utils.list_to_listnode([1, 2, 3, 4, 5, None]))))


class TestDeleteNode(unittest.TestCase):
    # TODO

    def setUp(self):
        self.dn = DeleteNode()

    def test_delete_node(self):
        pass


class TestReverseWordsIII(unittest.TestCase):

    def setUp(self):
        self.rw3 = ReverseWordsIII()

    def test_reverse_words(self):
        self.assertEqual(
            "s'teL ekat edoCteeL tsetnoc",
            self.rw3.reverseWords("Let's take LeetCode contest"))


class TestNimGame(unittest.TestCase):

    def setUp(self):
        self.ng = NimGame()

    def test_can_win_nim(self):
        self.assertTrue(not self.ng.canWinNim(4))
        self.assertTrue(self.ng.canWinNim(3))
        self.assertTrue(self.ng.canWinNim(5))


class TestReverseString(unittest.TestCase):

    def setUp(self):
        self.rs = ReverseString()

    def test_reverse_string(self):
        self.assertEqual("olleh", self.rs.reverseString("hello"))


class TestMaxAreaOfIsland(unittest.TestCase):

    def setUp(self):
        self.maoi = MaxAreaOfIsland()

    def test_max_area_of_island(self):
        self.assertEqual(
            6,
            self.maoi.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
                                      ))


class TestMoveZeroes(unittest.TestCase):

    def setUp(self):
        self.mz = MoveZeroes()

    def test_move_zeroes(self):
        nums = [0, 1, 0, 3, 12]
        self.mz.moveZeroes(nums)
        self.assertEqual([1, 3, 12, 0, 0], nums)

        nums = [0, 0, 1]
        self.mz.moveZeroes(nums)
        self.assertEqual([1, 0, 0], nums)


class TestMajorityElement(unittest.TestCase):

    def setUp(self):
        self.me = MajorityElement()

    def test_majority_element(self):
        self.assertEqual(3, self.me.majorityElement([3, 2, 3]))
        self.assertEqual(2, self.me.majorityElement([2, 2, 1, 1, 1, 2, 2]))


class TestToeplitzMatrix(unittest.TestCase):

    def setUp(self):
        self.tm = ToeplitzMatrix()

    def test_toeplitz_matrix(self):
        self.assertEqual(
            True, self.tm.isToeplitzMatrix([
                [1, 2, 3, 4],
                [5, 1, 2, 3],
                [9, 5, 1, 2]
            ]))
        self.assertEqual(
            False, self.tm.isToeplitzMatrix([
                [1, 2],
                [2, 2]
            ]))


class TestReshapeTheMatrix(unittest.TestCase):

    def setUp(self):
        self.rtm = ReshapeTheMatrix()

    def test_reshape_the_matrix(self):
        self.assertEqual(
            [[1, 2, 3, 4]], self.rtm.matrixReshape([[1, 2], [3, 4]], 1, 4))
        self.assertEqual(
            [[1, 2], [3, 4]], self.rtm.matrixReshape([[1, 2], [3, 4]], 2, 4))
        self.assertEqual(
            [[1, 2, 3]], self.rtm.matrixReshape([[1, 2], [3, 4]], 1, 3))


class TestPascalsTriangle(unittest.TestCase):

    def setUp(self):
        self.pt = PascalsTriangle()

    def test_pascals_triangle(self):
        self.assertEqual(
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
            self.pt.generate(5))
        self.assertEqual([[1]], self.pt.generate(1))
        self.assertEqual([], self.pt.generate(0))


class TestPython(unittest.TestCase):

    def test_list(self):
        self.assertEqual(range(1, 10), range(0, 10)[1:])
        self.assertEqual([0, 0, 0, 0, 0], [0] * 5)

    def test_list_index(self):
        self.assertEqual(4, ([0, 0, 1, 1, 2, 2].index(2)))
        self.assertEqual(3, ([0, 0, 1, 1, 2, 2].index(1, 3)))

    def test_list_in(self):
        self.assertTrue(2 in [0, 0, 1, 1, 2, 2])

    def test_list_pop(self):
        _l = range(0, 10)
        self.assertEqual(9, _l.pop())
        self.assertEqual(range(0, 9), _l)

        _l = range(0, 10)
        self.assertEqual(0, _l.pop(0))
        self.assertEqual(range(1, 10), _l)

    def test_map(self):
        strs, i = ["flower", "flow", "flight"], 0

        self.assertEqual(["f", "f", "f"], map(lambda x: x[i], strs))
        self.assertEqual(strs, strs)

        try:
            map(lambda x: x[4], strs)
        except Exception as e:
            self.assertTrue("out of" in str(e))

    def test_str(self):
        self.assertEqual("321-", "-123"[::-1])
        self.assertEqual("321", "-123"[1:][::-1])

    def test_int(self):
        self.assertEqual(2147483648, 2**31)
        self.assertEqual(0, 1122 % 11)

        num, reverse_num = 1122, 0
        while num > 0:
            reverse_num = reverse_num * 10 + num % 10
            num = num / 10

        self.assertEqual(2211, reverse_num)

    def test_range(self):
        self.assertTrue(22 in range(11, 100, 11))
        self.assertEqual(9, len(range(11, 100, 11)))

    def test_set(self):
        self.assertEqual([1, 2], list(set([1, 1, 2])))
        self.assertEqual(sorted([2, 1]), list(set([2, 1, 1])))


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

    def test_two_sum_performance_correct(self):
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

    def test_two_sum_performance(self):
        if not IGNORE_OTHER_PERFORMANCE_TESTS:
            nums = filter(lambda num: num % 2 == 0, range(0, 25197))
            nums[8012], target = -1, 16021
            self.assertEqual(
                [8011, 8012], self.ts.twoSumPerformance(nums, target))


class TestLongestCommonPrefix(unittest.TestCase):

    def setUp(self):
        self.lcp = LongestCommonPrefix()

    def test_longest_common_prefix(self):
        self.assertEqual(
            "fl", self.lcp.longestCommonPrefix(["flower", "flow", "flight"]))
        self.assertEqual(
            "", self.lcp.longestCommonPrefix(["dog", "racecar", "car"]))


class TestReverse(unittest.TestCase):

    def setUp(self):
        self.r = Reverse()

    def test_reverse(self):
        self.assertEqual(321, self.r.reverse(123))
        self.assertEqual(-321, self.r.reverse(-123))
        self.assertEqual(21, self.r.reverse(120))


class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        self.ip = IsPalindrome()

    def test_number_of_digits(self):
        self.assertEqual(1, self.ip.number_of_digits(1122, 4))

    def test_is_palindrome(self):
        self.assertTrue(self.ip.isPalindrome(121))
        self.assertTrue(not self.ip.isPalindrome(-121))
        self.assertTrue(not self.ip.isPalindrome(10))
        self.assertTrue(self.ip.isPalindrome(313))

    def test_is_palindrome_for_int(self):
        self.assertTrue(self.ip.isPalindromeForInt(121))
        self.assertTrue(not self.ip.isPalindromeForInt(-121))
        self.assertTrue(not self.ip.isPalindromeForInt(10))
        self.assertTrue(self.ip.isPalindromeForInt(313))
        self.assertTrue(not self.ip.isPalindromeForInt(1122))
        self.assertTrue(self.ip.isPalindromeForInt(11))

    def test_fill_digits(self):
        self.assertEqual(11, self.ip.fill_digits(1, 1))
        self.assertEqual(111, self.ip.fill_digits(11, 2))
        self.assertEqual(
            1111, self.ip.fill_digits(self.ip.fill_digits(11, 2), 3))
        self.assertEqual(11122, self.ip.fill_digits(1122, 4))


class TestIsValid(unittest.TestCase):

    def setUp(self):
        self.iv = IsValid()

    def test_is_valid(self):
        self.assertTrue(self.iv.isValid("()"))
        self.assertTrue(self.iv.isValid("()[]{}"))
        self.assertTrue(not self.iv.isValid("(]"))
        self.assertTrue(not self.iv.isValid("([)]"))
        self.assertTrue(self.iv.isValid("{[]}"))
        self.assertTrue(not self.iv.isValid("]"))
        self.assertTrue(self.iv.isValid(""))
        self.assertTrue(not self.iv.isValid("[])"))


class TestMergeTwoLists(unittest.TestCase):

    def setUp(self):
        self.mtl = MergeTwoLists()

    def test_merge_two_lists(self):
        self.assertEqual(
            [1, 1, 2, 3, 4, 4],
            Utils.listnode_to_list(self.mtl.mergeTwoLists(
                Utils.list_to_listnode([1, 2, 4]),
                Utils.list_to_listnode([1, 3, 4]))))
        self.assertEqual(
            [1],
            Utils.listnode_to_list(self.mtl.mergeTwoLists(
                Utils.list_to_listnode([1]),
                Utils.list_to_listnode([]))))
        self.assertEqual(
            [1, 2],
            Utils.listnode_to_list(self.mtl.mergeTwoLists(
                Utils.list_to_listnode([2]),
                Utils.list_to_listnode([1]))))

    def test_merge_two_lists_for_list(self):
        self.assertEqual(
            [1, 1, 2, 3, 4, 4],
            self.mtl.mergeTwoListsForList([1, 2, 4], [1, 3, 4]))
        self.assertEqual(
            [1],
            self.mtl.mergeTwoListsForList([1], []))
        self.assertEqual(
            [1, 2],
            self.mtl.mergeTwoListsForList([2], [1]))


class TestThreeSum(unittest.TestCase):

    def setUp(self):
        self.ts = ThreeSum()

    def test_three_sum(self):
        self.assertEqual(
            sorted([[-1, -1, 2], [-1, 0, 1]]),
            sorted(self.ts.threeSum([-1, 0, 1, 2, -1, -4])))
        self.assertEqual([[0, 0, 0]], self.ts.threeSum([0, 0, 0]))
        self.assertEqual([[0, 0, 0]], self.ts.threeSum([0, 0, 0, 0]))
        self.assertEqual(
            sorted([[-2, 1, 1], [-2, 0, 2]]),
            sorted(self.ts.threeSum([-2, 0, 1, 1, 2])))

    def test_three_sum_performance(self):
        self.assertEqual([[0, 0, 0]], self.ts.threeSum([0] * 3000))


class TestTransposeMatrix(unittest.TestCase):

    def setUp(self):
        self.tm = TransposeMatrix()

    def test_transpose(self):
        self.assertEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]],
                         self.tm.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertEqual([[1, 4], [2, 5], [3, 6]],
                         self.tm.transpose([[1, 2, 3], [4, 5, 6]]))


class TestArrayPartitionI(unittest.TestCase):

    def setUp(self):
        self.api = ArrayPartitionI()

    def test_array_partition_i(self):
        self.assertEqual(4, self.api.arrayPairSum([1, 4, 3, 2]))


class TestUtils(unittest.TestCase):

    def test_list_to_listnode(self):
        _l, i = range(0, 5), 0
        listnode = Utils.list_to_listnode(_l)
        while listnode:
            self.assertEqual(_l[i], listnode.val)
            listnode = listnode.next
            i += 1

    def test_listnode_to_list(self):
        _l = range(0, 5)
        listnode = Utils.list_to_listnode(_l)

        self.assertEqual(_l, Utils.listnode_to_list(listnode))

    def test_reverse_num(self):
        for num in range(0, 9999):
            self.assertEqual(int(str(num)[::-1]), Utils.reverse_num(num))

    def test_list_to_treenode(self):
        # TODO
        _l = [3, 9, 20, None, None, 15, 7]
        Utils.list_to_treenode(_l)


if __name__ == "__main__":
    unittest.main()
