def amp_to_watt_hours(amp_hour):
  """
  Converts Amp-hour to Watt-hours.

  Args:
    amp_hour: The value in Amp-hours.

  Returns:
    The equivalent value in Watt-hours.
  """
  watt_hours = amp_hour * 3600  # 1 Amp-hour = 3600 Watt-hours
  return watt_hours

def watt_hours_to_amp_hours(watt_hours):
  """
  Converts Watt-hours to Amp-hours.

  Args:
    watt_hours: The value in Watt-hours.

  Returns:
    The equivalent value in Amp-hours.
  """
  amp_hour = watt_hours / 3600  # 1 Watt-hour = 3600 Amp-hours
  return amp_hour

# Get input from the user
try:
  amp_hour = float(input("Enter the Amp-hour value: "))
  
  if amp_hour < 0:
      print("Amp-hour value must be non-negative.")
  else:
      # Convert and display the results
      watt_hours = amp_to_watt_hours(amp_hour)
      print(f"Amp-hour: {amp_hour} Amp-hours")
      print(f"Watt-hours: {watt_hours} Watt-hours")
      
except ValueError:
  print("Invalid input. Please enter a number.")
