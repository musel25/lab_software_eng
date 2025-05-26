import os
import subprocess
import shutil

# Define paths
input_folder = "/code"  # Replace with your MMD folder path
output_folder = "/diagrams"  # Replace with desired output folder path

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List all .mmd files in the input folder
mmd_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mmd')]

# Iterate through each MMD file
for mmd_file in mmd_files:
    mmd_path = os.path.join(input_folder, mmd_file)
    # Define output PNG path (same name as MMD file but with .png extension)
    png_file = os.path.splitext(mmd_file)[0] + '.png'
    png_path = os.path.join(output_folder, png_file)
    
    # Replace this with the actual command to render the MMD file to PNG
    # Example: If using a hypothetical MMD command-line tool
    try:
        subprocess.run([
            'mmd_renderer',  # Replace with actual MMD rendering tool/command
            '--input', mmd_path,
            '--output', png_path,
            '--format', 'png'
        ], check=True)
        print(f"Converted {mmd_file} to {png_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {mmd_file}: {e}")

print("Conversion complete!")