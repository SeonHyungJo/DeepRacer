import math
PREV_SPEED = 0

def reward_function(params):
  global PREV_SPEED
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
  isleft = params['is_left_of_center']
  steering = params['steering_angle']

  # Distance from center function
  if distance_from_center <= 0.52 * track_width:
	  reward = 1
  else:
    reward = 1e-3

  if speed < SPEED_THRESHOLD / 2:
    return float(1e-3)

  # Heading
  if abs(heading - waypoint_angle) > 5 :
    reward *= 1e-3
  elif waypoint_angle - next_waypoint_angle < 5:
    if speed >= PREV_SPEED:
      reward *= 1
    else:
      reward *= 0.5

  if abs(waypoint_angle - next_waypoint_angle) > abs(steering):
    reward *= 1e-3

  # Current Angle
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

  # Next Angle
  if abs(next_waypoint_angle - waypoint_angle - heading) + 5 > abs(steering):
      reward *= 1
  else:
      reward *= 1e-3

  PREV_SPEED = speed

  return float(reward)