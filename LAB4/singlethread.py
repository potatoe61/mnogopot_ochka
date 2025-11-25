from dataclasses import dataclass
from typing import List
import time

@dataclass
class Pixel:
    Red: int
    Green: int
    Blue: int

def make_white() -> Pixel:
    return Pixel(255, 255, 255)

def make_black() -> Pixel:
    return Pixel(0, 0, 0)

def to_rgb_tuple(p: Pixel):
    return (p.Red, p.Green, p.Blue)

def chessboard_transform_linear(pixels: List[Pixel], width: int, height: int) -> List[Pixel]:
    out = [Pixel(p.Red, p.Green, p.Blue) for p in pixels]
    for idx in range(len(out)):
        x = idx % width
        y = idx // width
        if (x + y) % 2 == 0:
            out[idx] = make_white()
        else:
            out[idx] = make_black()
    return out

def run_no_threads(pixels: List[Pixel], width: int, height: int) -> (List[Pixel], float):
    t0 = time.time()
    result = chessboard_transform_linear(pixels, width, height)
    t1 = time.time()
    return result, t1 - t0

def example_no_threads():
    width, height = 2000, 2000
    pixels = [make_white() for i in range(width * height)]
    result, dt = run_no_threads(pixels, width, height)
    print("Без потоков, время: {:.6f}s".format(dt))
    #print([to_rgb_tuple(p) for p in result])

if __name__ == "__main__":
    example_no_threads()