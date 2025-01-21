from app.main import handler as app_handler


# Vercel serverless function handler
def handler(request):
    return app_handler(request)
