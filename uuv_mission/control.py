class PDController:
  def __init__(self, Kp=0.15, Kd=0.6):
    self.Kp = Kp
    self.Kd = Kd

  def controller(self, reference, depth):
    '''
    Control the depth of the UUV using a PD controller.

    Parameters:
    reference (list): The desired depth values over time.
     depth (list): The actual depth values over time.

    Returns:
    control_signals (list): The control signals to be applied to the UUV.
    '''
    control_signals = []
   #u(t) = Kp * e(t) + Kd * (e(t) - e(t-1))
   #e(t) = r(t) - y(t)  # Error signal
    Kp = self.Kp  # Proportional gain
    Kd = self.Kd   # Derivative gain
    previous_error = 0 
    for i in range (0, len(reference)-1):
      error = reference[i] - depth[i] # Calculate the error signal
      u = Kp * error + Kd * (error - previous_error)  # Control signal
      control_signals.append(u)
      previous_error = error
    return control_signals