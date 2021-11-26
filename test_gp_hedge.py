import unittest
import gp_hedge

class TestGpHedge(unittest.TestCase):
  def test_three_iterations(self):
    g = gp_hedge.GpHedge(["PI", "EI", "UCB"], eta=1)
    # iteration 1
    g.run()
    p = g.get_probabilities()
    self.assertAlmostEqual(p[0], 0.333, places=3)
    self.assertAlmostEqual(p[1], 0.333, places=3)
    self.assertAlmostEqual(p[2], 0.333, places=3)
    self.assertEqual(g.get_chosen_x(), -1)
    gains = g.get_gains()
    self.assertEqual(gains[0], 1)
    self.assertEqual(gains[1], 10)
    self.assertEqual(gains[2], 0.1)
    self.assertEqual(g.get_number_of_samples(), 1)
    # iteration 2
    g.run()
    p = g.get_probabilities()
    self.assertAlmostEqual(p[0], 0.000123, places=6)
    self.assertAlmostEqual(p[1], 0.9998, places=4)
    self.assertAlmostEqual(p[2], 0.000050, places=6)
    self.assertEqual(g.get_chosen_x(), 3)
    gains = g.get_gains()
    self.assertEqual(gains[0], 2)
    self.assertEqual(gains[1], 4)
    self.assertEqual(gains[2], 3.1)
    self.assertEqual(g.get_number_of_samples(), 2)
    # iteration 3
    g.run()
    p = g.get_probabilities()
    self.assertAlmostEqual(p[0], 0.08777, places=5)
    self.assertAlmostEqual(p[1], 0.6485, places=4)
    self.assertAlmostEqual(p[2], 0.264, places=3)
    self.assertEqual(g.get_chosen_x(), 3)
    gains = g.get_gains()
    self.assertEqual(gains[0], 3)
    self.assertEqual(gains[1], -2)
    self.assertEqual(gains[2], 6.1)
    self.assertEqual(g.get_number_of_samples(), 2)

if __name__ == "__main__":
  unittest.main()
