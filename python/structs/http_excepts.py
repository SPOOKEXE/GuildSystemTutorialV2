
from http import HTTPStatus
from fastapi import HTTPException

NOT_AUTHORIZED_EXCEPTION = HTTPException(status_code=HTTPStatus.FORBIDDEN, detail='Not Authorized')
