# Nation Simulator

## Project Overview
This project is a **simple socio-economic simulator** for a fictional country called *Quera*. The main goal is to implement the principles of **object-oriented programming (OOP)** in Python by modeling people, professions, and workplaces in a basic economic system.

## Learning Objectives
- Practice designing base and derived classes using inheritance
- Use attributes and methods to define object behavior
- Organize logic and data through object-oriented design
- Implement relationships between objects (e.g., employment)

---

## System Components

### 👤 People (Persons)
Each person in the simulation has:
- `name`
- `age`
- `level`
- a profession (Engineer, Teacher, or Worker)

People have daily living expenses and can earn income if employed. Over time, they may level up based on certain conditions.

### 🏢 Workplaces
Each workplace has:
- `name`
- `years_active`
- `level`
- `capacity` for hiring people

There are different types of workplaces:
- `Mine`
- `School`
- `Company`

Each workplace type has specific maintenance costs and affects the income of the employees differently.

---

## Class Structure

### Base Classes
- `Person`: base class for individuals
- `WorkPlace`: base class for workplaces

### Derived from `Person`
- `Engineer`
- `Teacher`
- `Worker`

### Derived from `WorkPlace`
- `Mine`
- `School`
- `Company`

---

## Key Behaviors

### For People:
- Calculate **daily income** based on level, profession, and workplace
- Calculate **daily living expenses**
- Level up based on experience or specific logic

### For Workplaces:
- Hire people (if capacity allows)
- Calculate **maintenance costs**
- Level up over time or based on performance

### System-Wide:
- Compute total income and expenses across all people
- Compute total income and maintenance costs for all workplaces

---

## Getting Started

1. Make sure you have Python 3.8 or higher installed.
2. Run the main script to test the simulator:

```bash
python main.py