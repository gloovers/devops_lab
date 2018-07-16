from unittest import TestCase

import task2


class TestTask(TestCase):
    def setUp(self):
        """Init"""

    def test_is_prime(self):
        """Test for task2 def search_max_count()"""
        self.assertEqual(task2.search_max_count([15, 12, 56, 24, 12, 5]), 12)

    def tearDown(self):
        """Finish"""
