"""Dos equipos de futbol desean crear un nuevo equipo con los jugadores más aptas de
cada equipo para ello. Los jugadores y colaboradores de cada equipo se deben
registrar en dos listas simplemente ligadas circulares."""

"""La lista ligada E1 y Lista Ligada E2. La lista ligada resultante es una lista doblemente ligada de tal forma que:

-  Solo se aceptan en el nuevo equipo personas menores de 25 años

-  El nuevo equipo debe quedar equilibrado, es decir igual cantidad de
personas del equipo 1 y del equipo 2.

- Se deben cubrir todos los puestos de jugadores, administrativos y cuerpo
técnico.
"""

# OJO notemos que la cantidad de personas de un equipo en la definición del problema debe ser un número PAR de integrantes entre Jugadores / Staff tecnico / directivos. Para poder distribuir de manera igual los integrantes de dos equipos. Si fuera IMPAR inevitablemente la cantidad de integrantes no podria ser la misma.

# Solución.


"""
Dado que no hay más restricciones ni se pide ninguna caraceristica en especial, vamos a hacer un programa según los siguinetes supuestos. 

Supongamos dos equipos de futbol, para simplicidad y dado que no se especifica tomemos equipos de de futbol 6 => (5 titulares, 1 suplente revulsivo.) 6 jugadores
 
1. entrenador.
2. segundo entrenador.
4. medico
6. utilero. 

# Para el personal administrativo tendremos. 
1. presidente 
2. vicepresidente
3. director deportivo 
4. secretario técnico

Para mantener el esquma simple obviaremos lo demas. 

Pruebas necesarias. 
De ingreso:
Se usará una simulación basada en diccionarios de data que tendra los siguentes controles:

1. Tipo de datos validos del aplicativo.
2. Presencia de todos los integrantes. 
3. Límite en los integrantes del equipo y verificación de roles.
"""


class Node:
    """
    Representa un nodo en una lista simplemente ligada.

    Args:
        age (int): Edad de la persona u objeto representado por el nodo.
        role (str): Rol asignado en el equipo.
        team (int): Identificador del equipo al que pertenece.
        next (Node): Referencia al next nodo en la lista. Es None por defecto.

        next: Referencia al next nodo en la lista.
    """

    def __init__(self, id: str, name: str, age: int, role: str, team: int):
        self.id = id
        self.name = name
        self.age = age
        self.role = role
        self.team = team
        self.next = None

    @classmethod
    def create(cls, id, name, age, role, team):
        """
        Crea una instancia de la clase Node validando los tipos de los argumentos.
        Verifica los tipos de datos dado que el ejericio pedía la aplicación de pruebas.

        Args:
            id : Identificación del empleado dentro del club
            name : Nomnbre del empleado.
            age: Edad del empleado.
            role: Rol del empleado.
            team: Número de empleado.

        Nota: Debido a los diferentes roles del equipo se trata a cualquier persona sin distinción usado el calificativo de "empleado"

        Returns:
            Node: Nueva instancia de la clase con los valores proporcionados.

        Raises:
            TypeError: Si algún argumento no tiene el tipo esperado.

        Nota2: Debido a la naturaleza de los tipos de datos y lo requerido para identificar correctamente a un integrante en exte contexto será el nodo a insertar en nuestra LSLC , se utiliza el método de clase create para:

            1. Validar tipos de datos de los argumentos de que podrian crear una instancia de la clase nodo.

            2. No recargar el constructor con la validación, separar responsabilidades seguir SOLID: PRU

            3. Utilitario en el diseño de la solución y para identificar nodos existosos y fallidos ya que todo el ingreso es por consola
        """
        campos = {
            "id": (id, str),
            "name": (name, str),
            "age": (age, int),
            "role": (role, str),
            "team": (team, int),
        }

        # Validación genérica
        for nombre, (valor, tipo_esperado) in campos.items():
            if not isinstance(valor, tipo_esperado):
                raise TypeError(
                    f"Error en '{nombre}': se esperaba {tipo_esperado.__name__}, "
                    f"se recibió {type(valor).__name__} con valor {valor!r}"
                )

        return cls(id, name, age, role, team)


class NodeRole:
    """
    Nodo que representa un rol dentro de una lista enlazada (Auxiliar) de roles únicos.

    Attributes:
        rol (str): El nombre del rol (por ejemplo, 'entrenador', 'presidente').
        next (NodoRol): Referencia al next nodo en la lista.
    """

    def __init__(self, role):
        """
        Inicializa un nodo de rol con el valor proporcionado.

        Args:
            rol (str): Nombre del rol a almacenar.
        """
        self.role = role
        self.next = None


class ListaRolesUnicos:
    """
    Lista simplemente ligada que almacena roles únicos,
    usada para evitar duplicación de cargos en staff técnico o directiva.

    Attributes:
        head (NodoRol): Nodo inicial de la lista.
        size (int): Número total de roles almacenados.

    La clase junto con sus métodos se abstrae en esta lógica dado que se dee utilizar dos veces, para verificar roles del staff técnico y de la directiva.
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def append_role(self, role):
        """
        Agrega un nuevo rol a la lista de roles si no existe.

        Args:
            rol (str): Nombre del rol a agregar.

        Returns:
            bool: True si se agregó el rol exitosamente, False si ya existía.

        1. Usamos el método auxiliar self.existe para ver si el rol ya existe en la lista.

        2. Crea un nodo que contine como unico valor el rol.

        3. El nuevo nodo apunta a la cabecerá , y ahora la cabecera será el nuevo nodo
           (Es decir que insertamos al inicio de la LSL ya que no importar el orden de los roles evita recorrer la lista).

        4. Actualizamos el tamaño de la lista de roles.

        """
        if self.exist(role):
            return False  # ya existe el rol
        new_role = NodeRole(role)
        new_role.next = self.head
        self.head = new_role
        self.size += 1
        return True

    def exist(self, role: str):
        """
        Verifica si un rol ya está presente en la lista.

        Args:
            rol (str): Nombre del rol a buscar.

        Returns:
            bool: True si el rol existe, False si no.

        Funcionamiento:
        Creamos un nodo actual (current) para recorrer la lista de roles, actualizamos el nodo actual (current) y verifcamos si el rol que contiene ya está en la lista de roles.
        """
        current = self.head
        while current:
            if current.role == role:
                return True
            current = current.next
        return False

    def reset(self):
        """Reinicia la lista de roles, dejándola vacía. Para permitir nuevamente la verificación."""
        self.head = None
        self.size = 0


class Counter:
    """
    Clase auxiliar para llevar un conteo acumulativo de forma mutable,
    sin usar listas, enteros globales ni estructuras nativas no permitidas.

    Se utiliza para llevar el control de elementos agregados válidos,
    como por ejemplo jugadores menores de 25 años, entre múltiples listas.
    """

    def __init__(self):
        self.valor = 0

    def increment(self):
        """Incrementa el valor interno en uno."""
        self.valor += 1

    def get_counter(self):
        """Devuelve el valor actual acumulado."""
        return self.valor


def is_staff(rol):
    """
    Verifica si el rol pertenece al cuerpo técnico.

    Esta función evalúa explícitamente si el rol coincide con uno de los 4
    permitidos para el cuerpo técnico:

    Args:
        rol (str): El rol a evaluar.

    Returns:
        bool: True si el rol es válido para el cuerpo técnico, False en caso contrario.
    """
    return (
        rol == "entrenador"
        or rol == "segundo entrenador"
        or rol == "medico de cabecera"
        or rol == "utilero"
    )


def is_directive(rol):
    """
    Verifica si el rol pertenece a la directiva del equipo.

    Esta función evalúa de manera explícita si el rol coincide con uno de los 4
    roles válidos de la directiva:

    **Nota: El diseño alternativo se enfoca en evitar el uso de estructuras iterables.
    Nunca se ha realizado la aclaración de: "No usar listas ni vectores de python" incluye cualquier tipo de estructura iterable.**

    Args:
        rol (str): El rol a evaluar.

    Returns:
        bool: True si el rol pertenece a la directiva, False en caso contrario.
    """
    return (
        rol == "presidente"
        or rol == "vicepresidente"
        or rol == "director deportivo"
        or rol == "secretario técnico"
    )


class SimpleCircularLinkedList:
    # Definimos las constantes fuera del constructor ya que no cambian según la instancia.
    NUM_PLAYERS = 6
    NUM_DIRECTIVES = 4
    NUM_STAFF = 4

    def __init__(self):
        """Constructor de clase para inicializar una lista simplemente ligada circular.
        Args:
            self: define la cabecera null por defecto
            self: (size_*) : 3 acumuladores para medir cantidad de jugadores, directivos
            y miembros del staff.
        """
        self.head = None
        self.size = 0
        self.size_player = 0
        self.size_staff = 0
        self.size_directive = 0

        # Instancias para obtener los roles únicos de directiva y staff para hacer verificaciones. Se crean dos LSL debido a la imposbilidad, dada por el requerimiento del usuario (en este caso la profeosora), de usar listas nativas de python, o sets para la verificación por medio de un for ordinario.

        self.roles_staff = ListaRolesUnicos()
        self.roles_directiva = ListaRolesUnicos()

    def validar_y_actualizar_rol(self, role: str):
        """
        Valida y actualiza el rol según el tipo de integrante.

        Validación.
        Tipos de validaciones.

        1. Por Rol: Verifica si estamos ante un jugador / integrante del staff o de la directiva.

        2. Tamaño de ingrantes:
            - Límite de 6 jugadores por equipo)
            - Límite de 4 miembros para el staff
            - Límite de 4 miembros para la directiva del equipo.

        3. (Exclusivo de staff y directiva: los roles deben ser únicos.

        Ejm: No deben existir dos presidentes en la directiva o dos entrenadores (primer técnico) en el staff.

        """

        rol = role.lower()

        if rol == "jugador":
            if self.size_player >= self.NUM_PLAYERS:
                raise ValueError(
                    f"No se pueden registrar más de {self.NUM_PLAYERS} jugadores."
                )
            self.size_player += 1

        elif is_staff(rol):
            if self.roles_staff.get_size() >= self.NUM_STAFF:
                raise ValueError(
                    f"No se pueden registrar más de {self.NUM_STAFF} integrantes del cuerpo técnico."
                )
            if not self.roles_staff.append_role(rol):
                raise ValueError(
                    f"El rol '{rol}' ya está registrado en el cuerpo técnico."
                )
            self.size_staff += 1

        elif is_directive(rol):
            if self.roles_directiva.get_size() >= self.NUM_DIRECTIVES:
                raise ValueError(
                    f"No se pueden registrar más de {self.NUM_DIRECTIVES} integrantes de la directiva."
                )
            if not self.roles_directiva.append_role(rol):
                raise ValueError(f"El rol '{rol}' ya está registrado en la directiva.")
            self.size_directive += 1

        else:
            raise ValueError(f"Rol inválido o no permitido: {role}")
    

    def head_list_null(self):
        """verifica si la LSLC está vacia.
        Nota: Si la cabecera está vacia no existen nodos en la LSLC"""
        return self.head is None

    def insert_into_empty_list(self, new_node):
        """
        Este método es llamado cuando la LSLC está vacía.

        Permite tomar el nodo proporcionado "new_node" como la cabecera (head) de la LSLC
        y hace que su referencia 'next' apunte a sí mismo. (Para ser circular)

        Args:
            new_node (Node): Nodo que se insertará como único elemento de la lista.
        """
        self.head = new_node
        new_node.next = new_node
        self.size = 1

    def insert_at_end(self, id: str, name: str, age: int, role: str, team: int):
        """
        Este método permite insertar nodos en un LSLC

        Si la lista está vacía, se invoca insert_into_empty_list.
        En caso contrario, el nuevo nodo se enlaza al final y
        su referencia 'next' apunta nuevamente al head.
        Args:
            value: valor del noto
        """

        # Validar tipo de integrante y actualizar contadores
        self.validar_y_actualizar_rol(role)

        # Instancia para crear un nuevo nodo.
        new_node = Node.create(id, name, age, role, team)

        # Si la lista está vacía, insertamos el primer nodo.
        if self.head_list_null():
            self.insert_into_empty_list(new_node)
        else:
            """
            Si la lista no se encuentra vacia debemos.

            1. Establecer un nodo actual y partir desde la cabecera

            2. Recorrer la lista hasta e ir actualizando el nodo acutal hasta que current.next sea igual a la cabecera, esto significará que ya estamos en el último nodo.

            3. Enlazamos el nuevo nodo y luego lo apuntamos a la cabecera utilizando su liga (new_node.next = self.head)

            4. Actualizamos el acumulador que nos da el tamaño de la lista, para controlar el tamaño del equipo.
            """
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.size += 1

    def contar_validos_para_equipo(self):
        """
        Recorre la lista circular y cuenta:
        - jugadores menores de 25 (máximo 6)
        - roles únicos válidos en staff (máximo 4)
        - roles únicos válidos en directiva (máximo 4)

        Returns:
            tuple: (jugadores, staff_validos, directiva_validos)
        """
        if self.head_list_null():
            return (0, 0, 0)

        jugadores = Counter()
        roles_staff = ListaRolesUnicos()
        roles_directiva = ListaRolesUnicos()

        current = self.head
        while True:
            if current.age < 25:
                rol = current.role.lower()
                if rol == "jugador" and jugadores.get_counter() < self.NUM_PLAYERS:
                    jugadores.increment()
                elif is_staff(rol):
                    roles_staff.append_role(rol)
                elif is_directive(rol):
                    roles_directiva.append_role(rol)
            current = current.next
            if current == self.head:
                break

        return (jugadores.get_counter(), roles_staff.get_size(), roles_directiva.get_size())

    
    def print_list(self):
        """
        Recorre una lista simplemente ligada circualar.

        Nota: Para recorrer la lista debemos:

            1. Verificar que la lista no esté vacia (No habría nada que recorrer)

            2. Establecer un elemento actual que inicia en la cabecera.

            3. Imprime el conjunto de valores asignados al Nodo actual. (Args*: (id,name,role,team))

            4. Actualizar el elemento acutual pasando al next. (Previa verificación de que no sea el último.

            5. La verificación se realiza tomomando la liga izquierda y pregutando si el next elemento existe. Se detiene cuando el nodo actual sea igual a la cabecera.

        Imprime en consola todos los nodos de la lista circular,
        mostrando sus atributos (id, name, age, role, team).

        Si la lista está vacía, imprime un mensaje indicándolo.
        """
        if self.head is None:
            print("La lista está vacía.")
            return

        current = self.head
        while True:
            print(
                f"ID: {current.id}, "
                f"Nombre: {current.name}, "
                f"Edad: {current.age}, "
                f"Rol: {current.role}, "
                f"Equipo: {current.team}"
            )
            current = current.next
            if current == self.head:
                break


# Parte 2 lista simplmente ligada.
class NodeLdl:
    """
    Representa un nodo en una lista doblemente ligada.

    Args:
        args* (id/name/age/role/team): Contenido del nodo.
        next: Referencia al siguiente nodo en la lista.
        previous: Referencia al nodo anterior en la lista.
    """

    def __init__(self, id: str, name: str, age: int, role: str, team: int):
        self.id = id
        self.name = name
        self.age = age
        self.role = role
        self.team = team
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        """Inicializa la cabecera, la cola y el tamaño de una lista doblemente enlazada.
        Por defecto, la lista comienza vacía.
        """

        self.head = None
        self.last = None
        self.size = 0

    def list_null(self):
        """verifica si la LDL está vacia.
        Nota: Si la cabecera está vacia no existen nodos en la LDL"""
        return self.head is None

    def insert_node_at_end(self, id, name, age, role, team):
        """Permite insertar un nodo en la posición final de la LDL

        Args:
            id, name, age, role, team : Ya tratados en las listas circulares.
        """
        # Instancia para crear un nuevo nodo.
        new_node = NodeLdl(id, name, age, role, team)

        # Si la lista está vacía, el nuevo nodo es el primero y último
        if self.list_null():
            self.head = self.last = new_node

        else:
            """
            Si la lista no se encuentra vacia debemos.
            1. Enlazar último nodo con el nuevo a través de su liga derecha.

            2. Enlazar el nuevo nodo, con el nodo que hasta entonces era el último,
               utilizando su liga izquierda.

            3. Asignar a la cola el nuevo nodo (Que ahora es el último).

            4. Incrementar el tamaño de la lista en una unidad"""
            self.last.next = new_node  # 1.
            new_node.previous = self.last  # 2.
            self.last = new_node  # 3.

        self.size = self.size + 1  # 4.

    def print_list(self):
        """Imprime todos los nodos de la lista doblemente ligada."""
        current = self.head
        while current:
            print(
                f"ID: {current.id}, Nombre: {current.name}, Edad: {current.age}, Rol: {current.role}, Equipo: {current.team}"
            )
            current = current.next


class GestorFusion:
    """
    Clase que gestiona la fusión de dos listas simplemente ligadas circulares
    en una lista doblemente ligada final que represente un nuevo equipo válido.

    Esta clase se encarga de:
    - Filtrar elementos válidos de acuerdo a restricciones (edad y unicidad de rol).
    - Llevar control del número de jugadores válidos agregados.
    - Verificar que se cumplan las condiciones para una fusión exitosa.

    Requisitos que debe cumplir el equipo combinado:
    - Máximo 5 jugadores menores de 25 años.
    - 4 roles únicos de cuerpo técnico.
    - 4 roles únicos de directiva.

    A través de métodos internos, esta clase controla el estado de conteo y roles,
    y permite reiniciarlos al comenzar una nueva operación.
    """

    JUGADOR = "jugador"

    def __init__(self):
        self.jugadores_global = Counter()
        self.roles_staff = ListaRolesUnicos()
        self.roles_directiva = ListaRolesUnicos()

    def fusionar_equipos_balanceado(self, e1, e2):
        """
        Intenta fusionar dos equipos (e1 y e2) de forma estrictamente balanceada:

        1. Alterna turnos entre ambos equipos para insertar un nodo válido por turno.

        2. Un nodo es válido si cumple con restricciones de edad (< 25 años)
          y no sobrepasa los límites de su categoría (jugador, staff, directiva).

        3. Se detiene cuando se han insertado 14 elementos válidos en total
          (6 jugadores, 4 staff, 4 directivos).
        4. Se asegura que cada equipo haya aportado exactamente 7 integrantes válidos.

        Si no se puede lograr:
        - Lanza una excepción indicando qué equipo aportó más.
        - También valida que los roles estén completamente cubiertos.

        Returns:
            DoublyLinkedList: equipo combinado si se cumplen todas las condiciones.
        """

        # Creamos una instancia de la clase para la lista doblemente ligada.
        nuevo_equipo = DoublyLinkedList()

        # Crea dos contadores para ir actualizando la cantiad de integrantes tomados de los dos equipos. Se intercalan en un contador general
        count_e1 = Counter()
        count_e2 = Counter()

        # Concedemos el primer turno a e1 (se realiza con este validador al no poder usar estrcturas nativas listas/vectores/tuplas)
        turno_e1 = True

        # Creamos nodos actuales para recorrer ambas LSL (e1, e2) partiendo desde la cabecera de c/u.
        current_e1 = e1.head
        current_e2 = e2.head

        # Establecemos un control para el total de integrantes de un equipo.
        completado = False

        # Validación previa: asegurarse de que ambos equipos puedan al menos aportar 7 válidos
        jug_e1, staff_e1, dir_e1 = e1.contar_validos_para_equipo()
        jug_e2, staff_e2, dir_e2 = e2.contar_validos_para_equipo()

        total_validos_e1 = jug_e1 + staff_e1 + dir_e1
        total_validos_e2 = jug_e2 + staff_e2 + dir_e2

        if total_validos_e1 < 7 or total_validos_e2 < 7:
            raise ValueError(
                f"Uno de los equipos no puede aportar al menos 7 integrantes válidos. "
                f"Equipo 1: {total_validos_e1}, Equipo 2: {total_validos_e2}"
        )
        # Vamos a alternar sobre los nodos de ambas LSL (e1 , e2) hasta que el tamaño
        # Jugadores + Directiva + staff complete un equipo nuevo.
        while (
            self.jugadores_global.get_counter()
            + self.roles_staff.get_size()
            + self.roles_directiva.get_size()
            < 14
        ):
            # Asinamos a la variable
            # contador: se asigna el contador correspondiente (_e1,_e2) según el turno
            # Identicamente con el nodo actual.
            if turno_e1:
                equipo = e1
                contador = count_e1
                current = current_e1
            else:
                equipo = e2
                contador = count_e2
                current = current_e2

                # Si la lista está vacia cambiamos de LSL ("cambio de equipo").
                if equipo.head_list_null():
                    turno_e1 = not turno_e1
                    continue

            # Recorremos una sola vuelta por la lista circular del equipo actual
            # utilizando la condición clásica: cuando el nodo siguiente apunta a la cabecera.
            cabecera = current
            while True:
                if current.age < 25:
                    rol = current.role.lower()
                    puede_insertar = False

                    if rol == self.JUGADOR:
                        if self.jugadores_global.get_counter() < 6:
                            puede_insertar = True
                    
                    # Validamos si el rol pertenece al staff técnico y si no está repetido (rol único) (Identico comportamiento para la directiva)
                    elif is_staff(rol) and self.roles_staff.append_role(rol):
                        puede_insertar = True
                    elif is_directive(rol) and self.roles_directiva.append_role(rol):
                        puede_insertar = True

                    # Insersión comun de un nodo valido
                    if puede_insertar:
                        nuevo_equipo.insert_node_at_end(
                            current.id,
                            current.name,
                            current.age,
                            current.role,
                            current.team,
                        )
                        
                        #Incremento contador global de jugadores
                        if rol == self.JUGADOR:
                            self.jugadores_global.increment()
                        
                        # Se incrementa el contador de nodos validos del equipo
                        contador.increment()
                        
                        # Apuntamos al nodo siguiente según el turno de la LSLC
                        if turno_e1:
                            current_e1 = current.next
                        else:
                            current_e2 = current.next
                        break
                
                # Preguntamos si el nodo actual.siguiente (current.next) es la cabecera 
                
                # Significará haber recorrido todos los nodos y no haber encontrado que insertar. 
                
                # Actualizamos el nodo para empezar desde el proximo.
                
                # Sale del bucle interno.
                if current.next == cabecera:
                    if turno_e1:
                        current_e1 = current.next
                    else:
                        current_e2 = current.next
                    break
                current = current.next

            # Cambio de turno (Cambio de LSL).
            turno_e1 = not turno_e1

            # Si ambos equipos no pueden aportar más, se detiene
            if count_e1.get_counter() + count_e2.get_counter() == 14:
                completado = True
                break

        if not completado:
            raise ValueError(
                "No fue posible completar el equipo de forma balanceada con roles válidos y edad permitida."
            )

        if self.roles_staff.get_size() != SimpleCircularLinkedList.NUM_STAFF:
            raise ValueError("No se logró cubrir todos los roles del cuerpo técnico.")

        if self.roles_directiva.get_size() != SimpleCircularLinkedList.NUM_DIRECTIVES:
            raise ValueError("No se logró cubrir todos los roles de la directiva.")

        if self.jugadores_global.get_counter() != SimpleCircularLinkedList.NUM_PLAYERS:
            raise ValueError("No se logró cubrir los 6 puestos de jugadores.")

        if count_e1.get_counter() != count_e2.get_counter():
            raise ValueError(
                f"El equipo 1 aportó {count_e1.get_counter()} y el equipo 2 {count_e2.get_counter()}, pero deben aportar la misma cantidad."
            )

        return nuevo_equipo


if __name__ == "__main__":

    # Se recomienda poner un punto de interrupción aquí para probar cada caso en la consola de depuración. 
    print("Aquí!")
    """
    Nuevamente debido a la restricción de uso de listas y estructuras iterables se opta por crear manualmualmente cada instancia necesaria.
    """
    
    equipo1 = SimpleCircularLinkedList()
    equipo2 = SimpleCircularLinkedList()

    #-------------------------------------------------------------------------------------
    ################################ CASO 1 (EXITOSO) ###################################

    # Agregar jugadores (5 por equipo, todos menores de 25)
    equipo1.insert_at_end("E1J0", "Jugador0", 20, "jugador", 1)
    equipo1.insert_at_end("E1J1", "Jugador1", 21, "jugador", 1)
    equipo1.insert_at_end("E1J2", "Jugador2", 22, "jugador", 1)
    equipo1.insert_at_end("E1J3", "Jugador3", 23, "jugador", 1)
    equipo1.insert_at_end("E1J4", "Jugador4", 24, "jugador", 1)
    equipo1.insert_at_end("E1J4", "Jugador5", 24, "jugador", 1)

    equipo2.insert_at_end("E2J0", "Jugador0", 21, "jugador", 2)
    equipo2.insert_at_end("E2J1", "Jugador1", 22, "jugador", 2)
    equipo2.insert_at_end("E2J2", "Jugador2", 21, "jugador", 2)
    equipo2.insert_at_end("E2J3", "Jugador3", 22, "jugador", 2)
    equipo2.insert_at_end("E2J4", "Jugador4", 21, "jugador", 2)
    equipo2.insert_at_end("E2J4", "Jugador5", 24, "jugador", 1)

    # Agregar directiva (4 roles únicos por equipo, sin listas)
    equipo1.insert_at_end("E1D0", "Directivo0", 24, "presidente", 1)
    equipo1.insert_at_end("E1D1", "Directivo1", 24, "vicepresidente", 1)
    equipo1.insert_at_end("E1D2", "Directivo2", 24, "director deportivo", 1)
    equipo1.insert_at_end("E1D3", "Directivo3", 24, "secretario técnico", 1)

    equipo2.insert_at_end("E2D0", "Directivo0", 22, "presidente", 2)
    equipo2.insert_at_end("E2D1", "Directivo1", 22, "vicepresidente", 2)
    equipo2.insert_at_end("E2D2", "Directivo2", 22, "director deportivo", 2)
    equipo2.insert_at_end("E2D3", "Directivo3", 22, "secretario técnico", 2)

    # Agregar staff técnico (4 roles únicos por equipo, sin listas)
    equipo1.insert_at_end("E1S0", "Staff0", 23, "entrenador", 1)
    equipo1.insert_at_end("E1S1", "Staff1", 23, "segundo entrenador", 1)
    equipo1.insert_at_end("E1S2", "Staff2", 23, "medico de cabecera", 1)
    equipo1.insert_at_end("E1S3", "Staff3", 23, "utilero", 1)

    equipo2.insert_at_end("E2S0", "Staff0", 21, "entrenador", 2)
    equipo2.insert_at_end("E2S1", "Staff1", 21, "segundo entrenador", 2)
    equipo2.insert_at_end("E2S2", "Staff2", 21, "medico de cabecera", 2)
    equipo2.insert_at_end("E2S3", "Staff3", 21, "utilero", 2)



    print("CASO 1 - Equipo válido y balanceado:")
    try:
        gestor = GestorFusion()
        nuevo_equipo = gestor.fusionar_equipos_balanceado(equipo1, equipo2)
        print("Equipo combinado exitosamente:\n")
        nuevo_equipo.print_list()
    except ValueError as e:
        print(f"Error: {e}")
    

    #-------------------------------------------------------------------------------------
    ################################ CASO 2 (FALLA) ######################################

    #print("\nCASO 2 - Faltan cuerpo tecnico y directiva:")
    equipo_incompleto = SimpleCircularLinkedList()
    equipo2 = SimpleCircularLinkedList()
    
    # Solo 5 jugadores
    equipo_incompleto.insert_at_end("E3J0", "Jugador0", 21, "jugador", 1)
    equipo_incompleto.insert_at_end("E3J1", "Jugador1", 22, "jugador", 1)
    equipo_incompleto.insert_at_end("E3J2", "Jugador2", 22, "jugador", 1)
    equipo_incompleto.insert_at_end("E3J3", "Jugador3", 23, "jugador", 1)
    equipo_incompleto.insert_at_end("E3J4", "Jugador4", 24, "jugador", 1)
    
    equipo2.insert_at_end("E2J0", "Jugador0", 21, "jugador", 2)
    equipo2.insert_at_end("E2J1", "Jugador1", 22, "jugador", 2)
    equipo2.insert_at_end("E2J2", "Jugador2", 21, "jugador", 2)
    equipo2.insert_at_end("E2J3", "Jugador3", 22, "jugador", 2)
    equipo2.insert_at_end("E2J4", "Jugador4", 21, "jugador", 2)
    equipo2.insert_at_end("E2J4", "Jugador5", 24, "jugador", 1)
    # Se puede usar equipo2 como contraparte
    try:
        gestor = GestorFusion()
        nuevo_equipo = gestor.fusionar_equipos_balanceado(equipo_incompleto, equipo2)
        nuevo_equipo.print_list()
    except ValueError as e:
        print(f"Error: {e}")

    #-------------------------------------------------------------------------------------
    ################################ CASO 3 (Falla) ######################################

    print("\nCASO 3 - Staff duplicado:")
    equipo_duplicado = SimpleCircularLinkedList()
    equipo_duplicado.insert_at_end("E4J0", "Jugador0", 22, "jugador", 4)
    equipo_duplicado.insert_at_end("E4J1", "Jugador1", 22, "jugador", 4)
    equipo_duplicado.insert_at_end("E4J2", "Jugador2", 22, "jugador", 4)
    equipo_duplicado.insert_at_end("E4J3", "Jugador3", 22, "jugador", 4)
    equipo_duplicado.insert_at_end("E4J4", "Jugador4", 22, "jugador", 4)
    equipo_duplicado.insert_at_end("E4J5", "Jugador5", 22, "jugador", 4)

    # Staff duplicado (2 entrenadores)
    equipo_duplicado.insert_at_end("E4S0", "Staff0", 22, "entrenador", 4)
    equipo_duplicado.insert_at_end("E4S1", "Staff1", 22, "entrenador", 4)
    equipo_duplicado.insert_at_end("E4S2", "Staff2", 22, "medico de cabecera", 4)
    equipo_duplicado.insert_at_end("E4S3", "Staff3", 22, "utilero", 4)

    equipo_duplicado.insert_at_end("E4D0", "Directivo0", 22, "presidente", 4)
    equipo_duplicado.insert_at_end("E4D1", "Directivo1", 22, "vicepresidente", 4)
    equipo_duplicado.insert_at_end("E4D2", "Directivo2", 22, "director deportivo", 4)
    equipo_duplicado.insert_at_end("E4D3", "Directivo3", 22, "secretario técnico", 4)

    try:
        gestor = GestorFusion()
        nuevo_equipo = gestor.fusionar_equipos_balanceado(equipo_duplicado, equipo2)
        nuevo_equipo.print_list()
    except ValueError as e:
        print(f"Error: {e}")


    #-------------------------------------------------------------------------------------
    ################################ CASO 4 (FALLA)  ####################################
    print("\nCASO 4 - Error por tipo de dato incorrecto (edad como string):")
    equipo_error = SimpleCircularLinkedList()
    equipo2 = SimpleCircularLinkedList()

    try:
        # Este insertará mal la edad como string → debería ser int
        equipo_error.insert_at_end("E4J0", "Jugador0", "veintidós", "jugador", 1)
    except TypeError as e:
        print(f"Error detectado en creación del nodo: {e}")



    ######################### CASO 5 (EXITOSO) ########################################
    print("\nCASO 5 - Con algunos mayores de 25 pero se logra formar el equipo completo balanceado:")

    '''
    Notemos que este caso es interesante ya que aunque algunas personas no son validas con los datos ingresados se puede formar un equipo valido. Tomando igual cantidad de personas.'''
    equipo1 = SimpleCircularLinkedList()
    equipo2 = SimpleCircularLinkedList()

    # EQUIPO 1 – mezcla válidos y mayores
    equipo1.insert_at_end("E1J0", "Jugador0", 26, "jugador", 1)  # No válido
    equipo1.insert_at_end("E1J1", "Jugador1", 24, "jugador", 1)
    equipo1.insert_at_end("E1J2", "Jugador2", 23, "jugador", 1)
    equipo1.insert_at_end("E1J3", "Jugador3", 22, "jugador", 1)

    equipo1.insert_at_end("E1S0", "Staff0", 24, "entrenador", 1)
    equipo1.insert_at_end("E1S1", "Staff1", 24, "segundo entrenador", 1)
    equipo1.insert_at_end("E1D0", "Directivo0", 23, "presidente", 1)
    equipo1.insert_at_end("E1D1", "Directivo1", 21, "vicepresidente", 1)

    # EQUIPO 2 – completa lo faltante
    equipo2.insert_at_end("E2J0", "Jugador4", 23, "jugador", 2)
    equipo2.insert_at_end("E2J1", "Jugador5", 21, "jugador", 2)
    equipo2.insert_at_end("E2J2", "Jugador6", 22, "jugador", 2)

    equipo2.insert_at_end("E1S0", "Staff0", 29, "entrenador", 2)
    equipo2.insert_at_end("E2S2", "Staff2", 23, "medico de cabecera", 2)
    equipo2.insert_at_end("E2S3", "Staff3", 23, "utilero", 2)
    equipo2.insert_at_end("E1D0", "Directivo0", 24, "presidente", 2)
    equipo2.insert_at_end("E2D2", "Directivo2", 23, "director deportivo", 2)
    equipo2.insert_at_end("E2D3", "Directivo3", 23, "secretario técnico", 2)

    try:
        gestor = GestorFusion()
        combinado = gestor.fusionar_equipos_balanceado(equipo1, equipo2)
        print("Equipo combinado correctamente (algunos mayores fueron descartados):")
        combinado.print_list()
    except ValueError as e:
        print(f"Error: {e}")
        
        
