<%inherit file="local:templates.master"/>

<script src="${tg.url('/lib/ckeditor/ckeditor.js')}"></script>
<div class="row">
    <div class="col-xs-12">
        <textarea id="editorlocal"></textarea>
    </div>
</div>

<script type="text/javascript">
    CKEDITOR.replace('editorlocal', {
        scayt_serviceProtocol: 'http',
		scayt_serviceHost: '${server_host}',
		scayt_servicePort: '${server_port}',
		scayt_servicePath: 'scayt/ssrv.json',
		scayt_customerId: '',
        scayt_srcUrl: '/lib/ckscayt/ckscayt.js',
        scayt_autoStartup: true
    });
    CKEDITOR.config.scayt_sLang= 'fa_IR';

    var editor = editor = CKEDITOR.instances.editorlocal;
           editor.on( 'instanceReady', function() {

               editor.addCommand("add_to_dictionary", {
                    exec : function(e)
                    {
        CKEDITOR.instances.editorlocal.updateElement();
                        text = e._.selectionPreviousPath.elements[0].$.innerText;
                        alert(text);
        $.ajax({
            type: "POST",
            url: "http://localhost:8085/scayt/ssrv.json?cmd=add_to_dictionary&text=" + text,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8'
        });
    }});

               var add_to_dictionary = {
               label : 'ADDD',
               command : 'add_to_dictionary',
               group : 'scayt_control'
            };

              editor.contextMenu.addListener( function() {
               return {
                  myCommand : CKEDITOR.TRISTATE_OFF
               };
            });

            editor.addMenuItems({
               myCommand : {
                  label : 'افزودن به دیکشنری',
                  command : 'add_to_dictionary',
                  group : 'scayt_control',
                  order : 1
               }});
});

</script>
