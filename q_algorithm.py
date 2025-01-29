import numpy as np
import pddlgym
import random
import time
import argparse
import matplotlib.pyplot as plt

'''
INICIALIZACIÓN DE PARÁMETROS
'''
def parse_arguments():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Q-learning algorithm for airport problem')
    
    parser.add_argument('--episodes', type=int, default=500,
                        help='Number of episodes to run')
    parser.add_argument('--max_steps', type=int, default=2000,
                        help='Max steps for episode')
    parser.add_argument('--lr', type=float, default=0.2,
                        help='Learning rate or alpha for Q-learning')
    parser.add_argument('--gamma', type=float, default=0.99,
                        help='Discount factor for Q-learning')
    parser.add_argument('--seed', type=int, default=None,
                        help='Seed for random number generation')
    parser.add_argument('--epsilon', type=float, default=1.0,
                        help='Initial value of epsilon')
    parser.add_argument('--epsilon_decay', type=float, default=0.99,
                        help='Decay rate of epsilon after each episode')
    
    args = parser.parse_args()

    if args.episodes <= 0:
        raise ValueError("Number of episodes must be greater than 0")
    if not (0 < args.lr <= 1):
        raise ValueError("Learning rate must be between 0 and 1")
    if not (0 < args.gamma <= 1):
        raise ValueError("Discount factor must be between 0 and 1")
    if args.seed is not None and args.seed < 0:
        raise ValueError("Seed must be a non-negative integer")
    
    if args.seed:
        random.seed(args.seed)
    return args

args = parse_arguments()
dict_args = vars(args)

# Crear entorno de PDDLGym a partir de nuestro dominio
env = pddlgym.make("PDDLEnvAirport_adapted-v0")

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
        Q_table[state] = {}
    valid_actions = env.action_space.all_ground_literals(state)
    for a in valid_actions:
        if a not in Q_table[state]:
            Q_table[state][a] = 0.0

'''
DEFINICIÓN DE HIPERPARÁMETROS DEL Q-LEARNING
'''

total_episodes = args.episodes
learning_rate = args.lr # Alpha in Q-learning algorithm
max_steps = args.max_steps
gamma = args.gamma # Discount factor

####################################################################
# #
# RELLENAR: PARÁMETROS DE EXPLORACIÓN #
# #
####################################################################

epsilon = args.epsilon
epsilon_min = 0.01
epsilon_decay = args.epsilon_decay

def update_epsilon(epsilon):
    return max(epsilon_min, epsilon * epsilon_decay)

'''
ALGORITMO Q-LEARNING
'''

# Actualización de la Q-table
def update_q_table(state, action, reward, new_state, terminated, truncated):
    
    old_q = Q_table[state][action]

    if terminated or truncated:
        max_future_q = 0.0
    else:
        ensure_state_in_qtable(new_state)
        max_future_q = max(Q_table[new_state].values()) if Q_table[new_state] else 0.0

    new_q = old_q + learning_rate * (reward + gamma * max_future_q - old_q)
    Q_table[state][action] = new_q


print(f"Running Q-learning algorithm with parameters: {dict_args}")
# Entrenamos hasta un número máximo de episodios (reinicios)
for episode in range(total_episodes):
    start_time = time.time()

    state, debug = env.reset()
    ensure_state_in_qtable(state)
    # El agente irá tomando decisiones hasta un número máximo de pasos
    episode_steps = 0
    for step in range(max_steps):
        valid_actions = list(env.action_space.all_ground_literals(state))
        if not valid_actions:
            break
        """
            EXPLORACION-EXPLOTACION 
        """
        if random.uniform(0, 1) > epsilon:
            # Explotacion
            action = max(valid_actions, key=lambda a: Q_table[state][a])
        else:
            # Exploracion
            action = random.choice(valid_actions)

        new_state, reward, terminated, truncated, info = env.step(action)

        ensure_state_in_qtable(new_state)

        update_q_table(state, action, reward, new_state, terminated, truncated)

        state = new_state
        episode_steps += 1
        if terminated or truncated:
            break
    
    end_time = time.time()
    episode_time = end_time - start_time
    print(f"Episode {episode + 1} completed. Time: {episode_time:.2f} seconds. Epsilon: {epsilon}. Steps: {episode_steps}")
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

for _ in range(max_steps):
    valid_actions = list(env.action_space.all_ground_literals(state))
    if not valid_actions:
        print("No valid actions available, plan failed.")
        break

    # Choose the best action among the valid ones
    action = max(valid_actions, key=lambda a: Q_table[state][a])
    print(f"Action chosen for state {state}: {action}")

    new_state, reward, terminated, truncated, info = env.step(action)

    steps_taken += 1

    ensure_state_in_qtable(new_state)
    state = new_state

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
print(f"Number of rows in Q table: {len(Q_table)}")
if success:
    print("The agent reached the goal")
else:
    print("The agent did not reach the goal")
