# sp6lab
- FlameGraph
  ```
  git clone https://github.com/brendangregg/FlameGraph
  ```
- Perf.data
  ```
  sudo perf record ./my_main
  or
  sudo perf record -g -F 99 -a -g -- sleep 60
  ```
