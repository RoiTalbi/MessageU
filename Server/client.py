
# ----------------------------------------------------------------
# Imports
# ----------------------------------------------------------------
import logging
import sys

from errors import *

# ----------------------------------------------------------------
# Globals
# ----------------------------------------------------------------

CLIENT_NAME_MAX_SIZE = 255


# ----------------------------------------------------------------
# Classes
# ----------------------------------------------------------------

def Client():

	def __init__(self, id, name, public_key, last_seen = 0):
		self._id = id
		self._name = name
		self._public_key = public_key
		self._last_seen = last_seen

	def get_id(self):
		return id

	def get_name(self):
		return self._name

	def get_public_key(self):
		return self._public_key



