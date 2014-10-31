pqaut
=====
Automation for BDD testing PyQt apps

Requirements
---------------
pqaut requires: 
* Qt 5.2 or greater
* Python 2.7 or greater
* PyQt 5.2 or greater

Getting Started
---------------
pqaut is a client / server library that enables BDD-style testing in your PyQt apps. We use pqaut with [behave](http://pythonhosted.org/behave/) to make test assertions against our UI.

First, you need to get *pqaut* and *behave* installed. Assuming you are using pip, add them to your requirements.txt file and install them from PyPi.


### Running the Automation Server
In your application, you need to run the pqaut server. It's good to put it behind a launch argument so that it only runs while you're testing. Here's an example of doing this in main.py of your PyQt app:

```
import pqaut.server

if __name__ == '__main__':
    if '--automation_server' in sys.argv:
        pqaut.server.start_automation_server()

  # Start up our Qt application down here
```

### Setting up the Automation Client
Now we need to set up our first behave test to launch our app. In your `features\environment.py` file (create it if you don't have it, add something like this:

```
import subprocess
import pqaut.client

APP_PATH = '<path to your app>'

def launch_app():
    context.test_app_process = subprocess.Popen([APP_PATH, "--automation_server"])
    pqaut.client.wait_for_automation_server()

def kill_app():
    if context.test_app_process:
        subprocess.Popen.kill(context.test_app_process)

def before_scenario(context, scenario):
    launch_app()

def after_scenario(context, scenario):
    kill_app()

### Testing the App
Now it's time to make assertions against the UI. Make a feature file `features/hello_world.feature`:

```
Feature: Hello World
  As a developer
  I want to do automated testing
  So I can refactor without worry

  Scenario: Hello World
    When I tap button "Say Hello"
    Then I see "Hello World!"
```

Make a steps definition file `features/steps/hello_world_steps.py`:

```
import pqaut.client
from behave import *

use_step_matcher("re")

@when(u'I tap button "(?P<button_text>[^"]*)"$')
def i_tap_button(step, button_text):
  pqaut.client.tap(button_text)

@then(u'I see "(?P<text>[^"]*)"$')
def i_see(step, text):
  pqaut.client.assert_is_visible(text)
```

This, of course, assumes your PyQt app has a button labeled 'Say Hello', and tapping that button will display the text 'Hello World!' somewhere. You should be able to run `behave` from your project directory and see the app launch and the button press down.

Other Examples
---------------
To see a practical example of pqaut in action, check out [ci_screen](https://github.com/garyjohnson/ci_screen).

Also, pqaut uses itself for testing. You can run `behave` from the project directory to run the tests, and see the Qt apps used for testing in the `test_apps/` directory
