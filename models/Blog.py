class Blog:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def api_format(self):
        return {'id': self.id, 'name': self.name}
