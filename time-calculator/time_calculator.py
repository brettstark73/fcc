def add_time(start, duration, day=None):
  new_time = start
  days_count = 0

  time, period = start.split()
  hour, minute = time.split(':')
  # print(time, hour, minute)

  dur_hr, dur_min = duration.split(':')
  # print(dur_hr, dur_min)

  hour = int(hour)
  minute = int(minute)
  dur_hr = int(dur_hr)
  dur_min = int(dur_min)

  if (period=="PM"):
    hour += 12
  # should now be in 24 hr time
  print("start time", hour, minute, period, "adding: ", dur_hr, dur_min)


  new_hour = hour + dur_hr
  new_minute = minute + dur_min
  
  while(new_minute > 59):
    new_hour += 1
    new_minute -= 60

  days_count = new_hour // 24
  print("interim new time", new_hour, new_minute, period, "days", days_count)
  # print("modulo", new_hour%24)

  new_hour = new_hour%24
  
  if (new_hour >= 12):
    new_hour -= 12
    period = "PM"
  else:
    period = "AM"

  if (new_hour == 0):
    new_hour = 12
    
  print("12 hr new time", new_hour, new_minute, period, "days", days_count)

  new_hour, new_minute, period = str(new_hour), str(new_minute).zfill(2), str(period)

  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  lower_week = [x.lower() for x in week]
  # print(lower_week)

  new_day = None
  if day:
    # find a new day
    day_index = lower_week.index(day.lower())
    new_day_index = (day_index + days_count%7)%7
    # print("day", days_count, day, day_index, new_day_index, week[new_day_index])
    # print("old day", day)
    day = ", " + week[new_day_index]
    print("new day", day)
  else:
    day=""

  if (days_count == 0):
    new_time = new_hour + ":" + new_minute + " " + period + day
    # print(new_time)
  elif (days_count == 1):
    new_time = new_hour + ":" + new_minute + " " + period + day + " (next day)"
    # print(new_time)
  else:
    new_time = new_hour + ":" + new_minute + " " + period + day + " (" + str(days_count) + " days later)"
    # print(new_time)
    
  return new_time
