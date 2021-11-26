import math
import mock_gp

class GpHedge:
  gp = mock_gp.MockGp()
  eta = 0
  gains = []
  af = [] # allocation functions
  p = [] # probabilities
  chosen_x_list = []

  def __init__(self, allocation_functions, eta):
    self.af = allocation_functions
    self.eta = eta
    self.gains = [0] * len(allocation_functions)

  def run(self):
    max_points = [self.gp.get_max_point(allocation_function) for allocation_function in self.af]
    self.compute_probabilities()
    chosen_x = self.choose_x(max_points)
    if chosen_x not in self.chosen_x_list:
      self.chosen_x_list.append(chosen_x)
      self.gp.sample_and_add(chosen_x)
      self.gp.update()
    means = self.gp.get_means(max_points)
    self.gains = [self.gains[idx] + means[idx] for idx in range(0, len(self.af))]

  def compute_probabilities(self):
    total = sum([math.exp(self.eta * gain) for gain in self.gains])
    self.p = [math.exp(self.eta * gain) / total for gain in self.gains]

  def choose_x(self, max_points):
    chosen_x = None
    max_probability = -1
    for idx in range(0, len(self.p)):
      if max_probability < self.p[idx]:
        max_probability = self.p[idx]
        chosen_x = max_points[idx]
    return chosen_x

  def get_probabilities(self):
    return self.p 

  def get_chosen_x(self):
    return self.chosen_x_list[-1]

  def get_gains(self):
    return self.gains

  def get_number_of_samples(self):
    return len(self.chosen_x_list)
