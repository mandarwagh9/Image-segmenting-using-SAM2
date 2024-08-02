# Image Segmenting using SAM2

This project is an image segmentation application that utilizes the SAM2 (Segment Anything Model) to perform object detection and segmentation on uploaded images.

## Features

- **Image Upload**: Allows users to upload images.
- **Segmentation**: Uses SAM2 model to segment objects within the image.
- **Results**: Displays segmented masks and combined mask of the image.

## Getting Started

### Prerequisites

- Python 3.6 or later
- Flask
- Replicate Python Client

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mandarwagh9/Image-segmenting-using-SAM2.git
   cd Image-segmenting-using-SAM2
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the project root and add your Replicate API token:

   ```bash
   REPLICATE_API_TOKEN=your_replicate_api_token_here
   ```

### Running the Application

1. **Start the Flask Server**

   ```bash
   python app.py
   ```

2. **Access the Application**

   Open a web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

1. **Navigate to the Application**

   Open your web browser and go to `http://127.0.0.1:5000/`.

2. **Upload an Image**

   Use the upload form to select and upload an image. Ensure the image is in one of the allowed formats: PNG, JPG, JPEG, or GIF and its uploaded to a image hosting site, and you are able to provide a link in the `app.py` for further processing.

3. **View Results**

   After uploading, the application will process the image using the SAM2 model and display the segmentation results, including combined and individual masks in your terminal to be specific.

### File Structure

- `app.py`: Main Flask application file.
- `templates/`: Directory containing HTML templates for the web pages.
- `uploads/`: Directory for storing uploaded images.
- `requirements.txt`: File listing the Python dependencies.

### Contributing

Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue on GitHub.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [Replicate](https://replicate.com) for providing the SAM2 model.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) for the web framework.
