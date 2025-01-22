# test-service

## Development setup

### Prerequisites

* Python 3.12
* PyCharm (optinal but recommended)

### Set up local development environment

1. **Configure the environment**: Copy the file `.env.sample` to `.env` and fill in 
   the required values.

2. **Run the dev-setup script**: Run the script `./util/dev-setup.sh` to create a Python
   virtual environment and install the required dependencies.

3. **Open the project in PyCharm**: Open the project in PyCharm and configure the
   Python interpreter to use the virtual environment created in step 2. This should happen automatically

### Endpoints

See `/redoc` (e.g. http://localhost:8041/redoc when running locally) for the API documentation which will
list all available endpoints.

### Linting & tests

The following tools are used to statically analyze the code:

* `flake8` - Code linter.
* `mypy` - Type checker.
* `bandit` - Security flaw analysis.

You can run the linter & tests using the following commands:

* **Run the linter**: `./util/lint.sh`
* **Run the tests**: `./util/test.sh` (this will also run the linter)

#### Test coverage

After running the tests, [`htmlcov/index.html`](../htmlcov/index.html) will contain the coverage report.

## Project structure

* `app` - Production code and business logic.
* `clients` - Auto-generated API clients are stored here. See `util/generate-clients.sh`.
* `logs` - Logs will be written to this directory when running the service.
* `requirements` - Dependency management.
* `tests` - Tests.
* `util` - Scripts to automate various tasks, chores & analyses.
* `.idea` - Contains configuration related to PyCharm.

## App structure

As mentioned above, production & business logic lies within the `app` directory.

* `app/config` - Configuration files belong here.
* `app/routers` - Routers that will route API requests to their respective internal functions.

### Schema

The API needs well-defined data structures that describes all possible variations
of input & output. The way this is achieved is using `pydantic`.

The file `app/schema.py` should contain all data structures that are exposed in the API,
which means any input received or output produced should ultimately be of a class that
is defined in `app/schema.py`.

#### Naming convention

Any API operations (e.g. `@router.post`) should have a class called `XxxRequest` and
the output of those operations should be a class called `XxxResponse`.

Even if the API just takes one parameter and returns one parameter, it should be wrapped
in such an object, because in the future there may be an additional parameter, which
will be easier to change if there already is a class.
