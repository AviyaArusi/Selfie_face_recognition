import face_recognition
import os
from shutil import copy2
import time
from multiprocessing import Pool

def process_image(args):
    image_file, your_face_encoding, photo_directory, output_directory = args
    try:
        # Load an image
        current_image = face_recognition.load_image_file(os.path.join(photo_directory, image_file))
        
        # Find all the faces in the image
        current_image_encodings = face_recognition.face_encodings(current_image)
        
        # Compare faces found to your face
        for face_encoding in current_image_encodings:
            results = face_recognition.compare_faces([your_face_encoding], face_encoding)
            if results[0]:  # If a match was found
                copy2(os.path.join(photo_directory, image_file), output_directory)
                return True  # Indicate a match
    except Exception as e:
        print(f"Error processing {image_file}: {e}")
    return False  # No match found or error occurred

# Start time measurement
start_time = time.time()

# Load your selfie image and encode your face
your_face_image = face_recognition.load_image_file("selfie.jpeg")
your_face_encoding = face_recognition.face_encodings(your_face_image)[0]

# Path to the directory containing wedding photos
photo_directory = 'myPhotos'
output_directory = 'OutputImage'
os.makedirs(output_directory, exist_ok=True)

# Get a list of all images in the directory
image_files = os.listdir(photo_directory)

# Prepare arguments for parallel processing
args = [(image_file, your_face_encoding, photo_directory, output_directory) for image_file in image_files]

# Use multiprocessing Pool to process images in parallel
with Pool() as pool:
    pool.map(process_image, args)

# End time measurement
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Photos where you appear have been copied.")
print(f"Time taken: {elapsed_time:.2f} seconds.")

