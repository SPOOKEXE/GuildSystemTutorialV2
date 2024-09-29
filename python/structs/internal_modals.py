
from typing import Optional
from pydantic import BaseModel, Field

import datetime

class BaseModelIgnore(BaseModel):

	class Config:
		extra = 'ignore'

class GuildData(BaseModelIgnore):
	guild_id : int
	owner_id : int
