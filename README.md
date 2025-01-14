# Chat Application

## Project Overview
This is a real-time chat application built with Django, Channels, and AWS Lambda functions.

### Frontend
- The frontend is a responsive webpage with a fixed navbar, a collapsible left menu, and a chat interface.
- The page adjusts its layout based on screen size using JavaScript.

### Backend
- The backend is powered by Django with Django Channels for real-time WebSocket communication.
- Users can sign up, log in, and chat with each other.

### AWS Lambda Functions
- **add_numbers.py**: Adds two numbers and returns the result.
- **upload_file.py**: Uploads files to an S3 bucket.

### Hosting Instructions
1. Clone the repository.
2. Set up a Django project with the necessary configurations (channels, WebSockets).
3. Configure AWS Lambda for adding numbers and uploading files to S3.

### Running the Project
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
