import numpy as np

class LogicGate:
    def __init__(self):
        self.w1 = None
        self.w2 = None
        self.th = None
        self.out = None
        self.x1 = None
        self.x2 = None


    # AND Gate:

    def and_gate(self, x1, x2):
        self.w1 = 0.5
        self.w2 = 0.5
        self.th = 0.99

        self.x1 = x1
        self.x2 = x2

        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])

        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0


    # OR Gate:

    def or_gate(self, x1, x2):
        self.w1 = 0.5
        self.w2 = 0.5
        self.th = 0.0
        
        self.x1 = x1
        self.x2 = x2
        
        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])
        
        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0


    # NAND Gate:

    def nand_gate(self, x1, x2):
        self.w1 = -0.5
        self.w2 = -0.5
        self.th = -0.75

        self.x1 = x1
        self.x2 = x2

        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])

        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0


    # NOR Gate:

    def nor_gate(self, x1, x2):
        self.w1 = -0.5
        self.w2 = -0.5
        self.th = -0.25

        self.x1 = x1
        self.x2 = x2

        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])

        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0


    # XOR Gate:

    def xor_gate(self, x1, x2):
        c = self.or_gate(x1, x2)
        d = self.nand_gate(x1, x2)
        e = self.and_gate(c, d)

        self.x1 = x1
        self.x2 = x2

        if e == 1:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0
        


            