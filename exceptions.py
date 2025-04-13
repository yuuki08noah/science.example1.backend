class IsotopeNotFound(Exception):
    def __init__(self, isotope):
        self.isotope = isotope
        super().__init__("The isotope '{}' was not found.".format(isotope))

class HistoryNotFound(Exception):
    def __init__(self, history_id):
        self.history = history_id
        super().__init__("The history id '{}' was not found.".format(history_id))