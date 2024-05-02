import unittest
from sorting import insertion_sort, selection_sort


class TestSort(unittest.TestCase):

    # data testing  for insertion sort and selection sort
    data_negative = {"input": [-1, 0, 35, 15, -4, 70, -90, -100, 400],
                     "output": [-100, -90, -4, -1, 0, 15, 35, 70, 400]}

    data_positive = {"input": [15, 13, 12, 10, 8],
                     "output": [8, 10, 12, 13, 15]}

    data_descending = {"input": [9, 8, 7, 6, 5, 4, 3, 2, 1],
                       "output": [1, 2, 3, 4, 5, 6, 7, 8, 9]}

    def test_sort(self):
        input_data = [14, 12, 10, 8, 6]
        result = insertion_sort(self.data_positive["input"])
        self.assertEqual(result, self.data_positive["output"])
        self.assertNotEqual(insertion_sort([]), [12])

    def test_sort_insertion_negative(self):
        self.assertEqual(insertion_sort(
            self.data_negative["input"]), self.data_negative["output"])
        self.assertEqual(selection_sort(
            self.data_negative["input"]), self.data_negative["output"])

    def test_sort_insertion_positive(self):
        self.assertEqual(insertion_sort(
            self.data_positive["input"]), self.data_positive["output"])
        self.assertEqual(selection_sort(
            self.data_positive["input"]), self.data_positive["output"])

    def test_sort_insertion_descending(self):
        self.assertEqual(insertion_sort(
            self.data_descending["input"]), self.data_descending["output"])
        self.assertEqual(selection_sort(
            self.data_descending["input"]), self.data_descending["output"])


if __name__ == "__main__":
    unittest.main()
