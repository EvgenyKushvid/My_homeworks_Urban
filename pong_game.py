import arcade
SCREEN_WIDHT = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong game'


class Bar (arcade.Sprite):
    def __init__(self):
        super().__init__(filename=' bar.png', 1.0)
class Game (arcade.Window):
    def __init__(self,widht,height,title):
            super().__init__(widht,height,title)
            self.bar = Bar()



    def on_draw(self):
        self.clear((255,255,255)) # делаем окно белым
        self.bar.draw()



if __name__ == '__main__':
    window  = Game(SCREEN_WIDHT, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()

