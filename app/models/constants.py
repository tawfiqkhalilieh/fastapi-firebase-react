from fastapi.security import APIKeyHeader

collection: str = "users"
api_key_header = APIKeyHeader(name='X-API-Key', auto_error=True)
api_key: str = 'tawfiq'