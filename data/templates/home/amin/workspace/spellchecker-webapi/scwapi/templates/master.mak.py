# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1458050639.7980063
_enable_loop = True
_template_filename = '/home/amin/workspace/spellchecker-webapi/scwapi/templates/master.mak'
_template_uri = '/home/amin/workspace/spellchecker-webapi/scwapi/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['footer', 'main_menu', 'content_wrapper', 'head_content', 'meta', 'title', 'body_class']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer('\n    <title>')
        __M_writer(escape(self.title()))
        __M_writer('</title>\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer('" />\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer('" />\n    ')
        __M_writer(escape(self.head_content()))
        __M_writer('\n</head>\n<body class="')
        __M_writer(escape(self.body_class()))
        __M_writer('">\n    ')
        __M_writer(escape(self.main_menu()))
        __M_writer('\n  <div class="container-fluid">\n    ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\n  </div>\n    ')
        __M_writer(escape(self.footer()))
        __M_writer('\n\n    <script src="http://code.jquery.com/jquery.js"></script>\n    <script src="')
        __M_writer(escape(tg.url('/javascript/bootstrap.min.js')))
        __M_writer('"></script>\n</body>\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        h = context.get('h', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <footer class="footer hidden-xs hidden-sm">\n    <a class="pull-right" href="http://www.turbogears.org"><img style="vertical-align:middle;" src="')
        __M_writer(escape(tg.url('/img/under_the_hood_blue.png')))
        __M_writer('" alt="TurboGears 2" /></a>\n    <p>Copyright &copy; ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'TurboGears2')))
        __M_writer(' ')
        __M_writer(escape(h.current_year()))
        __M_writer('</p>\n  </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        page = context.get('page', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- Navbar -->\n  <nav class="navbar navbar-default">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">\n        <img src="')
        __M_writer(escape(tg.url('/img/turbogears_logo.png')))
        __M_writer('" height="20" alt="TurboGears 2"/>\n        ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'turbogears2')))
        __M_writer('\n      </a>\n    </div>\n\n    <div class="collapse navbar-collapse" id="navbar-content">\n      <ul class="nav navbar-nav">\n        <li class="')
        __M_writer(escape(('', 'active')[page=='index']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">Welcome</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='about']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/about')))
        __M_writer('">About</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='data']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/data')))
        __M_writer('">Serving Data</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='environ']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/environ')))
        __M_writer('">WSGI Environment</a></li>\n      </ul>\n\n')
        if tg.auth_stack_enabled:
            __M_writer('      <ul class="nav navbar-nav navbar-right">\n')
            if not request.identity:
                __M_writer('        <li><a href="')
                __M_writer(escape(tg.url('/login')))
                __M_writer('">Login</a></li>\n')
            else:
                __M_writer('        <li><a href="')
                __M_writer(escape(tg.url('/logout_handler')))
                __M_writer('">Logout</a></li>\n        <li><a href="')
                __M_writer(escape(tg.url('/admin')))
                __M_writer('">Admin</a></li>\n')
            __M_writer('      </ul>\n')
        __M_writer('    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer('\n')
        if flash:
            __M_writer('      <div class="row">\n        <div class="col-md-8 col-md-offset-2">\n              ')
            __M_writer(flash )
            __M_writer('\n        </div>\n      </div>\n')
        __M_writer('  ')
        __M_writer(escape(self.body()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer('" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/home/amin/workspace/spellchecker-webapi/scwapi/templates/master.mak", "source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 7, "32": 7, "33": 8, "34": 8, "35": 10, "36": 10, "37": 11, "38": 11, "39": 13, "40": 13, "41": 15, "42": 15, "43": 18, "44": 18, "45": 33, "46": 35, "47": 39, "48": 40, "49": 42, "50": 49, "51": 87, "57": 44, "65": 44, "66": 46, "67": 46, "68": 47, "69": 47, "70": 47, "71": 47, "77": 51, "86": 51, "87": 61, "88": 61, "89": 62, "90": 62, "91": 63, "92": 63, "93": 69, "94": 69, "95": 69, "96": 69, "97": 70, "98": 70, "99": 70, "100": 70, "101": 71, "102": 71, "103": 71, "104": 71, "105": 72, "106": 72, "107": 72, "108": 72, "109": 75, "110": 76, "111": 77, "112": 78, "113": 78, "114": 78, "115": 79, "116": 80, "117": 80, "118": 80, "119": 81, "120": 81, "121": 83, "122": 85, "128": 21, "134": 21, "135": 22, "139": 24, "140": 25, "141": 26, "142": 28, "143": 28, "144": 32, "145": 32, "146": 32, "152": 40, "161": 36, "166": 36, "167": 37, "168": 37, "174": 42, "178": 42, "184": 35, "193": 184}, "filename": "/home/amin/workspace/spellchecker-webapi/scwapi/templates/master.mak"}
__M_END_METADATA
"""
