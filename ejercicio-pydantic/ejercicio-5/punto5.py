from pydantic import BaseModel, Field, ValidationError, HttpUrl
from typing_extensions import Annotated
from typing import Optional, List, Union

class PerfilUsuario(BaseModel):
    username: Annotated[str, Field(pattern=r"^[a-z0-9_]{3,20}$")]
    biografia: Annotated[Optional[str], Field(max_length=200)] = None
    redes_sociales: Optional[List[Union[HttpUrl, str]]] = None

perfil_ok = PerfilUsuario(
    username="Usuario de Git",
    biografia="Estudiante de desarrollo",
    redes_sociales=["https://github.com", "usuario_dev"]
)
print("Perfil ok:\n", perfil_ok)

try:
    perfil_malo = PerfilUsuario(
        username="Usuario Falso", 
        biografia="X" * 250       
    )
except ValidationError as e:
    print("\nErrores atajados:")
    print(e)