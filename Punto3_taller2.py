"""3. Una empresa se dedica a la venta de llantas para vehículos. Las llantas están
organizadas por marca (se venden tres tipos de marcas), desde el mayor
radial hasta el menor radial (apiladas de mayor a menor). Cada vez que un
cliente llega se debe mostrar la llanta solicitada, para lo cual se debe mover
las llantas como una pila que son. Cada llanta esta etiquetada con un código.
Se debe registrar cada venta de llanta, en una cola, identificando la venta
hecha y llanta vendida. Diseñe e implemente una solución.

No se requieren supuestos adicionales: """


class NodePila:
    """
    Nodo para la pila de llantas.

    Attributes:
        codigo (str): Código de la llanta.
        next (NodePila): Enlace al siguiente nodo (None si es el último).
    """

    def __init__(self, codigo):
        self.codigo = codigo
        self.next = None


class NodeCola:
    """
    Nodo para la cola de ventas.

    Attributes:
        venta (Venta): Objeto que representa la venta realizada.
        next (NodeCola): Enlace al siguiente nodo (None si es el último).
    """

    def __init__(self, venta):
        self.venta = venta
        self.next = None


class Venta:
    """
    Representa una venta de una llanta por marca y código

    Attributes:
        marca (str): Marca de la llanta vendida.
        codigo (str): Código único de la llanta.
    """

    def __init__(self, marca, codigo):
        self.marca = marca
        self.codigo = codigo

    def __str__(self):
        # Formato definido para la impresión de una venta.
        return f"Venta: Marca={self.marca}, Código={self.codigo}"


class Stack:
    """
    Clase que se utiliza para crear una pila (LIFO) para almacenar llantas por marca.
    Las llantas se apilan desde el mayor hasta el menor radial.
    """

    def __init__(self):
        """
        Inicializa una pila vacía.
        Define el atributo 'top' como None para indicar que no hay elementos apilados.
        """
        self.top = None

    def stack_is_empty(self):
        """
        Verifica si la pila está vacía.

        Returns:
            bool: (True) si la pila está vacía, de lo contrario False.
        """
        return self.top is None

    def push(self, codigo):
        """
        Añade un nuevo elemento a la pila.

        Args:
            codigo: Código único que representa la llanta a añadir.

        Proceso para apilar un nuevo elemento:

        1. Crea un nuevo nodo con el código proporcionado.

        2. El nuevo nodo se enlaza al top (Nodo en la cima de la pila).

        3. El nuevo nodo se convierte en el "top" (La nueva cima de la pila).

        """
        node = NodePila(codigo)  # 1
        node.next = self.top  # 2
        self.top = node  # 3

    def pop(self):
        """
        Desapila un elemento de la pila.

        Returns:
            El código del elemento removido.

        Proceso para desapliar un elemento existente.

        1. Verifica si la pila contiene elementos (Sino no hay nada que desapilar)

        2. Guardamos el codigo del elemento que vamos a eliminar ( Para conservar el elemento
        que vamos a desapilar.)

        3. Actualizamos la cima de la pila al siguiente nodo.
        """

        # Vefifica si la pila está vacia.
        if self.stack_is_empty():  # 1
            return None

        codigo = self.top.codigo  # 2
        self.top = self.top.next  # 3
        return codigo


class Queue:
    """
    Clase que se utiliza para crear una cola vacia (FIFO)
    Cada venta se agrega al final de la cola.

    La cola trabaja similarmente a una LSL.
    """

    def __init__(self):
        """
        Inicializa una cola vacía.

        'front': Apunta al primer nodo de la cola (cabeza de la cola).
        'rear': Apunta al último nodo de la cola (final de la cola).

        Dado que la cola está vacia,  front y rear apuntan a None
        """
        self.front = None
        self.rear = None

    def queue_is_empty(self):
        """
        Verifica si la cola está vacía.

        Returns:
            bool: True si la cola no tiene elementos (front es None), False en caso contrario.
        """
        return self.front is None

    def enqueue(self, venta):
        """
        Agrega un nuevo elemento (venta) al final de la cola.

        Args:
            venta: La información de la venta que será almacenada en un nodo.

        Como encolar:
        1. Crea un nuevo nodo con la información de la venta.

        2. Si la cola está vacía, las dos ligas 'front' y 'rear' apuntan al nuevo nodo.

        3. Si la cola ya tiene elementos, se enlaza el nuevo nodo al final (usando 'rear.next')

        4. 'rear' se actualiza para que apunte al nuevo nodo.
        """
        node = NodeCola(venta)  # 1
        if self.queue_is_empty():  # 2
            self.front = self.rear = node
        else:
            self.rear.next = node  # 3
            self.rear = node  # 4

    def dequeue(self):
        """
        Remueve y devuelve el elemento al frente de la cola.

        Returns:
            La información de la venta en el primer nodo, si la cola no está vacía.
            Si la cola está vacía, devuelve None.

        Proceso:
        1. Verifica si la cola está vacía (si 'front' es None). Si está vacía, no hay nada que remover.

        2. Almacena la información de la venta del nodo al frente de la cola.

        3. Actualizamos la liga 'front' para que apunte al nodo siguiente.

        4. Si después de remover el nodo ya no quedan elementos, actualiza también 'rear' a None.
        """
        if self.queue_is_empty():
            return None
        venta = self.front.venta
        self.front = self.front.next  # 3.

        if self.front is None:  # 4.
            self.rear = None
        return venta

    def show_vtas(self):
        """
        Muestra en pantalla todos los elementos de la cola en orden, desde el frente hasta el final.

        Itera a través de todos los nodos de la cola, comenzando por 'front', y muestra
        la información de cada venta (por ejemplo, marca y código).

        Nota: el método show_vtas es adicional y maneja la cola como si fuera una LSL
        el método se implemente con motivos de visualización, pero como se vio en los metodos anteriores, (enqueue) y  (dequeue) las colas ofrecen la funcionalidad de enlazar nodos sin recorrer toda la estructura de datos.
        """

        # Recorreido tipico nodo a nodo.
        current = self.front
        while current is not None:
            venta = current.venta
            print(f"Marca: {venta.marca}, Código: {venta.codigo}")
            current = current.next


class TireShop:
    """
    Clase principal que gestiona las pilas de llantas por marca y la cola de ventas.
    """

    def __init__(self):
        """Instancias de pilas para cada tipo de llantas (tires), e instancia de una cola
        para almacenar las vtas.
        """
        self.michelin = Stack()
        self.metzeler = Stack()
        self.bridgestone  = Stack()
        self.ventas = Queue()

    def load_individual_tire(self, marca, codigo):
        """
        Inserta una nueva llanta a la pila correspondiente según la marca proporcionada.

        Args:
            marca (str): Nombre de la marca de la llanta (Michelin, Metzeler, Bridgestone).
            codigo (str): Código único que identifica la llanta.

        Según la  pila de la marca se agrega a la misma con .push

        """
        if marca == "Michelin":
            self.michelin.push(codigo)
        elif marca == "Metzeler":
            self.metzeler.push(codigo)
        elif marca == "Bridgestone":
            self.bridgestone.push(codigo)
        else:
            print(f"Marca desconocida: {marca}")

    def sell_tire(self, marca):
        """
        Gestiona la venta de una llanta según la marca especificada.

        Args:
            marca (str): Marca de la llanta que se desea vender (por ejemplo, "Michelin", "Metzeler", "Bridgestone").

        Proceso paso a paso:

        1. Identificación de la pila:
            - Se determina qué pila corresponde a la marca indicada.
            - Si la marca no está registrada, muestra un mensaje de error y termina el proceso.

        2. Verificación de disponibilidad:
            - Comprueba si hay llantas disponibles en la pila seleccionada.
            - Si la pila está vacía, muestra un mensaje indicando que no hay llantas disponibles y termina el proceso.

        3. Desapilado de una llanta:
            - Remueve una llanta de la pila correspondiente utilizando el método `pop()`.
            - Guarda el código de la llanta eliminada para generar una venta.

        4. Creación de la venta:
            - Instancia un objeto `Venta` con la marca y el código de la llanta que fue removida.

        5. Registro de la venta:
            - Agrega la nueva venta a la cola de ventas utilizando el método `enqueue()`.
            - Muestra un mensaje confirmando la venta realizada.
        """

        # 1
        pila = None
        if marca == "Michelin":
            pila = self.michelin
        elif marca == "Metzeler":
            pila = self.metzeler
        elif marca == "Bridgestone":
            pila = self.bridgestone 
        else:
            print(f"Marca no registrada: {marca}")
            return

        # 2
        if pila.stack_is_empty():
            print(f"No hay llantas disponibles de la marca {marca}.")
            return

        # 3
        codigo = pila.pop()

        # 4
        venta = Venta(marca, codigo)

        # 5
        self.ventas.enqueue(venta)
        print(f"{venta}")

    def get_history_vtas(self):
        """Historico de vtas

        Crea una instancia del método mostrar_vtas
        Que recorre la cola al estilo de una LSL, para mostrar cada nodo."""
        self.ventas.show_vtas()



#Prueba de la cola.
shop = TireShop()
shop.load_individual_tire("Michelin", "M300")
shop.load_individual_tire("Michelin", "M250")
shop.load_individual_tire("Michelin", "M200")

shop.load_individual_tire("Metzeler", "P320")
shop.load_individual_tire("Metzeler", "P280")

shop.load_individual_tire("Bridgestone", "G310")
shop.load_individual_tire("Bridgestone", "G260")
shop.load_individual_tire("Bridgestone", "G210")

# Podemos vender 2 de la pila Micheline 1 de Metzeler y todas de Bridgestone
shop.sell_tire("Michelin")
shop.sell_tire("Michelin")

shop.sell_tire("Metzeler")

shop.sell_tire("Bridgestone")
shop.sell_tire("Bridgestone")
shop.sell_tire("Bridgestone")

print("\nHistorico total de vtas.")
shop.get_history_vtas()


