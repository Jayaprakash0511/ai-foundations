import os 
import sys

def squares_list(n):
    return [x*x for x in range(n)]

def squares_gen(n):
    for x in range(n):
        yield x*x 

def demo_memory():
    n = 1000000
    as_list = squares_list(n)
    as_gen = squares_gen(n)

    print(f"list of {n} squares: {sys.getsizeof(as_list):>12,} bytes")
    print(f"generator object of {n} sqaures: {sys.getsizeof(as_gen):>12,} bytes")
    print(f" sum(squares_list(n)): {sum(squares_list(n))}")
    print(f" sum(squares_gen(n)): {sum(squares_gen(n))}")

def demo_file_streaming():
    print("=== 2. Streaming a file one line at a time ===")
    path = "demo_log.txt"
    with open(path, "w") as f:
        for i in range(10):
            level = "ERROR" if i % 3 == 0 else "INFO"
            f.write(f"{level}: event {i}\n")

    def read_errors(p):
        with open(p) as f:
            for line in f:              
                if "ERROR" in line:
                    yield line.strip()

    for err in read_errors(path):       
        print("  found:", err)

    os.remove(path)                     
    print()

def demo_pipeline():
    print("=== 3. A lazy pipeline of generators ===")

    def numbers():
        for n in range(1, 11):
            yield n

    def evens(src):
        for n in src:
            if n % 2 == 0:
                yield n

    def doubled(src):
        for n in src:
            yield n * 2

    pipeline = doubled(evens(numbers()))   
    print("  result:", list(pipeline))     
    print()

def main():
    demo_memory()
    demo_file_streaming()
    demo_pipeline()


if __name__ == "__main__":
    main()


