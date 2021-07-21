import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import POST, Like


@login_required
def api_POST(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    post_body = data['post_body']
    POST.objects.create(body=post_body, created_by=request.user)
    return JsonResponse({'success': True})

def api_add_likes(request):
    data = json.loads(request.body)
    post_id = data['post_id']
    if not Like.objects.filter(post_id=post_id).filter(created_by=request.user).exists():
        like = Like.objects.create(post_id=post_id,created_by=request.user)

    return JsonResponse({'success':True})
