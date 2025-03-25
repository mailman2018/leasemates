# LeaseMates Backend

LeaseMates is a comprehensive property management platform that connects landlords and tenants, streamlining the rental experience through integrated payment processing, communication tools, and maintenance request management.

## Features

### For Tenants
- Submit and track maintenance requests with priority levels
- Direct communication with landlords
- View and respond to property announcements
- Track payment history and upcoming payments

### For Landlords
- Manage multiple properties and tenants
- Process maintenance requests with status tracking
- Send announcements to tenants
- Handle tenant communications
- Track payment collections

## Tech Stack

- **Backend Framework**: Django 5.1.3
- **API**: Django REST Framework with JWT Authentication
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **CORS**: django-cors-headers
- **Documentation**: drf-yasg (Yet Another Swagger Generator)

## Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package manager)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mailman2018/leasemates.git
   cd leasemates
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv lease_mates_env
   source lease_mates_env/bin/activate  # On Windows: lease_mates_env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   Create a `.env` file in the root directory with the following variables:
   ```env
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   ```

5. **Database Setup**
   - Create a PostgreSQL database
   - Update the database credentials in your `.env` file

6. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## API Documentation

The API documentation is available at:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

### Authentication Endpoints

- `POST /api/token/` - Get JWT token
- `POST /api/token/refresh/` - Refresh JWT token

### Maintenance Endpoints

- `GET /api/maintenance/` - List all maintenance requests
- `POST /api/maintenance/` - Create new maintenance request
- `GET /api/maintenance/{id}/` - Get specific maintenance request
- `PUT /api/maintenance/{id}/` - Update maintenance request
- `DELETE /api/maintenance/{id}/` - Delete maintenance request

### Communication Endpoints

- `GET /api/messages/` - List all messages
- `POST /api/messages/` - Send new message
- `GET /api/announcements/` - List all announcements
- `POST /api/announcements/` - Create new announcement

## Testing

1. **Run Tests**
   ```bash
   python manage.py test
   ```

2. **Run Tests with Coverage**
   ```bash
   coverage run manage.py test
   coverage report
   ```

## Development Guidelines

1. Always use environment variables for sensitive data
2. Follow PEP 8 style guide
3. Write tests for new features
4. Update documentation when making changes
5. Use meaningful commit messages

## Security Considerations

- Never commit sensitive information like API keys, passwords, or secret keys
- Use environment variables for all sensitive configuration
- Keep your dependencies up to date
- Follow Django's security best practices
- Use HTTPS in production
- Implement rate limiting for API endpoints
- Regular security audits and updates

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the development team.

## Security Policy

Please report any security vulnerabilities to security@yourdomain.com. Do not create public issues for security-related concerns.
