import distutils.version
import os
import sys
import warnings

from gym_lab5 import error
from gym_lab5.version import VERSION as __version__

from gym_lab5.core import Env, GoalEnv, Wrapper, ObservationWrapper, ActionWrapper, RewardWrapper
from gym_lab5.spaces import Space
from gym_lab5.envs import make, spec, register
from gym_lab5 import logger

__all__ = ["Env", "Space", "Wrapper", "make", "spec", "register"]
