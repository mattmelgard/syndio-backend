# Syndio Backend Test

A simple little API for the [Syndio Backend Test](https://gist.github.com/kpurdon/ac43d733370e89824304e89d3ec502bf) take home exercise.

## Local Development

### 1. Pre-reqs

To spin up the local development environment, you'll first want to install the dependencies into a virtualenv.

This can be accomplished in many different ways, but the easiest way to do so is to use the built in [venv](https://docs.python.org/3/library/venv.html) module like so:

```shell
> python3 -m venv env
> source env/bin/activate
```

Once the virtualenv is activated you can then install the dependencies by running:
```shell
> pip install -r requirements.txt
```

### 2. Running the Application

To run the application, ensure the virtualenv you created earlier is activated and run:

```shell
> python main.py
```

 By default, the application will be exposed on `lcoalhost` port `8080`, to change this, set the environment variable `PORT` to the port number you'd like to use instead:

```shell
> export PORT=8081
> python main.py
```

You should now be able to navigate to `http://localhost:8080` if you did not set a custom port, otherwise you can reach the application at `http://localhost:${PORT}`

### 3. Testing with The Employees Route

You're now ready to test out a route using `cURL`. With the app running in a separate shell window, you can run the following to get data from the `/employees` endpoint:

```shell
> export PORT=8080 # Or the custom port you defined above
> curl -X GET http://localhost:${PORT}/employees
[
  {
    "gender": "male",
    "id": 1
  },
  {
    "gender": "male",
    "id": 2
  },
  {
    "gender": "male",
    "id": 3
  },
  {
    "gender": "female",
    "id": 4
  },
  {
    "gender": "female",
    "id": 5
  },
  {
    "gender": "female",
    "id": 6
  }
]
```
