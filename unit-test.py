import unittest
import unit_test_cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'oluwaseun'
        res = unit_test_cap.cap_text(text)
        self.assertEqual(res, 'Oluwaseun')

    def test_multiple_words(self):
        text = 'seun python'
        result = unit_test_cap.cap_text(text)
        self.assertEqual(result, 'Seun Python')

if __name__ == '__main__':
    unittest.main()