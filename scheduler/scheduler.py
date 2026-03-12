```python
import time
from datetime import datetime
from autoposter.autoposter import autopost
from agent.autopilot import autopilot

def run_every(seconds, task, *args, **kwargs):
    while True:
        task(*args, **kwargs)
        time.sleep(seconds)

def run_daily(task, *args, **kwargs):
    while True:
        now = datetime.now()
        target = now.replace(hour=9, minute=0, second=0, microsecond=0)

        if now > target:
            target = target.replace(day=now.day + 1)

        wait_seconds = (target - now).total_seconds()
        time.sleep(wait_seconds)

        task(*args, **kwargs)

def schedule_autopost_every(hours, content):
    seconds = hours * 3600
    run_every(seconds, autopost, content)

def schedule_autopilot_every(hours, content):
    seconds = hours * 3600
    run_every(seconds, autopilot, content)

def schedule_daily_autopost(content):
    run_daily(autopost, content)

def schedule_daily_autopilot(content):
    run_daily(autopilot, content)
```
