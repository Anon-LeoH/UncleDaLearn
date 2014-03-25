import math
import random

class mathObject(object):
    def __init__(self):
        self.type = "MathObject"

class NegInfinite(mathObject):
    def __init__(self):
        pass

    def __eq__(self, other):
        if isinstance(other, NegInfinite):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True
    
    def __lt__(self, other):
        if self == other:
            return False
        else:
            return True
    
    def __gt__(self, other):
        return False

    def __le__(self, other):
        return True

    def __ge__(self, other):
        if self == other:
            return True
        else:
            return False

class PosInfinite(mathObject):
    def __init__(self):
        pass

    def __eq__(self, other):
        if isinstance(other, PosInfinite):
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True
    
    def __gt__(self, other):
        if self == other:
            return False
        else:
            return True
    
    def __lt__(self, other):
        return False

    def __ge__(self, other):
        return True

    def __le__(self, other):
        if self == other:
            return True
        else:
            return False

