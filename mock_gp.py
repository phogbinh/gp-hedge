class MockGp:
  first_iteration_end = False

  def get_max_point(self, af): # allocation function
    if af == "PI":
      return -1
    elif af == "EI":
      return 3
    else: # UCB
      return 5

  def sample_and_add(self, x):
    pass

  def update(self):
    pass

  def get_means(self, points):
    if not self.first_iteration_end:
      self.first_iteration_end = True
      return [1, 10, 0.1]
    else:
      return [1, -6, 3]
