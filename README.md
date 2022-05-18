# E2E Final Project

Final project's aim is to predict rent price based on some characteristics of an apartment. 

# Source data

We have data from Yandex.Realty classified [https://realty.yandex.ru](https://realty.yandex.ru/) containing real estate listings for apartments in St. Petersburg and Leningrad Oblast from 2016 till the middle of August 2018. 

## Descriptive statistics

**Firstly, here is the brief description of the main variables:**
|variable|description  |
|--|--|
|last_price |last rent price on the website |
|floor | floor of the apartment
|rooms | number of rooms in the apartment |
|area | total area of the apartment |
|agent_fee | agent fee, % from the rent price |
|renovation | type of renovation |


**Below is some descriptive statistics for cleaned dataset.** 

1. Basic descriptive statistics

|variable|min|max|mean|median|
|--|--|--|--|--|
|last_price| 9'900.00 |199'000|32'276.84|25'000|
|floor|1|36|6.62|5|
|rooms|0|5|1.67|2|
|area|12|200|54.21|47|
|agent_fee|0|100|70.79|60|
|renovation|0|11|3.73|1|

2. Most rent prices are below 100'000 roubles. Variable has a non-normal distribution.

*Histogram of last price*

![Histogram of last price](https://sun9-40.userapi.com/s/v1/ig2/6FVnDxI2Sk4HZLyOkUIgwXsr1iFbjtJ9xunSPl8aQDQTmKXUEVl9A2Ge2DMmC9W3RgZOzJC0uJ1yFGkkAaxpBUSV.jpg?size=323x225&quality=96&type=album)

3. Most apartments for rent have 1 or 2 rooms.

*Bar chart of rooms number*

![enter image description here](https://sun9-12.userapi.com/s/v1/ig2/pesVADZ8Ke1gqnWXVNvfxzUMPoyJBrtm6VcG8VmIqefEbhph4QGJnEm4i2pCRiTJNjQb-TPP860xlFoIqiq9FMAz.jpg?size=342x219&quality=96&type=album)

4. Correlation matrix for all variables. 

![enter image description here](https://sun9-20.userapi.com/s/v1/ig2/GH4Q-ys0kFr5kQBiq7lmGfcZru4EV7JXn0IalAXVyHJipAIykzLhRz8FYC2Whwyj69eFRJBMrewakcABhknuSpTY.jpg?size=402x313&quality=96&type=album)

# Models

2 models were built for predicting rent price. Based on the correlation matrix and common sense it was decided to choose following variables: floor, open_plan, rooms, area (for the 1st model); floor, open_plan, rooms, area, agent_fee, renovation (for the 2nd model).

For both models train sample consists of all data before the 1st of April and test sample - after the 1st of April. Both models' framework is Random Forest. For choosing hyperparams grid search was conducted for both models.

# Installing instructions and running app with virtual environment

To run app in virtual environment firstly connect to virtual machine and go to the necessary folder. Then install and activate virtual environment with the following commands:
>sudo apt install python3.8-venv
>python3 -m venv env
>source env/bin/activate

As the next step, install all the necessary packages:
>pip install numpy
>pip install flask
>pip install joblib
>pip install sklearn

Now run app:
>python app.py

# Dockerfile

It contains instructions for building the docker container:
> from ubuntu:20.04
MAINTAINER Anna Lisitcyna
RUN apt-get update -y
COPY . /opt/final_project
WORKDIR /opt/final_project
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py

#  Port in remote VM

To open the port in remote Virtual Machine this piece of code is used:
> if __name__ == '__main__':  
    app.run(debug = True, port = 5444, host = '0.0.0.0')

# Running app using docker

Firstly, build the docker:
>docker build -t test/final_project:v.0.1 .

Then run it:
>docker run --network host -it test/final_project:v.0.1 /bin/bash
>python3 app.py

It uses port 5444.
