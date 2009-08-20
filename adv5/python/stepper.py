import pickle, sys
from data import *
from adv import *

# The initial state
INITIAL_SAVED_STATE = None

def InitialSavedState():
  global INITIAL_SAVED_STATE
  if not INITIAL_SAVED_STATE:
    initial_state = State(INITIAL)
    try:
      CALL(initial_state, INITIAL)
    except Quit, e:
      pass
    initial_state.continuation = e.continuation
    INITIAL_SAVED_STATE = \
        pickle.dumps(SavedState(initial_state, clear_output=False))
  return INITIAL_SAVED_STATE

STATUS_NEW = 0
STATUS_PLAY = 1
STATUS_DONE = 2

class Stepper:
  def __init__(self, saved_state):
    if not saved_state:
      self.state = pickle.loads(InitialSavedState()).state()
      self.status = STATUS_NEW
    else:
      self.state = pickle.loads(saved_state).state()
      if self.state.exited:
        self.status = STATUS_DONE
      else:
        self.status = STATUS_PLAY

  def step(self, input=None):
    if not input:
      return

    s = self.state
    if s.exited:
      return

    HAS_INPUT(s, input)

    while True:
      try:
        CALL(s, s.continuation)
      except Quit, e:
        if e.continuation:
          s.continuation = e.continuation
          break
        else:
          s.continuation = REPEAT
      except Stop, e:
        self.status = STATUS_DONE
        return
      else:
        break
    self.status = STATUS_PLAY

  def isnew(self):
    return self.status == STATUS_NEW
    
  def exited(self):
    return self.status == STATUS_DONE

  def get_output(self):
    return self.state.output

  def get_saved_state(self):
    return pickle.dumps(SavedState(self.state))

  def get_location(self):
    try:
      location = var_value(self.state, HERE).short
      linefeed_index = location.find("\n")
      if linefeed_index != -1:
        location = location[0:linefeed_index]
      return location
    except:
      return "Somewhere around Colossal Cave."

def main():
  stepper = Stepper(None)
  print stepper.get_output()
  saved_state = stepper.get_saved_state()

  while True:
    print "> ",
    input = sys.stdin.readline()[:-1]

    stepper = Stepper(saved_state)
    stepper.step(input)
    output = stepper.get_output()
    if output:
      print output
    if stepper.exited():
      return
    saved_state = stepper.get_saved_state()

if __name__ == '__main__':
  main()
