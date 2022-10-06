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
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    # stats.dump_stats('/stats')
    stats.print_stats()
