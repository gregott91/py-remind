class Observable:
    def __init__(self):
        super().__init__()
        self.subscriptions = []

    def subscribe(self, fun):
        self.subscriptions.append(fun)

    def onChange(self, state):
        [x(state) for x in self.subscriptions]

    