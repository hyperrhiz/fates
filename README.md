# fates

A kit for capturing accelerometer data using LightBlue Bean, and making mix-and-match tweets from the output.

You'll need:

* A LightBlue Bean
* A technology to attach it to
* Bean Loader software
* Arduino IDE
* Six texts for remixing

# instructions

### Text files:
Put together six text files with a bunch of text you want remixed. Make them meaningful. The more meaningful, the better the result will be! Paste each into one of the accelerometer axis files (inside the folder txtin). Each will now be associated with one axis of movement.

### Bean Loader:
Get the app here: https://punchthrough.com/products/bean/guides/getting-started/os-x/
You'll notice it has  lots of "legacy" warnings - that's ok. All we're using the loader for is to make a connection to the device.

### Associate your board with arduino: 
follow these instructions:
https://punchthrough.com/products/bean/guides/getting-started/os-x/#associate-with-arduino

### Arduino IDE:
Under Tools, make sure you have LghtBlue Bean selected as your board and /dev/cu/LightBlue-Bean as your port. Upload accelerometer.ino to the board.

### Terminal:
Once you have your board connected (you can see it in your bean loader console) and accelerometer script uploaded, open Terminal and navigate to the folder where you are keeping the Python scripts.

To test your data is reading ok, run data.py in Terminal ("python data.py") and it should return a sequence of x,y,z coordinates until you tell it to stop (ctrl-x).

### Twitter:

You'll need to set up a Twitter app following their procedure. Once you have your app authentication keys, paste them into blank-keys.py rename it to keys.py

If you have your axis text files prepared as in step 1, you should be able to run the script tweets.py in Terminal. You'll see sentences start to pop up; one will be posted to Twitter every 60 seconds, in order to comply with Twitter's traffic restrictions.

#### Note

The Beans are discontinued now, but you could also use a Flora or other Arduino based system for this, wired with a Bluetooth LE module (I tested this before settling on the Bean for its small footprint, and it works fine). To transition, you'll just need to change the port settings to make sure you're picking up the right Bluetooth channel.