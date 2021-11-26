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

  def get_mean(self, af, x): # allocation function, x
    if not self.first_iteration_end:
      if af == "PI":
        return 1
      elif af == "EI":
        return 10
      else: # UCB
        self.first_iteration_end = True
        return 0.1
    else:
      if af == "PI":
        return 1
      elif af == "EI":
        return -6
      else: # UCB
        return 3
