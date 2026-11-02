"""Defense research package (lane hrt-w1): map geometry, kill-zone planning, defensive bots.

Everything here uses only the observation, the bot's own state and the public engine
modules (td_game.pathfinding, td_game.combat, td_game.config) as a local planning
simulator on freshly constructed state copies. No live engine object is inspected.
"""
