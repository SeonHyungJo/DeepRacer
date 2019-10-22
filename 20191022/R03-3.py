import math

def reward_function(params):
  SPEED_THRESHOLD = 12
  first_speed = SPEED_THRESHOLD / 3
  second_speed = first_speed * 2
  third_speed = first_speed * 3

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

  if not all_wheels_on_track or speed < first_speed:
    return float(1e-3)

  angle_gap = abs(heading - waypoint_angle)

  # Angle + Heading function
  if angle_gap < 5:
    if speed <=first_speed :
      reward = 0.3  
    elif speed <=second_speed :
      reward = 0.7
    else :
      reward = 1
  elif angle_gap < 10:
    if speed <=first_speed :
      reward = 0.3
    elif speed <=second_speed :
      reward = 1
    else :
      reward = 0.7
  elif angle_gap < 15:
    if speed <=first_speed :
      reward = 1  
    elif speed <=second_speed :
      reward = 0.7
    else :
      reward = 0.3
  else:
    reward = 0.001

  if heading - waypoint_angle > 0:
    if steering > 0 and isleft :
      reward *= 1
    else :
      reward *= 0.3
  else:
    if steering > 0 and isleft :
      reward *= 0.3
    else :
      reward *= 1

  # Speed function
  # if reward < SPEED_THRESHOLD / 2:
  #   reward *= 0.7

  # Distance from center function
  # if distance_from_center <= 0.5 * track_width:
	#   reward *= 1
  # else:
  #   reward *= 1e-3

  return float(reward)