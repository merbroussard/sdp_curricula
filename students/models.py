from django.db import models
from datetime import datetime
from schools.models import School
from curricula.models import GradeCurriculum


class Grade(models.Model):
    school = models.ForeignKey(School)
    grade_level = models.IntegerField()
    likely_math_curriculum = models.ForeignKey(GradeCurriculum, blank=True, null=True, related_name='school_math')
    likely_reading_curriculum = models.ForeignKey(GradeCurriculum, blank=True, null=True, related_name='school_reading')

    """
        Define shortfalls as dynamic methods so they update
        when inventory is updated
    """
    def math_shortfall(self):
        pass

    def reading_shortfall(self):
        pass

    def __unicode__(self):
        return "%s, Grade %s" % (self.school.name, self.grade_level)

    def human_grade(self):
        if self.grade_level == 0:
            return 'K'
        elif self.grade_level == -1:
            return 'Pre-K'
        else:
            return self.grade_level


class Cohort(models.Model):
    YEARS = []

    for r in range(2008, (datetime.now().year + 1)):
        YEARS.append((r, r))

    grade = models.ForeignKey(Grade)
    # Cohort year, ex. 2008-2009
    year_start = models.IntegerField(max_length=4, choices=YEARS)
    year_end = models.IntegerField(max_length=4, choices=YEARS)

    # PSSA Scores
    math_advanced_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_proficient_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_below_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_advanced_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_proficient_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_below_basic_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    math_combined_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    read_combined_percent = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)

    # Number of students in the grade for that year
    number_of_students = models.PositiveIntegerField(blank=True, null=True)

    # Associated grade curriculum for the cohort
    associated_reading_curriculum = models.ManyToManyField(GradeCurriculum, related_name="reading_cohort", null=True)
    associated_math_curriculum = models.ManyToManyField(GradeCurriculum, related_name="math_cohort", null=True)
