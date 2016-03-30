<%inherit file="local:templates.master"/>

<script src="${tg.url('/lib/ckeditor/ckeditor.js')}"></script>

<div class="row">
    <div class="col-xs-12">
        <textarea id="editorOriginal">
            original
        </textarea>
   </div>
</div>

<script type="text/javascript">
    CKEDITOR.replace('editorOriginal', {
        language : 'en',
        scayt_autoStartup: true
    });

        CKEDITOR.config.scayt_sLang= 'de_DE'

</script>
