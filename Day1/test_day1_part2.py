import day1_part2
import unittest


class MyTestCase(unittest.TestCase):
    def test_three_measurement_zero(self):
        depth_measurements = [1, 2, 3]
        result = day1_part2.count_three_measurement_window(depth_measurements)
        self.assertEqual(0, result)

    def test_three_measurement_one(self):
        depth_measurements = [1, 2, 3, 4]
        result = day1_part2.count_three_measurement_window(depth_measurements)
        self.assertEqual(1, result)

    def test_three_measurement_one_with_decrease(self):
        depth_measurements = [1, 2, 3, 4, 0]
        result = day1_part2.count_three_measurement_window(depth_measurements)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
