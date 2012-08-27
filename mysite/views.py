# -*- coding: utf-8 -*-
from annoying.decorators import render_to

@render_to('test.html')
def test(request):
    return {'message': "The site is working"}