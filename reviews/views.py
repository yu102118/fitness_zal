from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden


def reviews_home(request):
    reviews = Review.objects.order_by('-date_posted')
    return render(request, 'reviews/reviews_home.html', {'reviews': reviews})


class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/details_view.html'
    context_object_name = 'review'


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user or self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user and not request.user.is_superuser:
            return HttpResponseForbidden("Вы не можете редактировать этот отзыв.")
        return super().dispatch(request, *args, **kwargs)


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/news-delete.html'
    success_url = '/reviews/'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user or self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        print(f'Current user: {request.user}, Review user: {obj.user}, Is superuser: {request.user.is_superuser}')
        if (obj.user != self.request.user) and (not request.user.is_superuser):
            return HttpResponseForbidden("Вы не можете редактировать этот отзыв.")
        return super().dispatch(request, *args, **kwargs)





def create_review(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # сохраняем текущего пользователя
            review.save()
            return redirect('reviews_home')
        else:
            error = 'Форма была неверной'

    form = ReviewForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'reviews/create_review.html', data)
