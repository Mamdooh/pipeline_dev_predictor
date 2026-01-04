from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_magic8ball_answer


def predict(request):
    """
    Handle magic 8-ball predictions.
    GET: Display form
    POST: Return prediction based on question hash
    """
    context = {
        'title': 'Magic 8-Ball',
        'answer': None,
        'question': None,
    }

    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        if question:
            answer = get_magic8ball_answer(question)
            context['answer'] = answer
            context['question'] = question

    return render(request, 'magic8ball/predict.html', context)


def health(request):
    """
    Health check endpoint.
    """
    return JsonResponse({
        'status': 'ok'
    })
