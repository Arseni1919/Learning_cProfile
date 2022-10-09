# Learning cProfile

Let’s say you have an algorithm that takes a lot of time to run. 
And you want to reduce the code run time. The first question that might crop up is:

Why does my code take so long to run?

Python Profilers can answer that question. 
It tells you which part of the code took how long to run. 
This lets you focus on that particular part and achieve efficiency. 

## Simple Usage

```python
import cProfile
cProfile.run("20+10")
```

# Function Inside Function Example

```python
def create_array():
    arr = []
    for i in range(0, 400000):
        arr.append(i)


def print_statement():
    print('Array created successfully')


def main():
    create_array()
    print_statement()


if __name__ == '__main__':
    cProfile.run('main()')
```

## Using classes of cProfile and Stats

```python
import cProfile
import pstats

def create_array():
    arr = []
    for i in range(0, 400000):
        arr.append(i)

def print_statement():
    print('Array created successfully')

def main():
    create_array()
    print_statement()

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    # stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()
```

## To Export Data

```python
stats = pstats.Stats(profiler).sort_stats('cumtime')
stats.dump_stats('stats/results.pstat')
```

## To remove dir prefixes from the output

```python
stats.strip_dirs()
```

## To visualize

```shell
snakeviz stats/results.pstat
```

## Credits

- [blog | cProfile – How to profile your python code](https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/)
