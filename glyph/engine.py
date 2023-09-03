import esper
import pyxel

from glyph.components import Position, Sprite


class Engine:
    player: int

    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("./glyph.pyxres")

        self.world = esper.World()
        self.world.player = self.world.create_entity(
            Position(20, 20), Sprite(0, 0, 0, 8, 8)
        )

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.world.process()

    def draw(self):
        pyxel.cls(0)

        for _, (position, sprite) in self.world.get_components(Position, Sprite):
            pyxel.blt(
                position.x,
                position.y,
                sprite.img,
                sprite.u,
                sprite.v,
                sprite.w,
                sprite.h,
            )
        pyxel.show()

    def run(self):
        pyxel.run(self.update, self.draw)
