#!/usr/bin/env python3
import argparse
import subprocess
import os

def run_imgrszr(input_path, size):
    output_dir = f"{size}x{size}"
    os.makedirs(output_dir, exist_ok=True)
    
    cmd = [
        "imgrszr",
        "--max-width", str(size),
        "--max-height", str(size),
        input_path,
        "--output", output_dir
    ]
    
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def create_favicons(sizes):
    favicon_dir = "favicon"
    os.makedirs(favicon_dir, exist_ok=True)
    
    # Use the smallest size folder as reference for filenames
    reference_folder = f"{sizes[0]}x{sizes[0]}"
    if not os.path.isdir(reference_folder):
        print(f"Reference folder {reference_folder} does not exist.")
        return
    
    for filename in os.listdir(reference_folder):
        if filename.lower().endswith(".png"):
            input_files = []
            missing = False
            for size in sizes:
                file_path = os.path.join(f"{size}x{size}", filename)
                if os.path.exists(file_path):
                    input_files.append(file_path)
                else:
                    print(f"Warning: {file_path} does not exist.")
                    missing = True
            if missing:
                print(f"Skipping {filename} due to missing sizes.")
                continue
            
            output_file = os.path.join(favicon_dir, filename.rsplit('.', 1)[0] + ".ico")
            cmd = ["magick"] + input_files + [output_file]
            print(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(
        description="Generate multi-resolution favicons from a single image."
    )
    parser.add_argument("input_path", help="Path to the full-size image or directory")
    parser.add_argument(
        "--sizes",
        nargs="+",
        type=int,
        default=[15, 32, 48, 64, 180],
        help="List of sizes to generate (default: 15 32 48 64 180)"
    )
    
    args = parser.parse_args()
    
    # Process each size with imgrszr
    for size in args.sizes:
        run_imgrszr(args.input_path, size)
    
    # Create individual favicon.ico files for each image found in the smallest size folder
    create_favicons(args.sizes)
    
if __name__ == "__main__":
    main()
