class Scene:

    def get_name(self):
        return "Get ready!"

    def init(self):
        pass

    def tick(self, frame, screen, events):
        raise NotImplementedError()