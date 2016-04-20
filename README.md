# Demo Edges

App with some demonstrator code/data for Edges

## Installation

Clone the project:

    git clone https://github.com/richard-jones/demo-edges.git

get all the submodules

    cd demo-edges
    git submodule update --init -- recursive

Install esprit and magnificent octopus, and related dependencies

    pip install -r requirements.txt

Create your local config

    cd demo-edges
    touch local.cfg

Then you can override any config values that you need to

Then, start your app with

    python service/web.py

You can visit the running application at:

    http://localhost:5029

## Loading the test data

For the demo intererfaces to function, you need to load the test data.  The following scripts can be run:

### UK Election data

    cd demo-edges/data/election
    sh load.sh
    

    