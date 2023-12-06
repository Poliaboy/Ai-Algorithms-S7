"""
OpenAI Gym environments designed for the AI lab course
"""

from gym_lab5.envs.registration import register
from envs_lab5.maze_env import *
from envs_lab5.lava_env import *
from envs_lab5.cliff_env import *
from envs_lab5.windy_env import *

register(
    id='SmallMaze-v0',
    entry_point='envs_lab5:SmallMazeEnv')
register(
    id='GrdMaze-v0',
    entry_point='envs_lab5:GrdMazeEnv')
register(
    id='BlockedMaze-v0',
    entry_point='envs_lab5:BlockedMazeEnv')

register(
    id='LavaFloor-v0',
    entry_point='envs_lab5:LavaFloorEnv')
register(
    id='VeryBadLavaFloor-v0',
    entry_point='envs_lab5:VeryBadLavaFloorEnv')
register(
    id='NiceLavaFloor-v0',
    entry_point='envs_lab5:NiceLavaFloorEnv')
register(
    id='BiggerLavaFloor-v0',
    entry_point='envs_lab5:BiggerLavaFloorEnv')
register(
    id='HugeLavaFloor-v0',
    entry_point='envs_lab5:HugeLavaFloorEnv')

register(
    id='Cliff-v0',
    entry_point='envs_lab5:CliffEnv')

register(
    id='WindyGridworld-v0',
    entry_point='envs_lab5:WindyGridworldEnv')
