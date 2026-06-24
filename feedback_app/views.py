from django.urls import reverse_lazy

from feedback_app.forms import FeedbackForm
from feedback_app.models import Feedback
from django.views.generic import FormView, TemplateView

# def feedback_view(request):
#     if request.method == 'POST':
#         form  = FeedbackForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#             email = form.cleaned_data.get('email')
#             message = form.cleaned_data.get('message')
#             subject = form.cleaned_data.get('subject')
#             Feedback.objects.create(
#                 name=name,
#                 email=email,
#                 message=message,
#                 subject=subject
#             )
#             return redirect('feedback:feedback_success')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback_page.html', {'form':form})

class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = 'feedback/feedback_page.html'
    success_url = reverse_lazy('feedback:feedback_success')

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        subject = form.cleaned_data.get('subject')

        Feedback.objects.create(
            name=name,
            email=email,
            message=message,
            subject=subject
        )
        return super().form_valid(form)

# def feedback_success(request):
#     return render(request, 'success.html')


class FeedbackSuccessView(TemplateView):
    template_name = 'feedback/success.html'
