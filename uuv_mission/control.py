def control_depth(reference, depth): # type: ignore
  '''
  Control the depth of the UUV using a PD controller.

  Parameters:
  reference (list): The desired depth values over time.
  depth (list): The actual depth values over time.

  Returns:
  list: The control signals to be applied to the UUV.
  '''
  control_signals = []
   #u(t) = Kp * e(t) + Kd * (e(t) - e(t-1))
   #e(t) = r(t) - y(t)  # Error signal
  Kp = 0.15  # Proportional gain
  Kd = 0.6   # Derivative gain
  for i in range (0, len(reference)-1):
      error = reference[i] - depth[i]
      # Calculate the error signal
      u = Kp * error + Kd * (error - (reference[i-1] - depth[i-1]))  # Control signal
      control_signals.append(u)
  return