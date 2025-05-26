import os
import subprocess
import sys

def convert_mmd_to_images(input_folder, output_folder):
    """Convert all .mmd files to both SVG and PNG formats with enhanced quality."""
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
        base_name = os.path.splitext(mmd_file)[0]
        
        # Define output paths for both formats
        svg_path = os.path.join(output_folder, f"{base_name}.svg")
        png_path = os.path.join(output_folder, f"{base_name}.png")
        
        try:
            # Convert to SVG with improved settings
            subprocess.run([
                'mmdc',
                '-i', mmd_path,
                '-o', svg_path,
                '-b', 'transparent',
                '--scale', '3',  # Increased scale for better quality
                '--backgroundColor', 'transparent'
            ], check=True)
            
            # Convert to PNG with high quality
            subprocess.run([
                'mmdc',
                '-i', mmd_path,
                '-o', png_path,
                '-b', 'transparent',
                '--backgroundColor', 'transparent',
                '--scale', '3',
                '--width', '2400',  # Increased width for better resolution
                '--height', '1600'  # Increased height for better resolution
            ], check=True)
            
            print(f"Successfully converted {mmd_file} to SVG and PNG formats")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {mmd_file}: {e}", file=sys.stderr)
        except FileNotFoundError:
            print("Error: mmdc command not found. Please install mermaid-cli first:", file=sys.stderr)
            print("npm install -g @mermaid-js/mermaid-cli", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    # Define paths relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(script_dir, "code")
    output_folder = os.path.join(script_dir, "diagrams")
    
    convert_mmd_to_images(input_folder, output_folder)
    print("Conversion complete!")