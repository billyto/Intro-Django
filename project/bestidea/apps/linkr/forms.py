from bestidea.apps.linkr.models import Topic, Item
from django.forms import ModelForm

class ItemForm(ModelForm):
    class Meta:
        model = Item

class TopicForm(ModelForm):
    class Meta:
        model = Topic