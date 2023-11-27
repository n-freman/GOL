from abc import ABC


class AbstractAdapter(ABC):
    
    def __init__(self, session):
        self.session = session

