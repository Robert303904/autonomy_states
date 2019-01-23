import abc

class AutonomyState:

    def __init__(self, autonomy):
        self.autonomy = autonomy
        self.current_state = None

    def next_state(self):
        return self.current_state.next_state(self)

    def set_state(self, new_state)
        self.current_state = new_state

class state(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def next_state(self):
        pass


"""
    There needs to be at least three different main states: Driving, Digging and Dumping
    that will all be linked into the various motor control and camera operations we will do.
    Along with those there will need to be states between the main states: Raising and Lowering
    the arms for the digging wheel etc. Most of these states will also need failsafe controls 
    that can interupt any state if the actions would be causing harm (eg. the digging wheel 
    getting lowered into the ground hits something harder than expected, we dont want the actuators
    burn up or lift the robot off the ground we need to detect if there is a problem and stop the 
    actuators.) There is a good flow chart on the google drive that has the expected states
    though they may change over time.
"""
