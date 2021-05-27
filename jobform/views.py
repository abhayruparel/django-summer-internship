from django.shortcuts import render
from django.http import HttpResponse
from .forms import JobApplicationForm
# Create your views here.


def jobForm(request):

	form = JobApplicationForm()

	if request.method == 'POST':
		form = JobApplicationForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request, 'mainForm.html', context)


