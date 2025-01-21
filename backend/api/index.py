from app.main import handler
from http.server import BaseHTTPRequestHandler


# Vercel serverless function handler
def endpoint(request):
    return handler(request)
