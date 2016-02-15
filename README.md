# portfolio
[![Build Status](https://img.shields.io/travis/jtwp470/codecheck-1029.svg?style=flat-square)](https://travis-ci.org/jtwp470/codecheck-1029)
[![License MIT](https://img.shields.io/badge/license-mit-blue.svg?style=flat-square)](LICENSE.md)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Service URL: https://codecheck-1029.herokuapp.com

## Language & Framework

* Python (3.5.1)
* Django
* SQLite3 (on local)
* PostgreSQL (on Heroku)


## API Document
We require to implement 4 endpoints. All details of specifications are written in files with format of [api-first-spec](https://github.com/shunjikonishi/api-first-spec).

- GET /api/projects
  - Return `200 OK` status code when server succeed to get data
  - [GET /api/projects spec](./specifications/localhost/GET-api-projects.spec.js)
- POST /api/projects
  - Return `400 BadRequest` when either of title or description was empty
  - Return `200 OK` when server succeed to create new data
  - [POST /api/projects spec](./specifications/localhost/POST-api-projects.spec.js)
- GET /api/projects/:id
  - Return `200 OK` when found data
  - Return `404 NotFound` when data didn't exists
  - [GET /api/projects/:id spec](./specifications/localhost/GET-api-projects_id.spec.js)
- DELETE /api/projects/:id
  - Return `200 OK` when data was successfully deleted
  - Return `404 NofFound` when data didn't exists
  - [GET /api/projects/:id spec](./specifications/localhost/DELETE-api-projects_id.spec.js)
