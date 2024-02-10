# MusXTube Video Downloader

MusXTube is a simple web application built using Flask that allows users to download YouTube videos and audio files. The application uses the Pytube library to fetch video information and download media files. This README file provides information on setting up and running the project.

## Features
- **Video Information Retrieval:** Enter a YouTube video URL, and the application fetches and displays relevant information such as video title and thumbnail.
- **Video and Audio Download:** Users can download the video in MP4 format or the audio in MP3 format.
- **Automatic File Deletion:** Downloaded files are automatically deleted after 20 seconds to save storage space.

## Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.6)
- Flask
- Pytube

Install the required Python packages using the following command:
```bash
pip install Flask pytube
```

# How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/musxeto/MusXTube.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd MusXTube
    ```

3. **Run the Flask application:**
    ```bash
    python app.py
    ```

4. **Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the application.**

# Usage

1. Enter a YouTube video URL in the provided form.
2. Click the "Download" button to fetch video information.
3. Video information, including the title and thumbnail, will be displayed.
4. Choose to download either the video or audio by clicking the respective buttons.
5. The file will be downloaded, and an automatic deletion timer will start.

# Project Structure

- **app.py:** Contains the Flask application code.
- **templates/index.html:** HTML template for the web interface.
- **static/css/styles.css:** CSS styles for the web interface.

# Dependencies

- Flask
- Pytube

# Acknowledgments

MusXTube uses Flask and Pytube to provide a simple and efficient video downloading experience.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
