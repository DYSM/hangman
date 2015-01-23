__author__ = 'KMK'

import unittest
import hangman



class hangmanTestCase(unittest.TestCase):

    def test_CheckCorrectAnswerTrue(self):
        answer=hangman.checkCorrectAnswer('tac','cat')
        self.assertTrue(answer)

    def test_CheckCorrectAnswerFalse(self):
        answer = hangman.checkCorrectAnswer('ito', 'cat')
        self.assertFalse(answer)

    def test_CheckWrongAnswerTrue(self):
        answer = hangman.checkWrongAnswer('rioooi', 'ourt')
        self.assertTrue(answer)

    def test_CheckWrongAnswerFalse(self):
        answer = hangman.checkWrongAnswer('tac', 'cat')
        self.assertFalse(answer)


if __name__ == '__main__':
    unittest.main()
