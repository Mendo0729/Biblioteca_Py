import Funciones.Funciones as fn



def agregar_libro(libros,BOOK_FILE):
    try:
        while True:
            nombre = input("Ingrese el nombre del libro: ").strip()
            if not nombre:
                print("El nombre del libro no puede estar vacío.")
                continue

            try:
                ano_publicacion = int(input("Ingrese el año de publicación: ").strip())
                if ano_publicacion <= 0:
                    print("El año de publicación debe ser un número positivo.")
                    continue
            except ValueError:
                print("Debe ingresar un año válido.")
                continue

            descripcion = input("Ingrese una breve descripción del libro: ").strip()
            if not descripcion:
                print("La descripción no puede estar vacía.")
                continue

            try:
                stock = int(input("Ingrese la cantidad en stock: ").strip())
                if stock < 0:
                    print("El stock no puede ser negativo.")
                    continue
            except ValueError:
                print("Debe ingresar un número válido para el stock.")
                continue

            # Obtener el último ID o asignar el primero si está vacío
            nuevo_id = max(libros.keys(), default=0) + 1

            # Agregar el libro al diccionario
            libros[nuevo_id] = {
                "nombre": nombre,
                "ano_publicacion": ano_publicacion,
                "descripcion": descripcion,
                "stock": stock
            }
            fn.guardar_datos(libros,BOOK_FILE)
            print(f"\n✅ Libro agregado exitosamente con ID: {nuevo_id}\n")
            break

    except KeyboardInterrupt:
        print("\nProceso interrumpido. Saliendo...")

def mostrar_libros(libros):
    if not libros:
        print("\n📚 No hay libros registrados.\n")
        return

    print("\n📖 Lista de libros registrados:\n")
    print(f"{'ID':<5}{'Nombre':<30}{'Año':<10}{'Stock':<10}{'Descripción':<50}")
    print("-" * 110)

    for libro_id, datos in libros.items():
        print(f"{libro_id:<5}{datos['nombre']:<30}{datos['ano_publicacion']:<10}{datos['stock']:<10}{datos['descripcion']:<50}")

    print()


def mostrar_usuarios(usuarios):
    fn.barra_carga()
    fn.borrar_barra()
    if not usuarios:
        print("No existen ususarios registrados")
    else:
        # Recorrer y mostrar usuarios por rol
        for rol, usuarios_por_rol in usuarios.items():
            print(f"\n--- {rol.capitalize()} ---")
            if not usuarios_por_rol:
                print(f"No hay {rol}s registrados.\n")
            else:
                # Imprimir encabezados
                print(f"{'ID':<5}{'Cédula':<15}{'Nombre':<25}{'Correo':<45}{'Sexo':<10}")
                print("-" * 120)  # Línea divisoria

                # Imprimir los datos de cada usuario en ese rol
                for id, datos in usuarios_por_rol.items():
                    print(f"{id:<5}{datos['cedula']:<15}{datos['nombre']:<25}{datos['correo']:<45}{datos['sexo']:<10}")
                print()

def agregar_usuario(usuarios, USUARIO_FILE):
    try:
        # Verificar si la clave 'usuario' existe en el diccionario
        if "usuario" not in usuarios:
            usuarios["usuario"] = {}
        if "admin" not in usuarios:
            usuarios["admin"] = {}

        while True:
            nombre = input("Ingresa el nombre: ").strip()
            if not nombre:
                print("El campo 'nombre' no puede estar vacío.")
                continue

            cedula = input("Ingresa la cédula: ").strip()
            if not cedula or not fn.validar_cedula(cedula):
                print("Cédula inválida. Inténtalo nuevamente.")
                continue

            correo = input("Ingresa el correo del usuario: ").strip()
            if not correo or not fn.validar_correo(correo):
                print(fn.validar_correo(correo))
                print("Correo inválido. Inténtalo nuevamente.")
                continue

            # Verificar si el correo ya existe
            usuario_encontrado = False
            for rol, usuario_rol in usuarios.items():
                for usuario_id, usuario_info in usuario_rol.items():
                    if usuario_info['correo'] == correo:
                        usuario_encontrado = True
                        print("El correo ya está registrado.")
                        break  # Rompe el bucle interno
                if usuario_encontrado:
                    break  # Rompe el bucle externo si ya se encontró el correo

            if usuario_encontrado:
                continue  # Vuelve a pedir la información

            contraseña = input("Ingresa la contraseña para el usuario: ").strip()
            if not contraseña:
                print("El campo 'contraseña' no puede estar vacío.")
                continue

            sexo = input("Ingresa el sexo M(masculino) - F(femenino): ").capitalize()
            if not sexo:
                print("El campo 'sexo' no puede estar vacío")
                continue

            rol = input("Ingresa el rol del usuario ('usuario'/'admin'): ").strip().lower()
            if rol not in ['usuario', 'admin']:
                print("Rol inválido. Debe ser 'usuario' o 'admin'.")
                continue

            # Obtener el último ID y asignar el siguiente número
            ultimo_id = max(usuarios[rol].keys(), default=0)
            nuevo_id = int(ultimo_id) + 1

            usuarios[rol][nuevo_id] = {
                'nombre': nombre,
                'cedula': cedula,
                'correo': correo,
                'sexo': sexo,
                'contrasena': fn.encriptar_contraseña(contraseña)
            }

            fn.guardar_datos(usuarios, USUARIO_FILE)  # ✅ Guardar cambios en el JSON
            print("\n✅ Usuario creado exitosamente con ID:", nuevo_id)
            break
    except KeyboardInterrupt:
        print("\nProceso interrumpido. Saliendo del programa...")


