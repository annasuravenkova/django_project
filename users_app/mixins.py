from django.core.exceptions import PermissionDenied

class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.author:
            raise PermissionDenied("Редактировать может только автор статьи")
        return super().dispatch(request, *args, **kwargs)
