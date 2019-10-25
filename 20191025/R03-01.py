import math

def reward_function(params):
  SPEED_THRESHOLD = 5

  prev_waypoint_index = params['closest_waypoints'][0]
  next_waypoint_index = params['closest_waypoints'][1]
  next_next_waypoint_index = next_waypoint_index + \
      1 if len(params['waypoints']) == next_waypoint_index else 0

  prev_waypoint = params['waypoints'][prev_waypoint_index]
  next_waypoint = params['waypoints'][next_waypoint_index]
  next_next_waypoint = params['waypoints'][next_next_waypoint_index]

  waypoint_angle = math.atan2(
      next_waypoint[1] - prev_waypoint[1], next_waypoint[0] - prev_waypoint[0]) * 180 / math.pi
  next_waypoint_angle = math.atan2(
      next_next_waypoint[1] - next_waypoint[1], next_next_waypoint[0] - next_waypoint[0]) * 180 / math.pi

  heading = params['heading']  # (-180, 180]

  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  all_wheels_on_track = params['all_wheels_on_track']
  speed = params['speed']
  isleft = params['is_left_of_center']
  steering = params['steering_angle']

  progress = params['progress']

  if not all_wheels_on_track:
    return float(1e-3)
  
  # Speed Function
  if speed < SPEED_THRESHOLD / 2:
    return float(1e-3)

  # Heading
  if abs(heading - waypoint_angle) > 10:
    return float(1e-3)

  if abs(next_waypoint_angle - waypoint_angle) < 0:
    # Distance from center function
    if distance_from_center <= 0.2 * track_width:
      reward = 1
    else:
      reward = 1e-3
  else:
    # Distance from center function
    if distance_from_center <= 0.4 * track_width:
      reward = 1
    else:
      reward = 1e-3

  # Current Angle
  if waypoint_angle * steering < 0:
    if isleft:
      reward *= 1
    else:
      reward *= 0.7
  else:
    if isleft:
      reward *= 0.7
    else:
      reward *= 1

  # Next Angle
  if abs(next_waypoint_angle - heading) + 5 > abs(steering):
      reward *= 1
  else:
      reward *= 0.7

  return float(reward)
