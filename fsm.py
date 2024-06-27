from state import State
from event import Event

class FSM:
    def __init__(self):
        self.state = State.MENU

    def transition(self, event):
        if self.state == State.MENU:
            if event == Event.START_CHARACTER_SELECT:
                self.state = State.CHARACTER_SELECT
        elif self.state == State.CHARACTER_SELECT:
            if event == Event.START_GAME:
                self.state = State.GAME
        elif self.state == State.GAME:
            if event == Event.END_GAME:
                self.state = State.MENU

    def get_state(self):
        return self.state