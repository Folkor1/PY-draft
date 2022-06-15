import unittest
import matrix


class TestMatrix(unittest.TestCase):
    """
    Validates the calculations in 2x2, 3x3 and 4x4 matrixes.
    """

    def test_matrix_2x2_input(self):
        numbers = matrix.Matrix_2x2(1, 2, 3, 4)
        calculation = numbers.determinant_2x2()
        determ_2x2 = '-2'
        msg_2x2 = "Matrix 2x2 determinant caclulation is not correct!"
        self.assertEqual(calculation, determ_2x2, msg_2x2)

    def test_matrix_3x3_input(self):
        numbers = matrix.Matrix_3x3(2, 6, 7, 2, 0, 8, 1, 2, 5)
        calculation = numbers.determinant_3x3()
        determ_3x3 = -16
        msg_3x3 = "Matrix 3x3 determinant caclulation is not correct!"
        self.assertEqual(calculation, determ_3x3, msg_3x3)

    def test_matrix_4x4_input(self):
        array = (7, 5, 0, 1, 2, 8, 5, 3, 8, 0, 2, 3, 6, 5, 8, 2)
        numbers = matrix.Matrix_4x4(*array)
        calculation = numbers.determinant_4x4()
        determ_4x4 = -1199
        msg_4x4 = "Matrix 4x4 determinant caclulation is not correct!"
        self.assertEqual(calculation, determ_4x4, msg_4x4)

if __name__ == '__main__':
    unittest.main()
