# %load utils/Node.py
class Node ():
  def __init__(self, state, value, operators, operator=None, parent=None, objective=None):
    self.state = state
    self.value = value
    self.children = []
    self.parent = parent
    self.operator = operator
    self.objective = objective
    self.level = 0
    self.operators = operators

  def add_child(self, value, state, operator):
    node = type(self)(value=value, state=state, operator=operator, parent=self, operators=self.operators)
    add_node_child(node)
    return node

  def add_node_child(self, node):
    node.level = node.parent.level + 1
    self.children.append(node)
    return node

  #Devuelve todos los estados según los operadores aplicados
  def get_childrens(self):
    return [
        self.getState(i)
          if not self.repeat_state_path(self.get_state(i))
            else None for i, op in enumerate(self.operators)]

  def get_state(self, index):
    pass

  def repeat_state_path(self, state):
      n = self
      while n is not None and n.state != state:
          n = n.parent
      return n is not None

  def path_to_objective(self):
      n = self
      result = []
      while n is not None:
          result.append(n)
          n = n.parent
      return result

  def heuristic(self):
    return 0

  def cost(self):
    return 1

  def f(self):
    return self.cost() + self.heuristic()

  def __eq__(self, other):
    return self.state == other.state

  def __lt__(self, other):
    return self.f() < other.f()
