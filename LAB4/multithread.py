import threading
import time
from typing import List
from dataclasses import dataclass

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
def chessboard_transform_row(input_pixels: List[Pixel], output_pixels: List[Pixel], width: int, height: int, row: int):
    y = row
    for x in range(width):
        idx = y * width + x
        if (x + y) % 2 == 0:
            output_pixels[idx] = make_white()
        else:
            output_pixels[idx] = make_black()
def run_with_threads(pixels: List[Pixel], width: int, height: int) -> (List[Pixel], float):
    output = [Pixel(0,0,0) for _ in range(width * height)]
    threads = []
    t0 = time.time()
    for row in range(height):
        t = threading.Thread(target=chessboard_transform_row, args=(pixels, output, width, height, row))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    t1 = time.time()
    return output, t1 - t0

def example_with_threads():
    width, height = 2000, 2000
    pixels = [make_white() for _ in range(width * height)]
    result, dt = run_with_threads(pixels, width, height)
    print("С потоками, время: {:.6f}s".format(dt))
    #print([to_rgb_tuple(p) for p in result])
if __name__ == "__main__":
    example_with_threads()