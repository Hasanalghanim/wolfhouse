from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import os

@csrf_exempt
def update_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('ref') == 'refs/heads/main':  # Check if the push was to the main branch
            project_path = '/home/hasanalghanim/wolfhouse'
            # Pull the latest changes from GitHub
            subprocess.run(['git', '-C', project_path, 'pull'])
            # Collect static files
            subprocess.run(['python', os.path.join(project_path, 'manage.py'), 'collectstatic', '--noinput'])
            # Apply database migrations
            subprocess.run(['python', os.path.join(project_path, 'manage.py'), 'migrate'])
            # Reload the web app
            subprocess.run(['touch', '/var/www/hasanalghanim_pythonanywhere_com_wsgi.py'])
    return JsonResponse({'status': 'ok'})