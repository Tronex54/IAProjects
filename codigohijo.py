import sys

class Nodo():
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion

class Frontera():
    def __init__(self):
        self.frontera =[]
    
    def empty(self):
        return (len(self.frontera) == 0)

    def add(self, nodo):
        self.frontera.append(nodo)
    
    def eliminar(self):
        # LIFO o FIFO
        pass

    def contiene_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)
    
    

class Pila(Frontera):
    def eliminar(self):
        # Termina la busqueda si la frontera esta vacia
        if self.empty():        
            raise Exception("Frontera vacia")
        else:
            # Guardamos el ultimo item en la lista 
            # (el cual es el nodo recientemente añadido)
            nodo = self.frontera[-1]
            # Guardamos todos los items excepto el 
            # ultimo (eliminamos)
            self.frontera = self.frontera[:-1]
            return nodo
    
class Cola(Frontera):
    def eliminar(self):
        # Termina la busqueda si la frontera esta vacia
        if self.empty():        
            raise Exception("Frontera vacia")
        else:
            # Guardamos el primer item en la lista 
            # (el cual es el nodo añadido de primero)
            nodo = self.frontera[0]
            # Guardamos todos los items excepto el 
            # primero (eliminamos)
            self.frontera = self.frontera[1:]
            return nodo
        
class SimpleProblemSolvingAgentProgram:

    """Marco abstracto para un agente de resolución de problemas. [Figure 3.1]"""

    def __init__(self, initial_state=None):
        """El estado es una representación abstracta del estado.
         del mundo, y seq es la lista de acciones requeridas
         para llegar a un estado particular desde el estado inicial (raíz)."""
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formule una meta y un problema, luego
         buscar una secuencia de acciones para resolverlo."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state, percept):
        raise NotImplementedError

    def formulate_goal(self, state):
        raise NotImplementedError

    def formulate_problem(self, state, goal):
        raise NotImplementedError

    def search(self, problem):
        raise NotImplementedError
    
class vacuumAgent(SimpleProblemSolvingAgentProgram):
        def update_state(self, state, percept):
            return percept

        def formulate_goal(self, state):
            goal = [state7, state8]
            return goal  

        def formulate_problem(self, state, goal):
            problem = state
            return problem   
    
        def search(self, problem):
            if problem == state1:
                seq = ["Suck", "Right", "Suck"]
            elif problem == state2:
                seq = ["Suck", "Left", "Suck"]
            elif problem == state3:
                seq = ["Right", "Suck"]
            elif problem == state4:
                seq = ["Suck"]
            elif problem == state5:
                seq = ["Suck"]
            elif problem == state6:
                seq = ["Left", "Suck"]
            return seq
        
state1 = [(0, 0), [(0, 0), "Dirty"], [(1, 0), ["Dirty"]]]
state2 = [(1, 0), [(0, 0), "Dirty"], [(1, 0), ["Dirty"]]]
state3 = [(0, 0), [(0, 0), "Clean"], [(1, 0), ["Dirty"]]]
state4 = [(1, 0), [(0, 0), "Clean"], [(1, 0), ["Dirty"]]]
state5 = [(0, 0), [(0, 0), "Dirty"], [(1, 0), ["Clean"]]]
state6 = [(1, 0), [(0, 0), "Dirty"], [(1, 0), ["Clean"]]]
state7 = [(0, 0), [(0, 0), "Clean"], [(1, 0), ["Clean"]]]
state8 = [(1, 0), [(0, 0), "Clean"], [(1, 0), ["Clean"]]]

a = vacuumAgent(state1)

#print(a(state2)) 
#print(a(state5))
print(a(state5))