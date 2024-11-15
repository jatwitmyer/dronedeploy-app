from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

data = [
  {
  "image_id": "001",
  "timestamp": "2024-09-24 14:31:05",
  "latitude": "44.4280° N",
  "longitude": "110.5885° W",
  "altitude_m": 50,
  "heading_deg": 270,
  "file_name": "YNP_001.jpg",
  "camera_tilt_deg": -15,
  "focal_length_mm": 24,
  "iso": 100,
  "shutter_speed": "1/500",
  "aperture": "f/2.8",
  "color_temp_k": 5600,
  "image_format": "RAW+JPEG",
  "file_size_mb": 25.4,
  "drone_speed_mps": 5.2,
  "battery_level_pct": 98,
  "gps_accuracy_m": 0.5,
  "gimbal_mode": "Follow",
  "subject_detection": "Yes",
  "image_tags": ["Geyser", "Steam"]
  },
  {
  "image_id": "002",
  "timestamp": "2024-09-24 14:33:22",
  "latitude": "44.4279° N",
  "longitude": "110.5890° W",
  "altitude_m": 75,
  "heading_deg": 180,
  "file_name": "YNP_002.jpg",
  "camera_tilt_deg": -30,
  "focal_length_mm": 35,
  "iso": 200,
  "shutter_speed": "1/1000",
  "aperture": "f/4",
  "color_temp_k": 5200,
  "image_format": "RAW+JPEG",
  "file_size_mb": 27.1,
  "drone_speed_mps": 3.8,
  "battery_level_pct": 95,
  "gps_accuracy_m": 0.6,
  "gimbal_mode": "Free",
  "subject_detection": "No",
  "image_tags": ["Forest", "River"]
  },
  {
  "image_id": "003",
  "timestamp": "2024-09-24 14:36:47",
  "latitude": "44.4275° N",
  "longitude": "110.5888° W",
  "altitude_m": 100,
  "heading_deg": 90,
  "file_name": "YNP_003.jpg",
  "camera_tilt_deg": 0,
  "focal_length_mm": 50,
  "iso": 400,
  "shutter_speed": "1/2000",
  "aperture": "f/5.6",
  "color_temp_k": 5800,
  "image_format": "RAW+JPEG",
  "file_size_mb": 26.8,
  "drone_speed_mps": 2.5,
  "battery_level_pct": 91,
  "gps_accuracy_m": 0.4,
  "gimbal_mode": "Tripod",
  "subject_detection": "Yes",
  "image_tags": ["Wildlife", "Elk"]
  },
  {
  "image_id": "004",
  "timestamp": "2024-09-24 14:40:13",
  "latitude": "44.4277° N",
  "longitude": "110.5882° W",
  "altitude_m": 120,
  "heading_deg": 0,
  "file_name": "YNP_004.jpg",
  "camera_tilt_deg": -45,
  "focal_length_mm": 70,
  "iso": 800,
  "shutter_speed": "1/4000",
  "aperture": "f/8",
  "color_temp_k": 6000,
  "image_format": "RAW+JPEG",
  "file_size_mb": 28.3,
  "drone_speed_mps": 1.2,
  "battery_level_pct": 87,
  "gps_accuracy_m": 0.7,
  "gimbal_mode": "Follow",
  "subject_detection": "No",
  "image_tags": ["Canyon", "Waterfall"]
  },
  {
  "image_id": "005",
  "timestamp": "2024-09-24 14:44:56",
  "latitude": "44.4282° N",
  "longitude": "110.5879° W",
  "altitude_m": 80,
  "heading_deg": 315,
  "file_name": "YNP_005.jpg",
  "camera_tilt_deg": -10,
  "focal_length_mm": 24,
  "iso": 100,
  "shutter_speed": "1/250",
  "aperture": "f/2.8",
  "color_temp_k": 5400,
  "image_format": "RAW+JPEG",
  "file_size_mb": 24.9,
  "drone_speed_mps": 6.7,
  "battery_level_pct": 82,
  "gps_accuracy_m": 0.5,
  "gimbal_mode": "Free",
  "subject_detection": "Yes",
  "image_tags": ["Thermal Pool", "Bacteria"]
  }
  ]


substring_key_correlations = {
  'id': "image_id",
  'timestamp': "timestamp",
  "latitude": "latitude",
  "longitude": "longitude",
  'altitude': "altitude_m",
  'heading': "heading_deg",
  'file name': "file_name",
  'tilt': "camera_tilt_deg",
  'focal length': "focal_length_mm",
  'iso': "iso",
  'shutter speed': "shutter_speed",
  'aperture': "aperture",
  'color temp': "color_temp_k",
  'format': "image_format",
  'size': "file_size_mb",
  'speed': "drone_speed_mps",
  'battery': "battery_level_pct",
  'gps accuracy': "gps_accuracy_m",
  'gimbal': "gimbal_mode",
  'subject detection': "subject_detection",
  'tags': "image_tags"
}

units = {
  'altitude_m': "miles",
  "camera_tilt_deg": "degrees",
  "focal_length_mm": "milimeters",
  "color_temp_k": "Kelvin",
  "file_size_mb": "megabytes",
  "drone_speed_mps": 'miles per second',
  "battery_level_pct": 'percent',
  "gps_accuracy_m": "miles"
}

substring_index_correlations = {
  "first": 0,
  "second": 1,
  "third": 2,
  "fourth": 3,
  "fifth": 4,
}

# test_query = "What is the aperture and the file size of the second image?"
def mock_AI(query):
  keys_in_query = []
  photos_referenced = []

  for key in substring_key_correlations.keys():
    if key in query:
      keys_in_query.append(key)

  for index in substring_index_correlations.keys():
    if index in query:
      photos_referenced.append(index)  
  
  # print(keys_in_query)
  # print(photos_referenced)

  if not photos_referenced:
    response = "I'm not sure which photo you are asking me about. Please try again."
    return response
  if not keys_in_query:
    response = "I don't understand what you are asking me about. Please try again."
    return response

  responses = []
  for photo in photos_referenced:
    id = substring_index_correlations[photo]
    print(f'Searching for data on the {photo} image.')
    for search_term in keys_in_query:
      key = substring_key_correlations[search_term]
      data_found = data[id][key]
      if key in units.keys():
        data_found = str(data_found) + ' ' + units[key]
      # print(data_found)
      response = f'The {search_term} of the {photo} image is {data_found}.'
      print(response)
      responses.append(response)
  response = " ".join(responses)
  print(response)
  return response


@app.route('/')
def index():
  return "Routes: /data, /query"

@app.route('/data')
def get_data():
  return data
  
@app.route('/query', methods=['POST'])
def query():
  # print(request.json)
  user_query = request.json.get('user_query')
  print(user_query)
  if not user_query:
    return jsonify({'error': 'No user query provided'}), 400
  response = mock_AI(user_query)
  return jsonify({'message': response})
   

if __name__ == '__main__':
    app.run(debug=True)