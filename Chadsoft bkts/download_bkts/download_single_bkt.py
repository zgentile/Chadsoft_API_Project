import requests
import os

''' Used Gemini to help with this one. I don't think that downloading in chunks is 
at all necessary for files like these, but just useful for me to know. This function takes
the api path, which in this case is the path directly to an rkg file, and requests the file. 
It then takes the file, and downloads it into the a ghosts folder which is created/recognized 
by the function using the os library. It also names the file based on the provided filepath,
which should be the the rightmost part of the api path. Both inputs to this function are the 
outputs of the ghost_filepath function. '''
def download(api_path, filepath):

    folder_name = "ghosts"

    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

    # Create the folder if it doesn't exist
    new_folder_path = os.path.join(parent_directory, folder_name)
    os.makedirs(folder_name, exist_ok=True)

    response = requests.get(api_path, stream=True)

    if response.status_code == 200:
       
        local_filename = filepath
        full_path = os.path.join(new_folder_path, local_filename)
        
        with open(full_path, "wb") as outfile:
            # Download the file in chunks (improves memory usage for large files)
            for chunk in response.iter_content(1024):
                outfile.write(chunk)
            print(f"File downloaded successfully: {full_path}")
    else:
        print(f"Error downloading file: {response.status_code}")
