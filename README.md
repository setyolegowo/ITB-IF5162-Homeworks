# ITB-IF5162-Homeworks

This repository is used for save programming howeworks for course IF5162 - Numerical Methods in second semester 2019.

## How to use

Execute through handler file.
```bash
python handler.py
```

- Show help.
  ```bash
  python handler.py -h
  ```

- Example finding root using binary method.
  ```
  $ python handler.py root_binary "pow(x, 2) - 3" -4 1
  Result is found: -1.73205161095
  ```

- Example finding root using binary method with performance evaluation.
  ```
  $ python handler.py -p root_binary "pow(x, 2) - 3" -4 1
  Result is found: -1.73205161095

  Performance:
      Total loop: 22

  ```

- Example finding root using regula-falsi method.
  ```
  $ python handler.py root_regula "pow(x, 2) - 3" -4 1
  Result is found: -1.73205007751
  ```

- Example finding root using regula-falsi method with performance evaluation.
  ```
  $ python handler.py -p root_regula "pow(x, 2) - 3" -4 1
  Result is found: -1.73205007751

  Performance:
      Total loop: 18

  ```

- Example finding root using fixed point iteration method.
  ```
  $ python handler.py root_fixed_point "pow(x, 3) - 3" "sqrt(3/x)" 1.0001
  Result is found: 1.44224944442
  ```

- Example finding root using fixed point iteration method with performance evaluation.
  ```
  $ python handler.py -p root_fixed_point "pow(x, 3) - 3" "sqrt(3/x)" 1.0001
  Result is found: 1.44224944442

  Performance:
      Total loop: 22

  ```

- Example finding root using newton-raphson method.
  ```
  $ python handler.py root_newton_rhapson "pow(x, 3) - 3" "3*pow(x,2)" 1.0001
  Result is found: 1.44224957031
  ```

- Example finding root using newton-raphson method with performance evaluation.
  ```
  $ python handler.py -p root_newton_rhapson "pow(x, 3) - 3" "3*pow(x,2)" 1.0001
  Result is found: 1.44224957031

  Performance:
      Total loop: 5

  ```

- Example finding root using newton-raphson method.
  ```
  $ python handler.py root_secant "pow(x, 3) - 3" 1.0001 2
  Result is found: 1.44224957044
  ```

- Example finding root using newton-raphson method with performance evaluation.
  ```
  $ python handler.py -p root_secant "pow(x, 3) - 3" 1.0001 2
  Result is found: 1.44224957044

  Performance:
      Total loop: 6

  ```
