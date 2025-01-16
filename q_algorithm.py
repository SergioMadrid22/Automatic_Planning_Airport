import numpy as np
import pddlgym
import random

'''
INICIALIZACIÓN DE PARÁMETROS
'''

# Crear entorno de PDDLGym a partir de nuestro dominio
env = pddlgym.make ("PDDLEnv<Domain>-v0")

# Fijar el problema del entorno
env.fix_problem_index(0)

# Iniciar el entorno con el agente para que esté en el lugar inicial
state, debug_info = env.reset()

# Definición de la Q-table

####################################################################
# #
# RELLENAR: DEFINICIÓN DE Q-TABLE #
# #
####################################################################

'''
DEFINICIÓN DE HIPERPARÁMETROS DEL Q-LEARNING
'''

total_episodes = 1000
learning_rate = 0.2 # Alpha in Q-learning algorithm
max_steps = 2000

gamma = 0.99 # Discount factor

####################################################################
# #
# RELLENAR: PARÁMETROS DE EXPLORACIÓN #
# #
####################################################################

# Ejemplo
epsilon = 0.01


'''
ALGORITMO Q-LEARNING
'''
# Entrenamos hasta un número máximo de episodios (reinicios)
for episode in range(total_episodes):
    state, debug = env.reset()
    # El agente irá tomando decisiones hasta un número máximo de pasos
    for step in range(max_steps):
        '''
            EXPLORACIÓN-EXPLOTACIÓN
        '''
        # Ejemplo
        if random.uniform(0,1) > epsilon:
            # EXPLOTACION
            pass
        else:
            # EXPLORACI´ON SEG´UN ALGORITMO
            action = env.action_space.sample(state)

        new_state, reward, done, info = env.step(action)

        ####################################################################
        # #
        # RELLENAR: ACTUALIZAR TABLA #
        # #
        ####################################################################

        state = new_state
        if done:
            break

'''
APLICACIÓN DE LA Q-TABLE PARA SACAR UN PLAN CON LA POLÍTICA
'''

state, debug = env.reset()
while True:
    # Valor numérico del estado para sacar la fila de la tabla
    index = vistos.index(state)

    ####################################################################
    # #
    # RELLENAR: PLANIFICAR #
    # #
    ####################################################################

    accion_a_aplicar = None
    state, reward, done, info = env.step(accion_a_aplicar)
    # Acabo cuando llego al objetivo
    if done:
        break








