import sys
import random        

# Integrantes: Juan Romero y Andres Torrijos


class SimpleProblemSolvingAgentProgram:

    def __init__(self, initial_state=None):

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
                seq = ["Suck, Right, Suck"]
            elif problem == state2:
                seq = ["Suck, Left, Suck"]
            elif problem == state3:
                seq = ["Right, Suck"]
            elif problem == state4:
                seq = ["Suck"]
            elif problem == state5:
                seq = ["Suck"]
            elif problem == state6:
                seq = ["Left, Suck"]
            return seq
        
state1 = [(0, 0), [(0, 0), "Dirty"], [(1, 0), ["Dirty"]]]
state2 = [(1, 0), [(0, 0), "Dirty"], [(1, 0), ["Dirty"]]]
state3 = [(0, 0), [(0, 0), "Clean"], [(1, 0), ["Dirty"]]]
state4 = [(1, 0), [(0, 0), "Clean"], [(1, 0), ["Dirty"]]]
state5 = [(0, 0), [(0, 0), "Dirty"], [(1, 0), ["Clean"]]]
state6 = [(1, 0), [(0, 0), "Dirty"], [(1, 0), ["Clean"]]] # (0,0) es la habitación numero 1 y (1,0) es la hbaitación numero 2
state7 = [(0, 0), [(0, 0), "Clean"], [(1, 0), ["Clean"]]]
state8 = [(1, 0), [(0, 0), "Clean"], [(1, 0), ["Clean"]]]

listaDeEstado = [state1,state2,state3,state4,state5,state6]

a = vacuumAgent(state1)
b = random.choice(listaDeEstado)

print("El robot está en la habitación: " , b[0])
print("La primera habitación está: " , b[1][1] , " y la segunda habitación está: " , b[2][1][0])
print("La solución es: " ,a(b))
print ( "Habitaciones limpias!")

