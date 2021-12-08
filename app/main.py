from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
# from typing import Optional

# from sqlalchemy.sql.operators import from_
from router.user_type import user_type
from router.document_type import document_type
from router.user import user
from router.turn_type import turn_type
from router.turn_state import turn_state
from router.turn import turn
from router.observation import observation
from router.reporte import reporte
app = FastAPI()
class Settings(BaseModel):
    authjwt_secret_key: str = "0cdb0aec294d9265ab84b64251f2038b5d30ce594f77a897d9ba802329cc1132"

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
app.include_router(user)
app.include_router(document_type)
app.include_router(user_type)
app.include_router(turn_type)
app.include_router(turn_state)
app.include_router(turn)
app.include_router(observation)
app.include_router(reporte)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}