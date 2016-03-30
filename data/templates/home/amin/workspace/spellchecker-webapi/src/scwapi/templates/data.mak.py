# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457956449.3916435
_enable_loop = True
_template_filename = '/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/data.mak'
_template_uri = '/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/data.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        params = context.get('params', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n  <div class="row">\n    <div class="col-md-6">\n      <h2>Content Type Dispatch</h2>\n        <p>\n          This page shows how you can provide multiple pages\n          directly from the same controller method.  This page is generated\n          from the expose decorator with the template defintion provided.\n          You can provide a url with parameters and this page will display\n          the parameters as html, and the json version will express\n          the entries as <code>JSON</code>.\n        </p>\n\n        <p>Click here for the <a href="')
        __M_writer(escape(tg.url('/data.json', params=params)))
        __M_writer('">JSON Version of this page.</a></p>\n    </div>\n    <div class="col-md-6">\n      <p>The data provided in the template call is:\n        <table class="table table-bordered table-striped">\n          <thead>\n            <tr>\n              <th>Key</th>\n              <th>Value</th>\n            </tr>\n          </thead>\n          <tbody>\n')
        for key, value in params.items():
            __M_writer('                <tr>\n                    <td>')
            __M_writer(escape(key))
            __M_writer('</td>\n                    <td>')
            __M_writer(escape(value))
            __M_writer('</td>\n                </tr>\n')
        __M_writer('          </tbody>\n        </table>\n      </p>\n    </div>\n  </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  Welcome to TurboGears 2.3, standing on the shoulders of giants, since 2007\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/data.mak", "line_map": {"35": 1, "36": 5, "37": 19, "38": 19, "39": 31, "40": 32, "41": 33, "42": 33, "43": 34, "44": 34, "45": 37, "51": 3, "55": 3, "28": 0, "61": 55}, "uri": "/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/data.mak"}
__M_END_METADATA
"""
