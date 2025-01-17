import numpy as np
import pddlgym
import random
import time

'''
INICIALIZACIÓN DE PARÁMETROS
'''

# Crear entorno de PDDLGym a partir de nuestro dominio
env = pddlgym.make ("PDDLEnvAirport-v0")

# Fijar el problema del entorno
env.fix_problem_index(0)

# Iniciar el entorno con el agente para que esté en el lugar inicial
state, debug_info = env.reset()

# Definición de la Q-table

# RELLENAR: DEFINICIÓN DE Q-TABLE #

env.action_space.all_ground_literals(state)
all_actions = list(env.action_space._all_ground_literals)

Q_table = {}

def ensure_state_in_qtable(state):
    if state not in Q_table:
        Q_table[state] = [0.0 for _ in all_actions]

'''
DEFINICIÓN DE HIPERPARÁMETROS DEL Q-LEARNING
'''

total_episodes = 50
learning_rate = 0.2 # Alpha in Q-learning algorithm
max_steps = 2000
gamma = 0.99 # Discount factor

####################################################################
# #
# RELLENAR: PARÁMETROS DE EXPLORACIÓN #
# #
####################################################################

# Ejemplo
#epsilon = 0.01

epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995

def update_epsilon(epsilon):
    return max(epsilon_min, epsilon * epsilon_decay)

'''
ALGORITMO Q-LEARNING
'''

# Actualización de la Q-table
def update_q_table(state, action, reward, new_state, terminated, truncated):
    # Índice de la acción en la lista de todas las acciones posibles
    action_index = all_actions.index(action)
    
    # Máximo valor Q para el nuevo estado (s') si no es terminal
    if not (terminated or truncated):
        max_future_q = max(Q_table[new_state])
    else:
        max_future_q = 0

    # Actualizar el valor Q(s, a)
    Q_table[state][action_index] = Q_table[state][action_index] + learning_rate * (
        reward + gamma * max_future_q - Q_table[state][action_index]
    )

# Entrenamos hasta un número máximo de episodios (reinicios)
for episode in range(total_episodes):
    start_time = time.time()

    state, debug = env.reset()
    ensure_state_in_qtable(state)
    # El agente irá tomando decisiones hasta un número máximo de pasos
    for step in range(max_steps):
        '''
            EXPLORACIÓN-EXPLOTACIÓN
        '''
        # Ejemplo
        if random.uniform(0,1) > epsilon:
            # EXPLOTACIÓN: escoger la mejor acción conocida
            action_index = np.argmax(Q_table[state])
            action = all_actions[action_index]
        else:
            # EXPLORACIÓN SEGÚN ALGORITMO
            action = env.action_space.sample(state)

        new_state, reward, terminated, truncated, info = env.step(action)
        ensure_state_in_qtable(new_state)

        # RELLENAR: ACTUALIZAR TABLA #
        update_q_table(state, action, reward, new_state, terminated, truncated)

        state = new_state
        if terminated or truncated:
            break
    
    end_time = time.time()
    episode_time = end_time - start_time
    print(f"Episode {episode + 1} completed. Time: {episode_time:.2f} seconds. Epsilon: {epsilon}")
    #Actualizar epsilon
    epsilon = update_epsilon(epsilon)

'''
APLICACIÓN DE LA Q-TABLE PARA SACAR UN PLAN CON LA POLÍTICA
'''

state, debug = env.reset()
ensure_state_in_qtable(state)

total_reward = 0
steps_taken = 0
success = False

while True:
    # Valor numérico del estado para sacar la fila de la tabla
    #index = vistos.index(state)
    
    # RELLENAR: PLANIFICAR #
    
    action_index = np.argmax(Q_table[state])
    action = all_actions[action_index]

    print(f"Action chosen for state {state}: {action}")

    state, reward, terminated, truncated, info = env.step(action)

    total_reward += reward
    steps_taken += 1

    ensure_state_in_qtable(action)

    # Terminar cuando el agente alcanza el objetivo
    if terminated:
        success = terminated
        print("Goal reached")
        break
    elif truncated:
        success = terminated
        print('Episode ended (truncated)')
        break

print(f"Plan took {steps_taken} steps")
print(f"Total reward: {total_reward:.2f}")

if success:
    print("The agent reached the goal")
else:
    print("The agent did not reach the goal")