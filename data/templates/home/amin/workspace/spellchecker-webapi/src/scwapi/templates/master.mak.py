# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457956443.1847355
_enable_loop = True
_template_filename = '/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/master.mak'
_template_uri = '/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['main_menu', 'head_content', 'content_wrapper', 'meta', 'title', 'body_class', 'footer']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        __M_writer('\n  <div class="container">\n    ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\n  </div>\n    ')
        __M_writer(escape(self.footer()))
        __M_writer('\n  <script src="http://code.jquery.com/jquery.js"></script>\n  <script src="')
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


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        page = context.get('page', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
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


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
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


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/master.mak", "line_map": {"17": 0, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 7, "32": 7, "33": 8, "34": 8, "35": 10, "36": 10, "37": 11, "38": 11, "39": 13, "40": 13, "41": 15, "42": 15, "43": 17, "44": 17, "45": 32, "46": 34, "47": 38, "48": 39, "49": 41, "50": 48, "51": 86, "57": 50, "66": 50, "67": 60, "68": 60, "69": 61, "70": 61, "71": 62, "72": 62, "73": 68, "74": 68, "75": 68, "76": 68, "77": 69, "78": 69, "79": 69, "80": 69, "81": 70, "82": 70, "83": 70, "84": 70, "85": 71, "86": 71, "87": 71, "88": 71, "89": 74, "90": 75, "91": 76, "92": 77, "93": 77, "94": 77, "95": 78, "96": 79, "97": 79, "98": 79, "99": 80, "100": 80, "101": 82, "102": 84, "108": 39, "117": 20, "123": 20, "124": 21, "128": 23, "129": 24, "130": 25, "131": 27, "132": 27, "133": 31, "134": 31, "135": 31, "141": 35, "146": 35, "147": 36, "148": 36, "154": 41, "158": 41, "164": 34, "173": 43, "181": 43, "182": 45, "183": 45, "184": 46, "185": 46, "186": 46, "187": 46, "193": 187}, "uri": "/home/amin/workspace/spellchecker-webapi/src/scwapi/templates/master.mak"}
__M_END_METADATA
"""
