# ModelReflexVacuum: A robot vacuum cleaner modeled as a model-based reflex agent.
# Your implementation should pass the tests in test_model_reflex_vacuum.py.
# CARSON HANSEN

class ModelReflexVacuum:

    def __init__(self, state, transition_model, sensor_model):
        self.state = state
        self.transition_model = transition_model
        self.sensor_model = sensor_model
        self.most_recent_action = None
        self.is_dirty = None
        self.location = None

    def suck(self):
        print("side effect: cause hardware to suck")
        self.is_dirty = False
        self.transition_model.apply_suction()

    def move_left(self):
        print("side effect: cause hardware to move left")
        self.transition_model.move_left()

    def move_right(self):
        print("side effect: cause hardware to move right")
        self.transition_model.move_right()

    def update_state(self):

        if self.sensor_model is None:
           return
        
        self.is_dirty = self.sensor_model.sense_dirt()
        
        if not self.is_dirty:
            self.location = self.sensor_model.sense_location_id()
        else:
            self.location = None
  
    def action(self):
        self.update_state()

        action = None

        if self.is_dirty:
            action = self.suck
        else:
            if self.location == 'A':
                action = self.move_right
            elif self.location == 'B':
                action = self.move_left

        self.most_recent_action = action
        if self.most_recent_action is not None:
            self.most_recent_action()
        return self.most_recent_action
