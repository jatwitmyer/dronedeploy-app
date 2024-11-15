# DroneDeploy App by jatwitmyer

## Instructions:
### 1. Start the Server
*Note: You must have python3 installed*
**Commands:**
- pip install pipenv && python3 -m venv .venv && pipenv shell
- pipenv install
- cd server && python app.py

### 2. Start the Frontend
*Note: You must have npm installed*
**Commands (in a new terminal):**
- npm install && npm start

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
