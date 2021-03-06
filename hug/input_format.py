"""hug/input_formats.py

Defines the built-in Hug input_formatting handlers

Copyright (C) 2015  Timothy Edmund Crosley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

"""
import json as json_converter
import re

from hug.format import content_type

UNDERSCORE = (re.compile('(.)([A-Z][a-z]+)'), re.compile('([a-z0-9])([A-Z])'))


@content_type('application/json')
def json(body):
    return json_converter.loads(body)


def _under_score_dict(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            value = _under_score_dict(value)
        if isinstance(key, str):
            key = UNDERSCORE[1].sub(r'\1_\2', UNDERSCORE[0].sub(r'\1_\2', key)).lower()
        new_dictionary[key] = value
    return new_dictionary


def json_underscore(body):
    return _under_score_dict(json(body))
