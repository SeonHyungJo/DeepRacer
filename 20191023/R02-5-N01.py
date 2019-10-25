import math


def reward_function(params):
  prev_waypoint_index = params['closest_waypoints'][0]
  next_waypoint_index = params['closest_waypoints'][1]
  next_next_waypoint_index = next_waypoint_index + \
      1 if len(params['waypoints']) > next_waypoint_index else 0

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
  speed = params['speed']
  all_wheels_on_track = params['all_wheels_on_track']
  isleft = params['is_left_of_center']

  steering = params['steering_angle']
  SPEED_THRESHOLD = 5

  if not all_wheels_on_track:
    return float(1e-3)

  # Distance from center function
  if distance_from_center <= 0.4 * track_width:
	  reward = 1
  else:
    reward = 1e-3

  # Speed function
  if speed < SPEED_THRESHOLD / 2:
	  reward = 1e-3

  if next_waypoint_angle - waypoint_angle == 0:
    if waypoint_angle != heading:
      reward *= 0.9
  # Right
  elif next_waypoint_angle - waypoint_angle < 0:
    if steering > 0:
      reward *= 0.2
  # Left
  elif next_waypoint_angle - waypoint_angle > 0:
    if steering < 0:
      reward *= 0.2

  return float(reward)
