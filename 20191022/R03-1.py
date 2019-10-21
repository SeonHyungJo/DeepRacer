import math

PREV_ANGLE = 0

def reward_function(params):
  SPEED_THRESHOLD = 12
  global PREV_ANGLE

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

  if not all_wheels_on_track:
    return float(1e-3)

  angle_gap = abs(heading - waypoint_angle)

  # Angle + Heading function
  if angle_gap < 5:
    if waypoint_angle - PREV_ANGLE < 0 and isleft:
      reward = 1
    elif waypoint_angle - PREV_ANGLE < 0 and not isleft:
      reward = 0.001
    elif waypoint_angle - PREV_ANGLE > 0 and isleft:
      reward = 0.001
    elif waypoint_angle - PREV_ANGLE > 0 and not isleft:
      reward = 1
    else:
      reward = 1
  else:
    reward = 0.001

  # Speed function
  reward *= speed / SPEED_THRESHOLD

  # Distance from center function
  if distance_from_center <= 0.4 * track_width:
	  reward *= 1
  else:
    reward *= 1e-3

  print("PREV_ANGLE", PREV_ANGLE)
  PREV_ANGLE = waypoint_angle
  return float(reward)