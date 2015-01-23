__author__ = 'KMK'

import unittest
import hangman



class hangmanTestCase(unittest.TestCase):

    def test_correct(self):
        answer=hangman.checkCorrectAnswer('tac','cat')

        self.assertTrue(answer)

<<<<<<< HEAD

=======
>>>>>>> FETCH_HEAD
    def test_CheckWrongAnswerFalse(self):
        answer = hangman.checkWrongAnswer('tac', 'cat')
        self.assertFalse(answer)
        self.assertEquals(answer,False)
<<<<<<< HEAD

=======
    def test_incorrect(self):
        answer=hangman.checkCorrectAnswer('ac','cat')

        self.assertEquals(answer,True)
>>>>>>> FETCH_HEAD


if __name__ == '__main__':
    unittest.main()
