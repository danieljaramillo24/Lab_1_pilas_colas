"""
2. En la central de atención de Tigo se desea mejorar el sistema de atención. En este 
momento funciona con múltiples colas (representadas como Listas doblemente
ligadas, una por cada asesor). Se desea conocer cuál es el tiempo promedio de 
atención de cada asesor, para cada una de las tres atenciones que se realiza:
a. Línea nueva
b. Daño en el dispositivo o servicio
c. Problemas de facturación

No se deben realizar supuestos adicionales. 
"""

class NodeAtention:
    """
    Representa un nodo en una lista doblemente ligada personalizado para crear atenciones.

    Args:
        type_att: (str): tipo de atención brindada : (Linea nueva/Daño dispositivo/Problema facturación).

        time_att (int): tiempo de atención para el requerimiento.

        next: Referencia al siguiente nodo en la lista.

        previous: Referencia al nodo anterior en la lista.
    """

    def __init__(self, type_att: str, time_att: int):
        self.type_att = type_att
        self.time_att = time_att
        self.next = None
        self.previous = None


class NodeContenedorAsesor:
    """
    Representa un nodo en una lista doblemente ligada de asesores.

    Args:
        asesor (Asesor): Objeto asesor que contiene nombre y lista de atenciones.
        next: Referencia al siguiente nodo en la lista.
        previous: Referencia al nodo anterior en la lista.
    """

    def __init__(self, asesor: "Asesor"):
        self.asesor = asesor
        self.next = None
        self.previous = None


class DoublyLinkedListGenerica:
    """
    Lista doblemente ligada genérica para almacenar nodos de cualquier tipo.

    Attributes:
        head (Node): Primer nodo de la lista.
        last (Node): Último nodo de la lista.
        size (int): Número de nodos en la lista.
        node_class (type): Clase de nodo a utilizar en las inserciones.

        Nota aclaratoria: Notemos que en la construcción de la solución al tratarse de un problema de una LDL con multiples colas ( mas LDL ), al momento de la inserción se puede utilizar un procedimiento común.

        (Revisar instancia del nodo)
    """

    def __init__(self, node_class):
        self.head = None
        self.last = None
        self.size = 0
        self.node_class = node_class

    def list_null(self):
        """
        Verifica si la lista está vacía.

        Returns:
            bool: True si está vacía, False en caso contrario.
        """
        return self.head is None

    def insert_node_at_end(self, *args, **kwargs):
        """
        Inserta un nodo en la posición final de la lista.

        Args:
            *args, **kwargs: Argumentos a pasar al constructor del nodo.

            Dependen del nodo a crear
        """
        # Instancia para crear un nuevo nodo.
        new_node = self.node_class(*args, **kwargs)

        """La diferencia en inserción reside en el tipo de nodo a agregar y la natrualeza de los argumentos (Parámetros == Valores que contiene el nodo). 
        
        Así podremos instanciar nodos de diferentes tipos que varien en sus parámetros.
        
        se define la estructura *args, **kwargs para ampliar la preferencia de paso de parámetros. """

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

            4. Incrementar el tamaño de la lista en una unidad
            """
            self.last.next = new_node  # 1.
            new_node.previous = self.last  # 2.
            self.last = new_node  # 3.

        self.size = self.size + 1  # 4.


class Asesor:
    """
    Objeto que contiene un asesor con nombre y su lista de atenciones.

    Attributes:
        nombre (str): Nombre del asesor.
        atenciones (DoublyLinkedList): Lista de atenciones del asesor.

    Notemos: Por definición tenemos múltiples colas y cada lista doblemente ligada representa el conjunto de atenciones de un asesor en particular. Abstraermos esta representación de un asesor en una clase para mejorar la legibilidad.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.atenciones = DoublyLinkedListGenerica(NodeAtention)


class AnalizadorAtencion:
    """
    Permite analizar múltiples asesores y calcular promedios de atención por tipo.
    """

    def __init__(self):
        # creamos una instacia de lista genérica con nodos NodeContenedorAsesor

        # Se usa el nombre completo para inferir que NodeContenedorAsesor contiene esta iformación completa (Nombre y  LDL)
        self.asesores = DoublyLinkedListGenerica(NodeContenedorAsesor)

    def agregar_asesor(self, asesor: "Asesor"):
        """
        Agrega un asesor con su lista de atenciones.

        Args:
            asesor (Asesor): Objeto asesor. Contiene *Nodo* configurado con el nombre del asesor y  su lista de atenciones.
            previamente encapsulado en una clase.

        (Se define adicionalmente para mayor claridad visual en la instancia)
        """
        self.asesores.insert_node_at_end(asesor)

    def mostrar_asesores(self):
        """
        Recorre e imprime el nombre de cada asesor junto con la cantidad de atenciones
        y el detalle individual de cada una (tipo y tiempo).

        Este método permite visualizar en cualquier momento el contenido actual de la lista
        de asesores y sus respectivas colas de atención.
        """
        if self.asesores.list_null():
            print("No hay asesores registrados en la lista.")
            return

        current = self.asesores.head
        numero = 1

        while current is not None:
            asesor = current.asesor
            print(
                f"\nAsesor {numero}: {asesor.nombre} - Total atenciones: {asesor.atenciones.size}"
            )

            nodo_atencion = asesor.atenciones.head
            num_atencion = 1

            while nodo_atencion is not None:
                type_a = nodo_atencion.type_att
                time = nodo_atencion.time_att
                print(f"  Atención {num_atencion}: {type_a} - {time} min")
                nodo_atencion = nodo_atencion.next
                num_atencion += 1

            current = current.next
            numero += 1

    def calcular_promedios(self):
        """
        Calcula y muestra el tiempo promedio por tipo de atención para cada asesor.
        
        ¿Como se calculan y almacenan los promedios? 
        
        1. Vericamos que existan asesores.
        
        2. Vamos a recorrer la lista de asesores partiendo desde la cabecera. Hacemos nodo actual igual a la cabecera. 
        
        3. Mientras el nodo actual no sea nulo, extramemos el objeto "asesor" (Recordemos que este es un objeto de la clase "Asesor" y contiene el nombre del asesor y su correspondiente lista de atenciones)
        
        4. Guardamos la lista de atenciones en una variable accediendo por asesor.atenciones (Recordemos: asesor.atenciones = DoublyLinkedListGenerica(NodeAtention))
        
        5. Definimos 3 contadores: count_ln, count_dn ,count_fac. (Cuentan la cantidad de cada servicio, que brindó el asesor)
        
        6. Similarmente 3 acumuladores: sum_ln, sum_dn , sum_fac. (Acumulan la el tiempo por cada servicio según su categoría)
        
        7. Ahora como la lista de atenciones es otra LDL, partimos de su cabecera, extraemos sus valores (Recordemos que se crean con base en el objeto NodeAtention, que contiene tipo de atención y tiempo de la misma. )
        
        8. En el recorrido actualizamos contadores y acumuladores,  además verificamos que los tiempos sean postivos. 
        
        9. Calculamos un promedio simple post recorrer todos los nodos del asesor actual.
        
        10. Pasamos al siguiente asesor en "asesores" , y le damos el número siguiente a otro asesor. 
        """
        
        if self.asesores.list_null():
            print("No hay asesores registrados.")
            return

        current_asesor = self.asesores.head
        num_asesor = 1

        while current_asesor is not None:
            asesor = current_asesor.asesor
            list_atencions = asesor.atenciones

            print(f"\nAsesor {num_asesor} - {asesor.nombre}:")

            #6           #5
            sum_tm_ln =  count_ln = 0  # Línea nueva
            sum_tm_dn =  count_dn = 0  # Daño
            sum_tm_fac = count_fac = 0  # Facturación

            nodo_atentions = list_atencions.head #7

            while nodo_atentions is not None:  #7 
                type_a = nodo_atentions.type_att
                tiempo = nodo_atentions.time_att
                
                #8
                if not isinstance(tiempo, int) or tiempo < 0:
                    print(f" Tiempo inválido: '{tiempo}'")
                elif type_a == "Línea nueva":
                    sum_tm_ln += tiempo
                    count_ln += 1
                elif type_a == "Daño":
                    sum_tm_dn += tiempo
                    count_dn += 1
                elif type_a == "Facturación":
                    sum_tm_fac += tiempo
                    count_fac += 1
                else:
                    print(f"Tipo desconocido: '{type_a}'")

                nodo_atentions = nodo_atentions.next

            #9
            if count_ln > 0:
                print(f"  Promedio Línea nueva: {sum_tm_ln / count_ln} min")
            if count_dn > 0:
                print(f"  Promedio Daño: {sum_tm_dn / count_dn} min")
            if count_fac > 0:
                print(f"  Promedio Facturación: {sum_tm_fac / count_fac} min")

            #10.
            current_asesor = current_asesor.next
            num_asesor += 1


# Crear asesor 1
asesor1 = Asesor("Daniel Jaramillo")
asesor1.atenciones.insert_node_at_end("Línea nueva", 10)
asesor1.atenciones.insert_node_at_end("Facturación", 5)
asesor1.atenciones.insert_node_at_end("Daño", 12)
asesor1.atenciones.insert_node_at_end("Línea nueva", 15)


# Crear asesor 2
asesor2 = Asesor("Paola Andrea Galindo")
asesor2.atenciones.insert_node_at_end("Facturación", 8)
asesor2.atenciones.insert_node_at_end("Daño", 9)
asesor2.atenciones.insert_node_at_end("Facturación", 10)
asesor2.atenciones.insert_node_at_end("Daño", 10)
# Crear analizador
analizador = AnalizadorAtencion()
analizador.agregar_asesor(asesor1)
analizador.agregar_asesor(asesor2)
analizador.mostrar_asesores()


# Ejecutar análisis
print("Calcular promedios")
analizador.calcular_promedios()
