from posixpath import splitext


class PowerUp(splitext):
    def __init__(self,image):
        self.image= image
        self.rect= self.image.get_rect()
        self
