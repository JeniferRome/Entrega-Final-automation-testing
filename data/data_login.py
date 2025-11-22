CASOS_LOGIN = [
     ("standard_user", "secret_sauce", True), # usuario valido, login exitoso
     ("locked_out_user", "secret_sauce", False), # usuario bloqueado, login falla
     ("usuarios_malo", "password_malo", False),  # credencial invalidas, login falla
]