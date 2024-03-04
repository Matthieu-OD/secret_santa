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
git clone https://github.com/Matthieu-OD/secret_santa.git
cd secret-santa-solver
```

## Usage
To run the Secret Santa Solver, execute the following command in the terminal:

```sh
python secret_santa_solver.py
```

This will use the examples that were given in the assignment.

You can add params following this example:
```sh
python secret-santa-solver.py --people "Alice,Bob,Charlie,Dana,Eve,Frank,George,Hannah" --couples "Alice,Bob;Charlie,Dana;Eve,Frank;George,Hannah"
```

Or if you prefer you cand directly modify the variables `PEOPLE` and `COUPLES` in the `secret-santa-solver.py` file. More information in the next section.

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
