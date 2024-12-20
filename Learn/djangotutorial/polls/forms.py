from django import forms
from .models import Question
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # Tie the form to the Question model
        fields = ['question_text', 'pub_date']
