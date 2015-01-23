__author__ = 'KMK'

import unittest
import hangman



class hangmanTestCase(unittest.TestCase):

    def test_correct(self):
        answer=hangman.checkCorrectAnswer('tac','cat')

        self.assertTrue(answer)

    def test_incorrect(self):
        answer=hangman.checkCorrectAnswer('ac','cat')

        self.assertEquals(answer,True)


if __name__ == '__main__':
    unittest.main()
