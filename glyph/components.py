from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Sprite:
    img: Union[Literal[0], Literal[1], Literal[2]]
    u: int  # x coordinate in sprite sheet
    v: int  # y coordinate in sprite sheet
    w: int  # width of sprite
    h: int  # height of sprite
