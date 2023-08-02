### script.py
Seaborn graph for China's wheat crop prediction till 2040
<img src="./screenshots/Screenshot 2023-08-02 at 11.22.11 PM.png">
<img src="./screenshots/Screenshot 2023-08-02 at 11.25.13 PM.png">

### json data from server
<img src="./screenshots/carbon.png">

### installation and setup
1.  dev : to install python3 and pip3 and run
    ```sh
    sudo apt-get python3
    sudo apt install python3-pip
    pip install -r requirements.txt

    flask run
    ```
1. prod : run `pip freeze > requirements.txt` in your console to create a requirements.txt file, and if while deploying you get any errors, you can remove the version numbers from the requirements.txt file and try deploying again.
1. prod : server will run this script before running the project to install the dependencies. Save this script as __build.sh__ in the root directory of the project
    ```
    #!/usr/bin/env bash
    # exit on error
    set -o errexit

    pip install --upgrade pip
    pip install wheel
    pip install -r requirements.txt
    ```