from typing import Tuple

import numpy as np #type: ignore

graphic_dt = np.dtype(
    [
        ("ch", np.int32), #Unicode codepoint
        ("fg", "3B",),    #3 unsigned bytes, for RGB colors
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),      # True if the tile can be walked over
        ("transparent", np.bool),   # True if the tile doesn't block FOV
        ("dark", graphic_dt),       # Graphics for when this tile is not in FOV
    ]
)

def new_tile(
        *,
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper Function for defining individual tile types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent= True, dark=(ord(" "), (255,255,255), (50,50,150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255,255,255), (0,0,100)),
)