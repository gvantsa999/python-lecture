import sys

def main():
    coordinates_list = [42.376, -71.115]
    coordinates_tuple = (42.376, -71.115)

    print(f"List size: {sys.getsizeof(coordinates_list)} bytes")
    print(f"Tuple size: {sys.getsizeof(coordinates_tuple)} bytes")

main()