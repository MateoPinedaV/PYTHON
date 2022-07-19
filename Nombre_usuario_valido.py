def nombre_valido(nombreusuario):
    if len(nombreusuario) < 3:
        print("nombre de usuario invalido. debe ser mayor a 3 caracteres")
    elif len (nombreusuario) > 15:
        print("Nombre de usuario invalido no puede superar los 15 caracteres")
    else:
        print("Nombre de usuario valido")

nombre_valido("mateo")
nombre_valido("mateoandrespinedavargas")
