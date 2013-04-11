from .models import Curriculum, GradeCurriculum, LearningMaterial, PublisherGroup
from django.views.generic import ListView
from django.http import HttpResponse


class LearningMaterialDetailView(ListView):

    context_object_name = "learning_material_detail"
    template_name = "learning_material_detail.html"

    def get_queryset(self):
            self.learning_material = LearningMaterial.objects.get(isbn=self.kwargs['id'])
            return self.learning_material

    def get_context_data(self, **kwargs):
        context = super(LearningMaterialDetailView, self).get_context_data(**kwargs)
        context['book_name'] = self.learning_material.title
        context['book_list'] = self.learning_material.curricula.all()
        return context


class GradeCurriculumDetailView(ListView):

    context_object_name = "curriculum_list"
    template_name = "curriculum.html"

    def get_queryset(self):
        self.curriculum = GradeCurriculum.objects.get(id=self.kwargs['id'])
        return self.curriculum

    def get_context_data(self, **kwargs):
        context = super(GradeCurriculumDetailView, self).get_context_data(**kwargs)
        return context


class CurriculumListView(ListView):

    context_object_name = "curricula"
    template_name = "curricula.html"
    model = GradeCurriculum


class IndexListView(ListView):

    template_name = "index.html"
    model = GradeCurriculum


def testing(request):
    curricula_list = Curriculum.objects.order_by('name')
    pubs = PublisherGroup.objects.all()
    output = "\n".join([c.name for c in pubs])
    return HttpResponse(output)
