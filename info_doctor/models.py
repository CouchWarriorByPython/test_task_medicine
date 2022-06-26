from django.db import models


class LineOfAction(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'LineOfAction'
        verbose_name_plural = 'LineOfAction'
        ordering = ['title']

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    work_experience = models.PositiveSmallIntegerField(blank=True, null=True)
    line_of_action = models.ManyToManyField(LineOfAction, related_name='doctor_info',
                                            help_text="Select a line of action for this doctor")

    objects = models.Manager()

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['name', 'id']

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'

    def display_line_of_action(self):
        """
        Creates a string for the LineOfAction. This is required to display line_of_action in Admin.
        """
        lst_query = self.line_of_action.all()
        if len(lst_query) >= 3:
            return f'{", ".join([action.title for action in lst_query[:2]])}, ...'
        return ', '.join([action.title for action in lst_query.all()])

    display_line_of_action.short_description = 'Line of Action'

    def full_name(self):
        return f'{self.name} {self.surname} {self.patronymic}'
