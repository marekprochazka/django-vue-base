import abc
import json

from django.views.generic import TemplateView

from user.serializers.user import BaseUserSerializer


class BaseVueView(TemplateView, abc.ABC):
    template_name = 'base.html'

    component_name: str = None
    component_props: dict = {}

    def get_component_props(self) -> dict:
        return self.component_props

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.component_name is None:
            raise ValueError('component_name must be defined')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['component_name'] = self.component_name
        user = BaseUserSerializer(self.request.user, ).data if self.request.user.is_authenticated else None
        props = {'user': user, **self.get_component_props()}
        context['component_props'] = json.dumps(props)
        return context
