class Node:
    def __init__(self):
        self.is_active = False
        self.EPP = []


    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False

    def change_epp(self, EPP) -> None:
        self.EPP = EPP