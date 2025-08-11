# Automatic Planning of Baggage Transport at an Airport

This repository implements **automatic planning for baggage transport at an airport** using **PDDL (Planning Domain Definition Language)** and a **Q-learning algorithm**. The project leverages [PDDLGym](https://github.com/tomsilver/pddlgym) to create a custom environment for reinforcement learning.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Usage](#usage)
  - [1. Setup Environment](#1-setup-environment)
  - [2. Q-learning Algorithm](#2-q-learning-algorithm)
  - [3. PDDL Models](#3-pddl-models)
- [Reports](#reports)
- [References](#references)
- [License](#license)

---

## Project Overview

The goal of this project is to automate the planning and control of baggage transport vehicles within an airport using AI planning and reinforcement learning. The environment is specified in PDDL, and agents learn optimal policies for baggage delivery using Q-learning.

- **PDDL** is used to describe the planning domain (actions, predicates, objects) and the problem instances (initial state, goals).
- **Q-learning** is used for learning optimal policies in a model-free way.
- **PDDLGym** provides a Gym-like interface for interacting with PDDL domains within Python.

## Features

- Custom PDDL domain for airport baggage transport
- Q-learning algorithm for learning optimal policies
- Integration with [PDDLGym](https://github.com/tomsilver/pddlgym)
- Configurable training parameters: episodes, learning rate, discount factor, epsilon-greedy strategy, etc.
- Step-by-step plan extraction and policy evaluation

## Repository Structure

```
.
├── pddlgym/                   # Custom PDDLGym environment and domain/problem files
│   └── pddl/                  # PDDL domain and problem definitions
├── q_algorithm.py             # Q-learning implementation for the airport domain
├── Report_PDDL.pdf            # Report explaining the PDDL modeling
├── Report_QAlgorithm.pdf      # Report explaining the Q-learning algorithm and results
└── README.md                  # (You are here)
```

## Requirements

- Python 3.7+
- [PDDLGym](https://github.com/tomsilver/pddlgym)
- numpy
- matplotlib
- argparse

Install dependencies:
```bash
pip install numpy matplotlib argparse
pip install git+https://github.com/tomsilver/pddlgym.git
```

## Usage

### 1. Setup Environment

Make sure the `pddlgym` and `pddlgym/pddl` directories contain the appropriate domain and problem files describing the airport and baggage transport scenarios.

### 2. Q-learning Algorithm

The main entry point is `q_algorithm.py`, which contains the Q-learning implementation.

**Example usage:**
```bash
python q_algorithm.py --episodes 500 --lr 0.2 --gamma 0.99 --epsilon 1.0 --epsilon_decay 0.99 --max_steps 2000 --seed 42
```

**Parameters:**

- `--episodes`: Number of training episodes (default: 500)
- `--max_steps`: Maximum steps per episode (default: 2000)
- `--lr`: Learning rate (alpha) for Q-learning (default: 0.2)
- `--gamma`: Discount factor (default: 0.99)
- `--epsilon`: Initial epsilon for exploration (default: 1.0)
- `--epsilon_decay`: Decay rate for epsilon (default: 0.99)
- `--seed`: Random seed (default: None)

The script will train a Q-learning agent and print statistics about training progress and final plan extraction.

### 3. PDDL Models

- **Domain file:** Defines actions, predicates, and types for the airport scenario.
- **Problem file:** Specifies objects, initial state, and goals for a specific scenario.

You can find these files in `pddlgym/pddl/`.

## Reports

- [`Report_PDDL.pdf`](Report_PDDL.pdf): Details about the PDDL domain and problem modeling for the airport baggage transport.
- [`Report_QAlgorithm.pdf`](Report_QAlgorithm.pdf): Explanation of the Q-learning implementation, experiments, and results.

## References

- [PDDLGym: Gym Environments for PDDL Planning Problems](https://github.com/tomsilver/pddlgym)
- [PDDL: Planning Domain Definition Language](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language)
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction*.

## License

This project is for academic purposes. Please refer to individual file headers or contact the author for licensing information.

---

**Author:** SergioMadrid22  
**Repository:** [Automatic_Planning_Airport](https://github.com/SergioMadrid22/Automatic_Planning_Airport)
