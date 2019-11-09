$(document).ready(function() {
    $('#places').DataTable( {
        "ajax": "../places/getPlaces",
        "columns": [
            { "data": "name" },
            { "data": "country" },
            { "data": "city" }
        ],
        "deferRender": true,
        "columnDefs": [
            {
                // The `data` parameter refers to the data for the cell (defined by the
                // `data` option, which defaults to the column being worked with, in
                // this case `data: 0`.
                "render": function ( data, type, row ) {
                    return "<a href='../admin/edit_place/" + row.id + "'> Редактировать   </a>" + 
                    "<a href='../admin/delete_place/" + row.id + "'> Удалить </a>";
                },
                "targets": 3
            }
        ]
    } );
} );

