import os

# Roots path of the python source code
source_roots = (
    '/Users/fancyxun/code/cv/ultralytics/ultralytics',
    '/Users/fancyxun/code/cv/ultralytics/tests',
)

# Exclude folders
exclude_folders = (
)

# Allow guessing ambiguity call
enable_ambiguity_call_guessing = True

# Output folder
output_folder = './output'

# Create output folder of not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
