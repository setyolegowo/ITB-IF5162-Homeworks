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
  $ python handler.py root_binary "sqrt(x, 2) - 3" -4 1
  Result is found: -1.73205161095
  ```

- Example finding root using binary method with performance evaluation.
  ```
  $ python handler.py root_binary "sqrt(x, 2) - 3" -4 1
  Result is found: -1.73205161095

  Performance:
      Total loop: 22

  ```