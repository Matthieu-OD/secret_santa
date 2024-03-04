# Secret Santa Solver

## Project Overview

This project presents my simple answer to the Secret Santa problem. The goal was to find a solution that has both quite good time and space complexity while staying simple.

It takes into account the following rules
- Each participant gifts exactly one other person.
- No participant gifts themselves or their significant other.
- The solution avoids direct reciprocity; if A gifts B, B does not gift A.

With the given condition we were able to fix the biggest draw back of the algorithm by swapping the two first person if the first and last person are a couple.

## Features
- **Flexibility**: Handles groups of varying sizes and compositions.
- **Constraint Respect**: Adheres strictly to the no-self-gifting and no-couple-gifting rules.

## Getting Started

### Prerequisites
- The project was build with python 3.12 but you can use whatever version of python as long as it supports typing.

### Installation
No additional installation is required just python, as the script uses standard Python libraries.

### Setup
Clone this repository to your local machine:

```
git clone https://yourrepositoryurl.com/secret-santa-solver.git
cd secret-santa-solver
```

## Usage
To run the Secret Santa Solver, execute the following command in the terminal:

```
python secret_santa_solver.py
```

Ensure you have defined the list of participants and couples within the script as per your group's specifics.

## Configuration
- **Participants**: Update the `PEOPLE` list with the names of all participants.
- **Couples**: Update the `COUPLES` list with tuples representing each couple in the group.

Example:
```python
PEOPLE =  ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
```

## Notes

On a larger project I would set up pre-commit with github actions to ensure good code quality.

## Testing
To test the solution with different group configurations, modify the `PEOPLE` and `COUPLES` lists as needed and rerun the script. The script's output will display the Secret Santa assignments or an error message if a valid configuration cannot be found.
