from pydantic import BaseModel, Field, ValidationError
from typing_extensions import Annotated
from typing import Optional

coordenadasGPS = Annotated[float, Field(ge= -90.0, le=90.0)]

class Ubicacion(BaseModel):
    latitud:coordenadasGPS
    longitud:coordenadasGPS
    etiqueta: Optional[str]=None

print("=====Menu De Prueba=====")
ubi1 = Ubicacion(latitud=-50.25, longitud=-65.30, etiqueta="Barrio de los simpsons")
print("Ubicacion correcta:", ubi1)


try:
    ubi_error = Ubicacion(latitud=200.5, longitud=-65.30)
except ValidationError as e:
    print("\nError de cordenada")
    print(e)