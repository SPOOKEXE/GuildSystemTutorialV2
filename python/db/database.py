
from typing import Optional
from sqlalchemy import JSON, DateTime, Boolean, Column, Integer, Null, PrimaryKeyConstraint, String, func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, registry

from structs.consts import DATABASE_ENV_ASSERT, DATABASE_BAD_ENV_ERR

import datetime
import dotenv

env : dict[str, Optional[str]] = dotenv.dotenv_values()

DATABASE_URL : str = env.get('DATABASE_URL')

assert DATABASE_ENV_ASSERT(DATABASE_URL), DATABASE_BAD_ENV_ERR

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

mapper_registry = registry()
Base = mapper_registry.generate_base()

class GuildsDB(Base):
	__tablename__ = "guilds"

	guild_id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
	owner_id = Column(Integer, index=True, nullable=False)

HAS_CREATED_TABLES : bool = False
async def create_tables() -> None:
	global HAS_CREATED_TABLES
	if HAS_CREATED_TABLES is True: return
	HAS_CREATED_TABLES = True
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
