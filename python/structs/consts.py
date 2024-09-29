
# database init
DATABASE_BAD_ENV_ERR = "You must include a 'DATABASE_URL' in .env with 'sqlite+aiosqlite:///' as the start."
DATABASE_ENV_ASSERT = lambda url : (url is not None) and (url.startswith("sqlite+aiosqlite:///") is True)
