class NetworkToken:
    def load_token(self, source_id, destination_id, message):
        self.history += source_id
        self.source_id = source_id
        self.free = False
        self.destination_id = destination_id
        self.message = message

    def __init__(self):
        self.source_id = ''
        self.destination_id = ''
        self.message = ''
        self.free = True
        self.reached_destination = False
        self.history = ''