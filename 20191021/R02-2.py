def reward_function(params):
  prev_waypoint_index = params['closest_waypoints'][0]
  next_waypoint_index = params['closest_waypoints'][1]

  prev_waypoint = params['waypoints'][prev_waypoint_index]
  next_waypoint = params['waypoints'][next_waypoint_index]
  inclination = (next_waypoint[1] - prev_waypoint[1] / next_waypoint[0] - prev_waypoint[0]) * 45

  heading = params['heading'] # (-180, 180]

  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  speed = params['speed']
  all_wheels_on_track = params['all_wheels_on_track']
  isleft = params['is_left_of_center']
  
  steering = abs(params['steering_angle'])
  SPEED_THRESHOLD = 5

  if not all_wheels_on_track:
    return float(1e-3)

  # Distance from center function
  if distance_from_center <= 0.2 * track_width:
	  reward = 1
  else:
		reward = 1e-6

  # Heading
  if inclination - heading > 10 :
    reward *= 0.03

  # Speed function
  if speed < SPEED_THRESHOLD / 2:
	  reward *= 0.1

  return float(reward)
