from unittest import TestCase

import Task2


class TestTask2(TestCase):

    def test_Task2(self):

        self.assertEqual(
            Task2.sets([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
            [1, 2, 3, 5, 8, 13])
