<p align="center">
  <img width="300" src="static/images/Logo.png">
</p>

# **RPi Contact sensor wakeup alarm**
### Wakeup alarm that 'beeps' until some action is performed

Based on Flask, it creates a Web Server on a Raspberry Pi in which you can set the wakeup time, then at the decided time the Buzzer will ring until the contact sensor is closed (ex: foldaway bed) or 30 mins passed.

It's designed to work as a mobile web app, but can also be used from the Desktop browser.

# *Wiring schema*

<p align="center">
  <img width="500" src="static/images/schema.png">
</p>

# *Installation*

* Download or clone the code
* run `pip install -r requirements.txt`
* start with `python main.py`

# *Front-end screens*
<p align="center">
  <img style="padding:20px" width="19%" src="static/images/mobile-screenshot.jpg">
  <img style="padding:20px" width="65%" src="static/images/desktop-screenshot.jpg">
</p>

