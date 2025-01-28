#!/bin/bash

# Default values for parameters
DEFAULT_EPISODES=300
DEFAULT_MAX_STEPS=2000
DEFAULT_LR=0.2
DEFAULT_GAMMA=0.99
DEFAULT_EPSILON=1.0
DEFAULT_EPSILON_DECAY=0.99

# Seeds to use for each experiment
SEEDS=(42 123 456 789)

# Arrays of parameter values to test
learning_rates=(0.1 0.2 0.5)
gammas=(0.9 0.95 0.99)
epsilons=(0.8 0.9 1.0)
epsilon_decays=(0.995 0.99 0.9)

# Directory for saving results
RESULTS_DIR="results"
mkdir -p "$RESULTS_DIR"

# Function to run an experiment
run_experiment() {
    local param_name=$1
    local param_value=$2
    local file_name=$3

    # Create a subdirectory for each parameter
    mkdir -p "${RESULTS_DIR}/results_${param_name}"

    # Loop over each seed for the experiment
    for SEED in "${SEEDS[@]}"; do
        echo "Running experiment: $param_name=$param_value, seed=$SEED"
        python3 q_algorithm.py \
            --episodes $DEFAULT_EPISODES \
            --max_steps $DEFAULT_MAX_STEPS \
            --lr $DEFAULT_LR \
            --gamma $DEFAULT_GAMMA \
            --epsilon $DEFAULT_EPSILON \
            --epsilon_decay $DEFAULT_EPSILON_DECAY \
            --"$param_name" $param_value \
            --seed $SEED \
            > "${RESULTS_DIR}/results_${param_name}/${SEED}_${file_name}" &
    done
}

# Run all experiments in parallel
echo "Starting parallel experiments..."

# Learning rates
for lr in "${learning_rates[@]}"; do
    run_experiment "lr" "$lr" "results_lr_${lr}.txt"
done

# Gamma values
for gamma in "${gammas[@]}"; do
    run_experiment "gamma" "$gamma" "results_gamma_${gamma}.txt"
done

# Epsilon values
for epsilon in "${epsilons[@]}"; do
    run_experiment "epsilon" "$epsilon" "results_epsilon_${epsilon}.txt"
done

# Epsilon decay values
for epsilon_decay in "${epsilon_decays[@]}"; do
    run_experiment "epsilon_decay" "$epsilon_decay" "results_epsilon_decay_${epsilon_decay}.txt"
done

# Wait for all processes to finish
wait

echo "All experiments completed in parallel. Results saved in the '$RESULTS_DIR' directory."
