import logging

from django.shortcuts import render
from django.views.decorators.http import require_GET


logger = logging.getLogger(__name__)


@require_GET
def home(request):
    """
    View for rendering the homepage.
    For now is a redirection to projects.
    """
    return render(request, 'web/home.html', {})
