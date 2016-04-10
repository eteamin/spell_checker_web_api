CKEDITOR.plugins.add( 'add_to_db', {
    icons: 'add_to_db',
    init: function( editor ) {
        if ( editor.contextMenu ) {
            editor.addMenuGroup('group');
            editor.addMenuItem( 'abbrItem', {
        label: 'Edit Abbreviation',
        command: 'abbr',
        group: 'group'
    });
            editor.contextMenu.addListener( function( element ) {
        if ( element.getAscendant( 'abbr', true ) ) {
            return { abbrItem: CKEDITOR.TRISTATE_OFF };
        }
    });
}}});