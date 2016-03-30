# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458135396.9902704
_enable_loop = True
_template_filename = '/home/amin/workspace/spellchecker-webapi/scwapi/templates/index.mak'
_template_uri = '/home/amin/workspace/spellchecker-webapi/scwapi/templates/index.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


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
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<script src="')
        __M_writer(escape(tg.url('/lib/ckeditor/ckeditor.js')))
        __M_writer('"></script>\n\n<div class="row">\n    <div class="col-xs-12">\n        <textarea id="editorOriginal">\n            original\n        </textarea>\n   </div>\n</div>\n\n<script type="text/javascript">\n    CKEDITOR.replace(\'editorOriginal\', {\n        language : \'en\',\n        scayt_autoStartup: true\n    });\n\n        CKEDITOR.config.scayt_sLang= \'de_DE\'\n\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/home/amin/workspace/spellchecker-webapi/scwapi/templates/index.mak", "source_encoding": "utf-8", "filename": "/home/amin/workspace/spellchecker-webapi/scwapi/templates/index.mak", "line_map": {"36": 3, "34": 1, "35": 3, "28": 0, "42": 36}}
__M_END_METADATA
"""
