# Minuscule Agent

## Introduction
Welcome to the *Minuscule Agent* repository! This project hosts a minimal but powerful AI agent, designed for efficiency and ease of use.
It can work with multiple APIs to perform a task that involves calling multiple endpoints and feeding the
results into each other. It learns on the fly about how to use the APIs.

## To read the full description of the framework please visit the following link: [Minuscule Agent](https://joinsingularity.beehiiv.com/p/automate-your-job)

## Installation

Follow these steps to install and run the AI agent:

### Prerequisites
- Ensure you have Python installed on your machine, I used Python 3.11 but should work with older versions as well.
- Git for cloning the repository.

### Cloning the Repository
First, clone the repository into a folder named "agent":
```
git clone https://github.com/ImiPataki/minuscule_agent.git agent
```
### Setting Up the Environment
Navigate to the cloned directory and set up a virtual environment:

1. Open your command prompt or terminal.
2. Navigate to the `agent` folder:
```
cd agent
```
3. Create a virtual environment:
```
python -m venv venv
 ```
4. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate.bat
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```

### Installing Dependencies
Install all the required packages:
```
pip install -r requirements.txt
```

### Updating API key
Please update the API key in the `llm.py` file with your own OpenAI API key.


### Installing the Minuscule Agent Server
Please install the *[Minuscule Agent Server](https://github.com/ImiPataki/minuscule_agent_server)* as well, as it is required for the agent to work.

## Usage
After installation and running the Server, you can start using the AI agent by running:
```
python main.py
```

## Demo
Ask the following question to the AI agent:
```
When will the sun rise at W6 9HW postcode?
```


## License
This project is licensed under the MIT License - see the `LICENSE` file for details.



