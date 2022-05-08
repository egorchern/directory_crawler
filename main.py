import argparse
import os
def convert_bytes_to_mb(bytes: int):
    return round(bytes / 1000000, 4)

def crawl(root_path, depth = 0):
    try:
        
        paths = os.listdir(root_path)
        path_stats = {}
        for path in paths:
            joined = os.sep.join([root_path, path])
            is_directory = os.path.isdir(joined)

            if is_directory:
                size = crawl(joined, depth + 1)
                path_stats[path] = size

            else:
                file_stats = os.stat(joined)
                file_size = convert_bytes_to_mb(file_stats.st_size)
                path_stats[path] = file_size

        directory_size = 0

        for path in path_stats:
            directory_size += path_stats[path]
        
        print(f"{''.join(['-' for x in range(depth*2)])} {root_path}, {directory_size}mb: ")
        
        for path in dict(sorted (path_stats.items(), key=lambda x: x[1], reverse=True)): 
            size = path_stats[path]
            print(f"{''.join(['-' for x in range(depth*2+1)])} {path}, {size}mb : {round((size / directory_size) * 100, 4)}%")
        
        return directory_size

    except:
        print("error")
        

def main():
    parser = argparse.ArgumentParser(description='Crawl a directory')
    parser.add_argument("path", type=str, help="Path to a directory to crawl")
    parsed = parser.parse_args()
    path = parsed.path
    crawl(path)

if __name__ == "__main__":
    main()