
from typing import Optional
from pydantic import BaseModel

# El ID de mongo es un string, para que pueda hacer IDs mas complejos. 
# Normalmente el ID no lo creamos nosotros, sino que lo hace la base de datos. Por ello le decimos a FastApi que el id que puede ser opcional, quizás no lo reciba como parámetro.
class User(BaseModel):
    id: Optional[str] = None
    username: str
    email : str
    
