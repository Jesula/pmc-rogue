#!/usr/bin/env python
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler

def main() -> None:
    screen_height = 80
    screen_width= 50
    player_icon = "@"

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), player_icon, (255, 255, 255))
    npc = Entity(int(screen_width /2 -5), int(screen_height / 2), player_icon, (255, 255, 0))
    entities = {npc, player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="The Esoteric Adventures of a PMC Tech",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
       #Game Loop
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()