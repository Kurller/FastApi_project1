from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import FastAPI,HTTPException,status,Depends,APIRouter
from app import Schemas
from router import oAuth
from app.config import settings
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
router = APIRouter()

#SECRET KEY
#ALGORITHM
#Expiration

SECRET_KEY = settings.secret_key
ALGORITHM = settings.Algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.Access_Token_expire_minutes
@router.post("/login")
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    #if expires_delta:
    expire = datetime.utcnow() + timedelta(minutes =ACCESS_TOKEN_EXPIRE_MINUTES)
    #else:
     #   expire = datetime.now(timezone.utc) + timedelta(minutes=15
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id = payload.get("user_id")
        if id is None:
            raise credential_exception
        
        # Ensure id is converted to string before passing to TokenData
        id_str = str(id)
        token_data = Schemas.TokenData(id=id_str)
    except JWTError:
        raise credential_exception
    
    return token_data

    
def get_current_user(token :str = Depends(oauth2_scheme)):
    credential_exception =  HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",headers = {"WWW.AUTHENTICATE":"bearer"})
    
    
    return verify_access_token(token,credential_exception)