#!/usr/bin/env python3
import argparse
import subprocess
import os

def run_imgrszr(input_path, size):
    output_dir = f"{size}x{size}"
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Build the imgrszr command
    cmd = [
        "imgrszr",
        "--max-width", str(size),
        "--max-height", str(size),
        input_path,
        "--output", output_dir
    ]
    
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def create_favicon(sizes):
    favicon_dir = "favicon"
    os.makedirs(favicon_dir, exist_ok=True)
    
    # Build the list of png files from each folder
    png_paths = []
    for size in sizes:
        folder = f"{size}x{size}"
        # Using a glob pattern to match all png files in the folder
        png_paths.append(f"{folder}/*.png")
    
    # Build the convert command
    # This will combine all pngs into one multi-resolution favicon.ico file.
    cmd = ["convert"] + png_paths + [os.path.join(favicon_dir, "favicon.ico")]
    
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(
        description="Generate resized images and combine them into a multi-resolution favicon."
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
    
    # Combine all generated PNGs into one favicon.ico
    create_favicon(args.sizes)
    
if __name__ == "__main__":
    main()
