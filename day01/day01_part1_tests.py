import day01_part1
import unittest


class TestDay01Part1(unittest.TestCase):
    def test_measurement_increase_byone(self):
        depth_measurements = [199, 200]
        result1, result2, result3 = day01_part1.count_increases(depth_measurements)
        self.assertEqual(result1, 1)

    def test_measurement_increase_bythree(self):
        depth_measurements = [199, 200, 180, 188, 210]
        result1, result2, result3 = day01_part1.count_increases(depth_measurements)
        self.assertEqual(result1, 3)

    def test_measurement_increase_bythree_with_duplicates(self):
        depth_measurements = [199, 200, 180, 180, 188, 188, 210]
        result1, result2, result3 = day01_part1.count_increases(depth_measurements)
        self.assertEqual(result1, 3)

    def test_measurement_decrease_bythree_with_duplicates(self):
        depth_measurements = [199, 200, 180, 180, 179, 179, 178]
        result1, result2, result3 = day01_part1.count_increases(depth_measurements)
        self.assertEqual(result2, 3)
        self.assertEqual(result3, 7)


if __name__ == '__main__':
    unittest.main()
