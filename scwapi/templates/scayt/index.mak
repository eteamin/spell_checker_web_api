<%inherit file="local:templates.master"/>

<script src="${tg.url('/lib/ckeditor/ckeditor.js')}"></script>
<div class="row">
    <div class="col-xs-12">
        <textarea id="editorlocal"></textarea>
    </div>
    </div>
</div>

<script type="text/javascript">
            CKEDITOR.replace('editorlocal', {
                    scayt_autoStartup: true
        });
            var editor = editor = CKEDITOR.instances.editorlocal;
           editor.on( 'instanceReady', function(e) {

               editor.addCommand("myCommand", {
                    exec : function( editor )
                  {
                     alert("myCommand");
                  }});

               var myCommand = {
               label : editor.lang.image.menu,
               command : 'myCommand',
               group : 'image'
            };


              editor.contextMenu.addListener( function( element, selection ) {
               return {
                  myCommand : CKEDITOR.TRISTATE_OFF
               };
            });

            editor.addMenuItems({
               myCommand : {
                  label : editor.lang.image.menu,
                  command : 'myCommand',
                  group : 'image',
                  order : 1
               }});
           });
   </script>
</script>
