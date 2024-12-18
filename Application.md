# URL Shortener Backend Challenge - Application Details

## Application

The application simulates a URL shortening service with the following resources:

- **ShortenURL**
- **RedirectURL**
- **URLAnalytics**

**Please read the challenge completely before starting the implementation.**

## Challenge

Clone this repository and complete the implementation of the provided boilerplate code. The application should provide the following functionalities:

### Your Tasks

- **Implement Missing Code**: Complete the implementation of the provided boilerplate code.
- **Implement the Following Functionalities**:
  - **Shorten a URL**: Users should be able to shorten a given URL and optionally set a custom expiration time.
  - **Update Expiration Time**: If an `id` is provided, update the expiration time of the existing shortened URL corresponding to that `id`.
  - **Redirect to Original URL**: Users should be redirected to the original URL when accessing the shortened URL.
  - **Retrieve URL Analytics**: Users should be able to get analytics for a shortened URL, including access count and expiration time.
- **Write Tests**: Implement tests for all endpoints, ensuring they cover various scenarios and edge cases.
- **Achieve Test Coverage**: Ensure that all tests pass and aim for a test coverage of 94% or above.


## Available APIs

### POST `/shorten`

**Description**: Shorten a URL. You should also be able to update the expiration time of a shortened URL if an `id` is provided.

**Request Payload**:

```
{
    "id": 1,  // Optional. If provided, update the expiration time of the shortened URL with this ID.
    "url": "http://example.com",
    "custom_expiration": {
        "type": "DAY",  // Options: SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, YEAR
        "value": 1
    }
}
```

**Response**:

```
{
    "id": 1,
    "url": "http://example.com",
    "custom_expiration": {
        "type": "DAY",
        "value": 1
    },
    "short_url": "http://localhost:5000/abc123"
}
```

### GET `/analytics/<short_url>`

**Description**: Get analytics for a shortened URL.

**Response**:

```
{
    "original_url": "https://example.com",
    "short_url": "http://localhost:5000/abc123",
    "access_count": 12,
    "expiration_time": "2021-08-01 12:00:00"
}
```

### GET `/<short_url>`

**Description**: Redirect to the original URL using the short URL.

**Example**:

Visiting `http://localhost:5000/abc123` in your browser will redirect you to `http://example.com`.


Feel free to add more endpoints or functionalities as you wish. We're looking for innovative solutions!

## Tests

Three dummy test functions are provided:

```
def test_shorten_url(client):
    """
    Test the /shorten endpoint to shorten a URL.
    """
    assert 1 == 2

def test_redirect_to_original(client):
    """
    Test the redirection from a short URL to the original URL.
    """
    assert 1 == 2

def test_get_analytics(client):
    """
    Test the /analytics endpoint to get analytics for a shortened URL.
    """
    assert 1 == 2
```

Your task is to implement these tests to verify the functionality of your application.
Feel free to add more tests as needed.

To run the tests, use:

```
pytest -vvv -s tests/

# For test coverage report
# pytest --cov
# open htmlcov/index.html
```

## Optional: Dockerization

To stand out in your submission, you can Dockerize the application:

- **Dockerfile**: Create a `Dockerfile` that defines the Docker image for your application.
- **docker-compose.yml**: Create a `docker-compose.yml` file to manage multi-container deployments if necessary.
- **Documentation**: Provide clear instructions on how to build and run the application using Docker.


## How to Submit

For submitting the assignment, please follow these steps:

* Ensure that you push your code into a private repository on GitHub.
* Add `Shwetabhk` and `kartikeyrajvaidya` as collaborators to your repository with Admin access.
* For steps to add a collaborator to your repository, refer to [this link](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository).

**Once you are done with your task, please use [this form](https://forms.gle/khbqTVLnMtbiQZTp6) to complete your submission.**

Once you submit the assignment, you will hear back from us within 2 working days via email.

We look forward to seeing your solution!

---

For any questions or clarifications, feel free to reach out to us.

