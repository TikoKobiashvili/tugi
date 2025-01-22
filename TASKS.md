# Take-home exercises

## Overall instructions

The goal of these exercises is to evaluate your ability to work with a Python web framework, specifically FastAPI.

* Initialize a git repository in the project directory and commit your changes after each task.
* You should complete the tasks in the order they are presented.
* The code you write should be covered by tests and should pass the linters (see `util/lint.sh`).
* When you are finished, create a zip file of the project directory and send it back to us.
  Alternatively, you can provide a link to a private repository.

## Task 1 - Project setup & configuration

Follow the README.md file to set up the project locally.
The README.md file contains all the necessary information to set up the project.

There is nothing to commit for this task, but it is important to complete it before moving on to the next tasks.

## Task 2 - Create a mock AI endpoint

Create an endpoint in `/ai/sentiment` to provide a mock sentiment analysis service.

### Requirements

* The endpoint should accept a POST request with a JSON body containing a `text` key.
* The endpoint should return a JSON response containing a sentiment from an enum of `positive`, `negative`, or `neutral`.
* There should be a test for the endpoint.
* Place the logic for the sentiment analysis in a separate module.
  The quality of the sentiment analysis is not crucial.
* Put the interfaces in `app/schema.py` according to the naming convention described in the README.

## Task 3 - Create an asynchronous endpoint using `asyncio`

Create an endpoint that will perform work asynchronously and return the result.
The work could be anything, such as a web request, a long-running task, or a database query.

The task should fail for some invalid input (e.g. a negative number), and there should be a unit test for this.

## Task 4 - Create unit tests for the health check endpoint

Create unit tests for the health check endpoints.

Also create a unit test that requires authentication for `/health-authenticated`.

## Task 5 - Create a Dockerfile

Create a Dockerfile that can be used to run the service in a container.

Make sure the Dockerfile is set up to run the service with the correct environment variables,
and that no unnecessary files are included in the final image.

You should be able to run it simply by running `docker compose up --build`.
