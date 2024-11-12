# URL Shortener Backend Challenge

## Who is this for?

This challenge is meant for candidates applying for the **Senior Member of Technical Staff (SMTS)** position to work with our engineering team. We are looking for experienced professionals who can make significant contributions to our projects.

## Why work with us?

We are a SaaS product startup based in Bangalore, founded by startup veterans. We want to build a great product, sell it worldwide, and have fun doing it!

Check out our [careers page](https://careers.fylehq.com/) to get a glimpse of what it's like to work with us. Also, check out our Glassdoor reviews [here](https://www.glassdoor.co.in/Reviews/Fyle-Reviews-E1723235.htm). You can read stories from our team members [here](https://stories.fylehq.com/).

## Challenge Outline

**You are allowed to use any online/AI tool such as ChatGPT, Gemini, etc., to complete the challenge. However, we expect you to fully understand the code and logic involved.**

This challenge involves writing a backend service for a URL Shortener. The challenge is described in detail [here](./Application.md).

## What happens next?

Once you submit the assignment, you will hear back from us within 2 working days via email.

## Installation

1. **Fork** this repository to your GitHub account.
2. **Clone** the forked repository and proceed with the steps mentioned below.

### Install Requirements

```bash
python3 -m virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Reset the Database

```bash
rm -rf url_shortener.db
```

### Start the Server

```bash
bash run.sh
```

### Run Tests

```bash
pytest -vvv -s tests/
```

---

We look forward to seeing your solution!
