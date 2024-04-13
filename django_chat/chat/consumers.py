from channels.generic.websocket import WebsocketConsumer


class JoinAndLeave(WebsocketConsumer):
    def connect(self):
        print("server says connected")

    def receive(self, text_data=None, bytes_data=None):
        print("server says client message received: ", text_data)
        self.send("Server sends Welcome")

    def disconnect(self, code):
        print("server says disconnected")
