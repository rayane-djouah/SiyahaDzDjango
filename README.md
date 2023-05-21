# SiyahaDZ API

This repository contains the API implementation for SiyahaDZ, a travel promting in Algeria application.

## Description

SiyahaDZ is a web-based application that provides information about various points of interest, events, cities, and regions in Algeria. The API serves as the backend for the application, allowing clients to interact with the data stored in the system.

The API is built using Django and Django REST Framework, providing a RESTful interface for accessing and manipulating the resources. It follows common RESTful design principles and includes authentication and permission handling.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/rayane-djouah/SiyahaDzDjango.git

   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt

   ```

3. Set up the environment variables.

Create a .env file in the project root directory and define the required environment variables. For example:

```plaintext
DB_ENGINE=django.db.backends.your-database-management-system
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password#
DB_HOST=your-database-host
DB_PORT=your-database-port
```

4. Set up the database:

```shell

python manage.py migrate

```

5. Start the development server:

```shell

 python manage.py runserver

```

The API will be accessible at http://localhost:8000/.

## API Documentation

The API provides comprehensive documentation using Swagger. You can access the API documentation by visiting the Swagger UI at http://localhost:8000/swagger/.

## Usage

The API supports various endpoints for managing points of interest, events, cities, regions, and other related entities. Here are some of the main endpoints:

```plaintext
/regions/: Retrieve a list of all regions or create a new region.
/regions/<region_id>/: Retrieve, update, or delete a specific region.
/cities/: Retrieve a list of all cities or create a new city.
/cities/<city_id>/: Retrieve, update, or delete a specific city.
/points-of-interest/: Retrieve a list of all points of interest or create a new point of interest.
/points-of-interest/<poi_id>/: Retrieve, update, or delete a specific point of interest.
...
```

Refer to the API documentation for detailed information on each endpoint, including request and response formats.

## Contributing

Contributions to the SiyahaDZ API are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request. Make sure to follow the existing coding style and guidelines.

## License

This project is licensed under the MIT License.
