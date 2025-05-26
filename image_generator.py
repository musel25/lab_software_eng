import os
import subprocess
import sys

def convert_mmd_to_png(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all .mmd files in the input folder
    mmd_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mmd')]

    if not mmd_files:
        print("No .mmd files found in the input folder")
        return

    # Iterate through each MMD file
    for mmd_file in mmd_files:
        mmd_path = os.path.join(input_folder, mmd_file)
        png_file = os.path.splitext(mmd_file)[0] + '.png'
        png_path = os.path.join(output_folder, png_file)
        
        try:
            # Use mmdc to convert MMD to PNG
            subprocess.run([
                'mmdc',
                '-i', mmd_path,
                '-o', png_path,
                '-b', 'transparent'
            ], check=True)
            print(f"Successfully converted {mmd_file} to {png_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {mmd_file}: {e}", file=sys.stderr)
        except FileNotFoundError:
            print("Error: mmdc command not found. Please install mermaid-cli first:", file=sys.stderr)
            print("npm install -g @mermaid-js/mermaid-cli", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    # Define paths
    input_folder = "/code"  # Folder containing MMD files
    output_folder = "/diagrams"  # Folder for output PNG files
    
    convert_mmd_to_png(input_folder, output_folder)
    print("Conversion complete!")