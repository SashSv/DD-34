from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import ArticleForm
from .models import Article
import datetime
from .filters import ArticleFilter

class ArticleList(ListView):
    model = Article  # указываем модель, объекты которой мы будем выводить
    template_name = 'all_news.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'all_news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    ordering = ['-datetime']
    paginate_by = 3
    form_class = ArticleForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow()  # добавим переменную текущей даты time_now
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['form'] = ArticleForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)

class OneArticlelDetail(DetailView):
    model = Article  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'one_news.html'  # название шаблона будет product.html
    context_object_name = 'one_news'  # название объекта. в нём будет

class SearchArticleList(ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

class AddArticleList(ListView):
    model = Article
    template_name = 'add.html'
    form_class = ArticleForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ArticleForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)

class UpdateArticleView(UpdateView):
    template_name = 'add.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)

class DelArticleView(DeleteView):
    template_name = 'delete.html'
    queryset = Article.objects.all()
    success_url = '/news/'