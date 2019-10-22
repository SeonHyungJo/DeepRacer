import math
PREV_ANGLE = 0

def reward_function(params):
  SPEED_THRESHOLD = 5
  
  prev_waypoint_index = params['closest_waypoints'][0]
  next_waypoint_index = params['closest_waypoints'][1]
  next_next_waypoint_index = next_waypoint_index + 1 if len(params['waypoints']) == next_waypoint_index  else 0

  prev_waypoint = params['waypoints'][prev_waypoint_index]
  next_waypoint = params['waypoints'][next_waypoint_index]
  next_next_waypoint = params['waypoints'][next_next_waypoint_index]

  waypoint_angle =  math.atan2(next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0]) * 180 / math.pi
  next_waypoint_angle = math.atan2(next_next_waypoint[1] - next_waypoint[1], next_next_waypoint[0] - next_waypoint[0]) * 180 / math.pi
  
  heading = params['heading'] # (-180, 180]

  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  speed = params['speed']
  all_wheels_on_track = params['all_wheels_on_track']
  isleft = params['is_left_of_center']
  steering = params['steering_angle']

  # Distance from center function
  if distance_from_center <= 0.52 * track_width:
	  reward = 1
  else:
    reward = 1e-6

  # Heading
  if abs(heading - waypoint_angle) > 7 :
    reward *= 0.5

  if abs(heading - next_waypoint_angle) > 15 :
    if speed > SPEED_THRESHOLD / 2:
      reward *= 1e-3

  if abs(waypoint_angle - next_waypoint_angle) < 5:
    if abs(steering) > 2.5:
      reward *= 1e-3

  if next_waypoint_angle * steering < 0:
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