### tasks
- [ ] [temperature data- country wise](https://climateknowledgeportal.worldbank.org/download-data)
    - for data from 1960s to 2021, check [this](py/temp_prev_data.png)
    - for predicted data from, check [this](py/temp_pred_data.png)
    - merge these two sheets and create one csv
        - delete rows with data till 1961
        - copy rows from 2022 to 2100 and paste it in the pred_document
        - drop first row and all the country-columns so that only year and temperature remains
- [ ] [get crop datasheet](https://docs.google.com/spreadsheets/d/1qPP5FzFYa5JpMEu8WhVvxF2-kvKqf_0Qg7zEU55pdf0/edit#gid=441730022) with that country 
    - enable filter, copy all the present cells and then paste it in a new sheet
    - add a column before 'Wheat' and paste the respective observed Temperatures


### constraints
- only year greater than 2021 and less than 2100
- i will give the list of countries and list of crops 
- an array will be returned with the predicted values


### installation and setup
1.  dev : to install python3 and pip3
    ```sh
    sudo apt-get python3
    sudo apt install python3-pip
    pip install pandas numpy tensorflow sklearn
    pip3 install -U scikit-learn scipy matplotlib seaborn
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