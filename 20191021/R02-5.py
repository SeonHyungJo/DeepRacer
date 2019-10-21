import math

def reward_function(params):
  prev_waypoint_index = params['closest_waypoints'][0]
  next_waypoint_index = params['closest_waypoints'][1]

  prev_waypoint = params['waypoints'][prev_waypoint_index]
  next_waypoint = params['waypoints'][next_waypoint_index]
  waypoint_angle =  math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0]) * 180 / math.pi
  
  heading = params['heading'] # (-180, 180]

  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  speed = params['speed']
  all_wheels_on_track = params['all_wheels_on_track']
  isleft = params['is_left_of_center']
  
  steering = params['steering_angle']
  SPEED_THRESHOLD = 5

  if not all_wheels_on_track:
    return float(1e-3)

  # Distance from center function
  if distance_from_center <= 0.2 * track_width:
	  reward = 1
  if distance_from_center <= 0.3 * track_width:
	  reward = 0.7
  if distance_from_center <= 0.5 * track_width:
	  reward = 0.3
  else:
    reward = 1e-3

  # Heading
  if abs(heading) - abs(waypoint_angle) > 10  :
    reward *= 0.8

  # Speed function
  if speed < SPEED_THRESHOLD / 2:
	  reward = 1e-3

  if waypoint_angle * steering < 0:
    if isleft:
      reward *= 1
    else:
      reward *= 0.01
  else:
    if isleft:
      reward *= 0.01
    else:
      reward *= 1
  return float(reward)