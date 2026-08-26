from pydantic import BaseModel, ValidationError
from typing import Union, Literal

class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: Literal["sensor", "actuador", "gateway"]

print("===Menu===")

dis1 = Dispositivo(id_dispositivo=21, tipo="sensor")
print("Dispositivo entero:", dis1)

dis2 = Dispositivo(id_dispositivo="Sensor 1", tipo="gateway")
print("Dispositivo texto:", dis2)

try:
    d_error = Dispositivo(id_dispositivo=32, tipo="motor")
except ValidationError as e:
    print("\nError")
    print(e)