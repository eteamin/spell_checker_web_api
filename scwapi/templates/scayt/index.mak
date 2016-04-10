<%inherit file="local:templates.master"/>

<script src="${tg.url('/lib/ckeditor/ckeditor.js')}"></script>
<script src="${tg.url('/lib/ckeditor/add_word_to_dab.js')}"></script>
<div class="row">
    <div class="col-xs-12">
        <textarea id="editorLocal">
            local
        </textarea>
    </div>
</div>

<script type="text/javascript">
    CKEDITOR.replace('editorLocal', {
        scayt_autoStartup: true
    });

</script>
