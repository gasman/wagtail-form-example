from django.shortcuts import render

from flavours.forms import FlavourSuggestionForm


def suggest(request):
    if request.method == 'POST':
        form = FlavourSuggestionForm(request.POST)
        if form.is_valid():
            flavour = form.save()
            return render(request, 'flavours/thankyou.html', {
                'flavour': flavour,
            })
    else:
        form = FlavourSuggestionForm()

    return render(request, 'flavours/suggest.html', {
        'form': form,
    })
