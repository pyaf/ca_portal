from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
def NoticeBooleanUpdate(request):
    if request.method == "POST" and request.is_ajax():
        msg_id = request.POST.get('msg_id')
        print msg_id
        response_data = {}
        notice = request.user.caprofile.usernotification_set.get(id=msg_id)
        notice.mark_read = True
        notice.save()

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see":"this is not working"}),
            content_type = "application/json"
        )
@login_required(login_url = "/login")
def NotificationsView(request):
    template_name = 'ca/notifications.html'
    context = context_call(request)
    return render(request, template_name, context)
