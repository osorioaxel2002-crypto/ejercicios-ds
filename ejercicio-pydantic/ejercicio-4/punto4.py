from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing_extensions import Annotated

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: Annotated[int, Field(ge=1, le=5)]

try:
    usuario_incorrecto = UsuarioSistema(email="hernestoFuntegmail.com", nivel_acceso=8)
except ValidationError as e:
    print("Errores detectados:")
    print(e)

usuario_correcto = UsuarioSistema(email="pepesantos@gmail.com", nivel_acceso=5)
print("\nUsuario cargado correctamente :", usuario_correcto)