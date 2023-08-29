# Movie Search Backend

## Project Overview

**Movie Search Backend** is the backend implementation of a movie search tool that enables users to find movies based on their queries. The movie data is fetched from the provided endpoint: [Movie Data Endpoint](https://august12-uqf7jaf6ua-ew.a.run.app/docs).

## Key Achievements

- Developed an API that allows users to send custom queries to a third-party server and retrieve paginated results with convenient navigation using links to previous and next pages. 
The basic user request should include parameters in the URL, such as offset (default: 0), limit (default: 10), and query (default: 0). Automatic reconnection to the server was implemented to address its intermittent behavior.

- Implemented user authentication using Django Rest Framework and JSON Web Tokens (JWT) for enhanced security. To ensure account activation, users are required to verify their email addresses through email verification.

- Email notifications for account activations use the Google SMTP service and are managed asynchronously using Celery and Redis.

- Customized error handling was implemented to improve the user experience.

- The API endpoints of the movie search service are thoroughly documented using Swagger. This documentation provides a clear and interactive overview of the available endpoints, request parameters, response formats, and authentication requirements.

- The project has been encapsulated within a Docker Compose configuration, simplifying the setup process. Docker Compose allows for the orchestration of multiple containers, making it effortless to launch the entire application stack with a single command.


## Time Frame

This project was completed in approximately 4 hours. While the core functionality is implemented, there is always room for further enhancements and optimizations.

## Potential Improvements

Given additional time, the following improvements could be made:

- **Caching with Redis**: Implement data caching from the external service in Redis to reduce the frequency of external API calls. Responses to user queries could be served from the Redis cache instead of making a request to the external service every time.

- **User Profiles and Recommendations**: Create user profiles to store the list of movies they've rated. Analyzing this data could lead to better-ordered search results based on user preferences. Additionally, user actions such as requests, model interactions, clicks, and page views could be logged or tracked to improve future recommendations and user experience.

- **Testing**: Write unit and integration tests for the system to ensure its reliability. This could involve simulating API interactions (using mocking) and validating responses.

- **Advanced Analytics**: Utilize user interaction data for advanced analytics, such as identifying trending movies, generating personalized recommendations, and enhancing the overall user experience.

## Deployment

To deliver this service to the end user it is needed to deploy application to cloud server. I've already integratedDocker, that provides a consistent environment across different stages of development and deployment, ensuring that the application runs reliably regardless of the hosting environment. With Docker already integrated into the project, deploying the application to cloud platforms such as AWS, Google Cloud, or Heroku becomes notably simplified. This approach minimizes potential compatibility issues and accelerates the process of setting up and launching the service in various cloud environments.

## Architecture and Technologies

- Python: The primary programming language.
- PostgreSQL: Used to store user profiles.
- Django: Framework for easing API development.
- Django Rest Framework: Enhanced tools for building APIs.
- Celery: Asynchronous task processing, used for email sending.
- Redis: Data caching and task management.
- Redis Admin, Celery Beat, Flower, and Postgres Admin: Tools for managing processes.
- Gunicorn: Application server for deploying the application.
- Docker and Docker Compose: For containerization and easy deployment.

## Requirements

- Ensure Docker and Docker Compose are installed.

## Getting Started

To run the application:

1. Clone [this repository](https://github.com/polinamalyhina/movie_search.git)
2. Navigate to the project directory: cd movie_search
3. Add the .env file
4. Build and run the Docker containers using `docker-compose up --build`

For communicating with the application, I recommend using tools like Postman.

## Use of AI Tools

During the development of the application, I utilized AI tools like ChatGPT for identifying mechanical errors and or as a tool for quick search of the right information. AI tools can be valuable aids for developers, assisting in error detection, providing improvements, and expediting development processes, but the results should be carefully checked. However, data security must always be a consideration when using AI tools.
