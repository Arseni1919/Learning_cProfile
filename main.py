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
    # with open('stats', 'w') as stats_folder:
    stats.strip_dirs()
    stats.dump_stats('stats/results.pstat')
    stats.print_stats()


# # Code to test visualization
# import random
# # Simple function to print messages
# def print_msg():
#     for i in range(10):
#         print("Program completed")
#
# # Generate random data
# def generate():
#     data = [random.randint(0, 99) for p in range(0, 1000)]
#     return data
#
# # Function to search
# def search_function(data):
#     for i in data:
#         if i in [100,200,300,400,500]:
#             print("success")
#
# def main():
#     data=generate()
#     search_function(data)
#     print_msg()
#
# if __name__ == '__main__':
#     main()
