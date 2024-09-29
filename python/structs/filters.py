
import re

async def ascii_letters_numbers(value : str) -> str:
	"""Get the first group of ascii letters/numbers from the value."""
	pattern : str = r'[A-Za-z0-9]+'
	return re.match(pattern, value).group()

async def is_sha256_hash(value: str) -> bool:
	"""Check if the value is a sha256 value."""
	if len(value) != 64:
		return False
	return bool(re.fullmatch(r'[0-9a-fA-F]{64}', value))
