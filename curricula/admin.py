from django.contrib import admin
from django import forms
from .models import PublisherGroup, Publisher, LearningMaterial, Curriculum, GradeCurriculum

admin.site.register(PublisherGroup)

admin.site.register(Publisher)

class LearningMaterialAdmin(admin.ModelAdmin):
    readonly_fields = ('publisher',)

admin.site.register(LearningMaterial, LearningMaterialAdmin)

admin.site.register(Curriculum)

class GradeCurriculumAdminForm(forms.ModelForm):
  class Meta:
    model = GradeCurriculum

  def __init__(self, *args, **kwargs):
    super(GradeCurriculumAdminForm, self).__init__(*args, **kwargs)
    if self.instance.id:
        self.fields['necessary_materials'].queryset = self.instance.materials.all()

class GradeCurriculumAdmin(admin.ModelAdmin):
    form = GradeCurriculumAdminForm

admin.site.register(GradeCurriculum, GradeCurriculumAdmin)