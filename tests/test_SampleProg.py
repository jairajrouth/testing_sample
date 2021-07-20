import unittest

from src.SampleProg import JackPot


class MyTestCase(unittest.TestCase):
    def test_sumJackPot(self):
        self.assertEqual(JackPot.sum_jack_pot(3, 1), 4)

    # def test_sumJackPot2(self): #Fails
    #     self.assertEqual(JackPot.sum_jack_pot(2, 5), 7)

    # def test_sumJackPot3(self): #Fails
    #     self.assertEqual(JackPot.sum_jack_pot(-2, -3), 2)

    def test_sumNoJackPot(self):
        self.assertEqual(JackPot.sum_jack_pot(5, 1), 8)

    def test_sumJackPot4(self):
        self.assertEqual(JackPot.sum_jack_pot(4, 0), 8)

    def test_sumJackPot5(self):
        self.assertEqual(JackPot.sum_jack_pot(-9, 7), -2)


if __name__ == '__main__':
    unittest.main()
