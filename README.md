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

- Example find linear interpolation function
  ```
  $ python handler.py interpolation_linear 0,0,1.0 1.0,3.0
  Generated function: y = 1.0 + 2.0*x
  ```

- Example find result of linear interpolation function
  ```
  $ python handler.py interpolation_linear_calc 4.0 0,0,1.0 1.0,3.0
  Generated function: y = 1.0 + 2.0*x
  Result is found: 9.0
  ```

- Example find lagrange interpolation function
  ```
  $ python handler.py interpolation_lagrange 0.0,1.0 0.4,0.921061 0.8,0.696707 1.2,0.362358
  Generated function: y = (-2.60416666667*(x - 0.4)*(x - 0.8)*(x - 1.2)) + (7.1957890625*(x - 0.0)*(x - 0.8)*(x - 1.2)) + (-5.4430234375*(x - 0.0)*(x - 0.4)*(x - 1.2)) + (0.943640625*(x - 0.0)*(x - 0.4)*(x - 0.8))
  ```

- Example find result of lagrange interpolation function
  ```
  $ python handler.py interpolation_lagrange_calc 0.5 0.0,1.0 0.4,0.921061 0.8,0.696707 1.2,0.362358
  Generated function: y = (-2.60416666667*(x - 0.4)*(x - 0.8)*(x - 1.2)) + (7.1957890625*(x - 0.0)*(x - 0.8)*(x - 1.2)) + (-5.4430234375*(x - 0.0)*(x - 0.4)*(x - 1.2)) + (0.943640625*(x - 0.0)*(x - 0.4)*(x - 0.8))
  Result is found: 0.8772215625
  ```

- Example find newton interpolation function
  ```
  $ python handler.py interpolation_newton 8.0,2.079442 9.0,2.197225 9.5,2.251292 11.0,2.397895
  Generated function: y = (2.079442) + (0.117783*(x - 8.0)) + (-0.00643266666667*(x - 8.0)*(x - 9.0)) + (0.000411111111111*(x - 8.0)*(x - 9.0)*(x - 9.5))
  ```

- Example find result of newton interpolation function
  ```
  $ python handler.py interpolation_newton 8.0,2.079442 9.0,2.197225 9.5,2.251292 11.0,2.397895
  Generated function: y = (2.079442) + (0.117783*(x - 8.0)) + (-0.00643266666667*(x - 8.0)*(x - 9.0)) + (0.000411111111111*(x - 8.0)*(x - 9.0)*(x - 9.5))
  Result is found: 2.21920816
  ```

- Example find result of integral with square strip
  ```
  $ python handler.py integral_square_strip "x**2 + x" 0 2.0 1000
  Result is found: 4.654687992
  ```

- Example find result of integral with trapezium strip
  ```
  $ python handler.py integral_trapezium_strip "x**2 + x" 0 2.0 1000
  Result is found: 4.654687992
  ```

- Example find result of integral with midpoint strip
  ```
  $ python handler.py integral_midpoint_strip "x**2 + x" 0 2.0 1000
  Result is found: 4.654675998
  ```

- Example find result of integral with simpson 1/3
  ```
  $ python handler.py integral_simpson_1_3 "x**2 + x" 0 2.0 1000
  Result is found: 4.642719968
  ```

- Example find result of integral with simpson 3/8
  ```
  $ python handler.py integral_simpson_3_8 "x**2 + x" 0 2.0 1000
  Result is found: 4.654684161
  ```
