# Agent Evaluation Lab Architecture

Agent Evaluation Lab is a testing platform for autonomous agents.

## Core Components

### Agent Interface
Defines how an agent receives state and returns actions.

### Scenario
Defines the task goal and initial conditions.

### Environment
Applies agent actions and updates the sandbox state.

### Tool Registry
Provides simulated tools that agents can call.

### Sandbox Runtime
Runs the interaction loop between agent and environment.

### Evaluator
Scores the outcome of the run.

## Execution Flow

1. Load an environment
2. Initialize the sandbox
3. Let the agent observe state
4. Agent chooses an action
5. Environment applies the action
6. Sandbox records the action history
7. Evaluator scores the run
