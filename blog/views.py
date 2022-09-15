from django.views import generic
from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "blog/index.html"
    # ここでの変数名は親クラスのプロパティでありそれを上書きしているイメージのため変更不可

class InquiryView(generic.FormView):
    template_name = "blog/inquiry.html"
    form_class = InquiryForm
