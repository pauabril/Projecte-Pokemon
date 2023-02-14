from enum import Enum

class GlobalGameState(Enum):
	NONE = 0,
	RUNNING = 1,
	ENDED = 2,

class RunningGameState(Enum):
	MAP = 0,
	BATTLE = 1
