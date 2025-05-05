# URL Shortener Backend Service

This repository provides the backend implementation of a URL shortening service. The service allows users to shorten long URLs into concise, easy-to-share links and manage them efficiently.

## Features

- **URL Shortening**: Convert long URLs into short and manageable links.
- **Redirect Functionality**: Automatically redirect users to the original URL using the short link.
- **Analytics**: Track usage statistics for shortened URLs (e.g., click counts, timestamps).
- **API-Driven**: Expose APIs for integration with other applications or frontends.
- **Scalable Architecture**: Designed to handle high traffic efficiently.

## Tech Stack

This backend service is built with the following technologies:

- **Python**: Core language for the backend logic and API implementation.
- **Flask**: For creating RESTful APIs.
- **SQLite**: A relational database for storing URL mappings and analytics.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/rajtoshranjan/url-shortner-backend.git
   cd url-shortner-backend
   ```

2. Run the server using docker:
   ```bash
   docker-compose up
   ```
