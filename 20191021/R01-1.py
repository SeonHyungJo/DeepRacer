def reward_function(params):
  #
  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  speed = params['speed']
  all_wheels_on_track = params['all_wheels_on_track']
  isleft = params['is_left_of_center']
  steering = abs(params['steering_angle'])

  SPEED_THRESHOLD = 5
  MAXIMUM_STEERING_ANGLE = 22

  if not all_wheels_on_track:
    return float(1e-3)

  # Distance from center function
  if distance_from_center <= 0.1 * track_width:
	  reward = 1
  elif distance_from_center <= 0.2 * track_width:
		reward = 0.8
  elif distance_from_center <= 0.3 * track_width:
		reward = 0.5
  elif distance_from_center <= 0.4 * track_width:
		reward = 0.1
  else:
		reward = 1e-3

  # Steering function
  if steering > MAXIMUM_STEERING_ANGLE / 2 and speed > SPEED_THRESHOLD / 2:
	  reward *= 0.3

  # Speed function
  if speed < SPEED_THRESHOLD:
	  reward *= 0.1

  return float(reward)
