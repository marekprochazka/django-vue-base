from core.views.base import BaseVueView


class ExampleView(BaseVueView):
    component_name = 'hello'
    component_props = {'msg': 'DJANGO'}
