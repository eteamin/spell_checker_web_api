<%inherit file="local:templates.master"/>

<script src="${tg.url('/lib/ckeditor/ckeditor.js')}"></script>

<div class="row">
    <div class="col-xs-12">
        <textarea id="editorLocal">
            local
        </textarea>
    </div>
</div>

<script type="text/javascript">
    CKEDITOR.replace('editorLocal', {
        scayt_serviceProtocol: 'http',
		scayt_serviceHost: '192.168.1.2',
		scayt_servicePort: 7575,
		scayt_servicePath: 'scayt/ssrv.json',
		scayt_customerId: '',
        scayt_srcUrl: '/lib/ckscayt/ckscayt.js',
        scayt_autoStartup: true
    });
             CKEDITOR.config.scayt_sLang= 'fa_IR'
</script>
