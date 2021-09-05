# Jungle Devs - Django Challenge #001

## Installation
1. Install Docker and Docker Compose.
2. Clone this repository:
```bash
git clone https://github.com/heytorvas/django-challenge-001.git
```
3. Change directory to repository:
```bash
cd django-challenge-001
```
### Development Environment
1. Build the containers:
```bash
docker-compose build &
```
2. Up the containers:
```bash
docker-compose up db_dev &
docker-compose up api_dev &
```
3. It's possible up pgadmin container, if you want:
```bash
docker-compose up pgadmin_dev &
```
### Production Environment
1. Build the containers:
```bash
docker-compose -f docker-compose-prod.yml build &
```
2. Up the containers:
```bash
docker-compose -f docker-compose-prod.yml up db_prod &
docker-compose -f docker-compose-prod.yml up api_prod &
docker-compose -f docker-compose-prod.yml up nginx &
```
3. It's possible up pgadmin container, if you want:
```bash
docker-compose -f docker-compose-prod.yml up pgadmin_prod &
```
### Notes
- API Documentation is located on: ```http://localhost:8000/api/docs/```

## Description

**Challenge goal**: The purpose of this challenge is to give an overall understanding of a backend application. You’ll be implementing a simplified version of a news provider API. The concepts that you’re going to apply are:

- REST architecture;
- Authentication and permissions;
- Data modeling and migrations;
- PostgreSQL database;
- Query optimization;
- Serialization;
- Production builds (using Docker).

**Target level**: This is an all around challenge that cover both juniors and experience devs based on the depth of how the concepts were applied.

**Final accomplishment**: By the end of this challenge you’ll have a production ready API.

## Acceptance criteria

- Clear instructions on how to run the application in development mode
- Clear instructions on how to run the application in a Docker container for production
- A good API documentation or collection
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`
- List article endpoint `/api/articles/?category=:slug` with the following response:
```json
[
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "picture": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  },
  ...
]
```
- Article detail endpoint `/api/articles/:id/` with different responses for anonymous and logged users:

    **Anonymous**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>"
    }
    ```

    **Logged user**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>",
      "body": "<div><p>Second paragraph</p><p>Third paragraph</p></div>"
    }
    ```
