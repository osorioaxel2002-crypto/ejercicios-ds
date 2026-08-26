from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing_extensions import Annotated

class Estudiante(BaseModel):
    
    legajo: Annotated[int, Field(gt=0)]
    nombre_completo: Annotated[str, Field(min_length=5)]
    email: EmailStr
    promedio: Annotated[float, Field(ge=0.0, le=10.0)] = 0.0

print("Menu De Prubas")

try:
    print("\nProbando legajo invalido")
    e1 = Estudiante(legajo=-5, nombre_completo="Axel Osorio", email="axelosorio@gmail.com")
except ValidationError as e:
    print(f"Error: {e}")
try:
    print("\nProbando nombre corto")
    e2 = Estudiante(legajo=10, nombre_completo="Ax", email="axelosorio@gmail.com")
except ValidationError as e:
    print(f"Error: {e}")
try:
    print("\nProbando email falso")
    e3 = Estudiante(legajo=10, nombre_completo="Axel Osorio", email="correo_sin_arroba")
except ValidationError as e:
    print(f"Error atajado: {e}")
try:
    print("\nProbando promedio excedido")
    e4 = Estudiante(legajo=10, nombre_completo="Axel Osorio", email="axel@mail.com", promedio=11.5)
except ValidationError as e:
    print(f"Error atajado: {e}")

print("\nProbando estudiante ")
estudiante_ok = Estudiante(legajo=99, nombre_completo="Axel Osorio", email="axelosorio@gmail.com")
print(f"Exito {estudiante_ok}")