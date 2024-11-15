# DroneDeploy App by jatwitmyer

## Instructions:
cd server && python3 -m venv .venv && pip install flask && pip install flask_cors && python app.py
npm install && npm start

## Features:
### Responsive UI
  - hover event for images and chatbot
    - shadow
  - click event for images
    - show whole image large in center of screen
    - grey out rest of screen
    - click out of featured image using the button in the top right or clicking away from the image
  - click event for chatbot
    - reopens chatbot window

### Displays Drone Data
  - fetches from database and pairs with matching image
  - two columns of images for large screens
  - on column for smaller screens (and more minimized for very small)

### Input Box for User Queries
  - displays message history