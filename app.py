import os
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Path to the directory containing the images
image_directory = 'static/image_directory'

# List all image filenames in the directory
image_filenames = os.listdir(image_directory)[:20]  # Select the first 20 images

# Path to the CSV file to store the data
csv_file = 'data.csv'

# Create the CSV file if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Image', 'Emotion'])  # CSV headers

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the selected emotion from the form
        selected_emotion = request.form['emotion']

        # Get the filename of the current image being displayed
        current_image = request.form['current_image']

        # Save the image filename and selected emotion to the CSV file
        with open(csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([current_image, selected_emotion])

    # Get the next image filename
    if len(image_filenames) > 0:
        next_image = image_filenames.pop(0)
    else:
        next_image = None

    return render_template('index.html', next_image=next_image)


if __name__ == '__main__':
    app.run()(debug=False,host='0.0.0.0')

