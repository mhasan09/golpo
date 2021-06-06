import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import POST


@login_required
def api_POST(request):
    data = json.loads(request.body.decode('utf-8'))
    post_body = data['post_body']
    post = POST.objects.create(body=post_body, created_by= request.user)
    return JsonResponse({'success': True})
