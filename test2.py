import asyncio
import re
import requests
from ktistory import *

access_token = '532a0328e01aa1509960111cb73f30be_3cdb6ea4c6e60805dd247f432afc7d1f'

asyncio.run(getTrendsToWrite(access_token))
