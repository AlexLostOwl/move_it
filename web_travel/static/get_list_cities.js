$(document).ready(function() {
    $('#cities').DataTable( {
        "ajax": "../cities/getCities",
        "columns": [
            { "data": "city" },
            { "data": "country" },
        ],
        "deferRender": true,
        "columnDefs": [
            {
                // The `data` parameter refers to the data for the cell (defined by the
                // `data` option, which defaults to the column being worked with, in
                // this case `data: 0`.
                "render": function ( data, type, row ) {
                    return "<a href='../admin/edit_city/" + row.id + "'> Редактировать </a>" +
                    "<a href='../admin/delete_city/" + row.id + "'> Удалить </a>";
                },
                "targets": 2
            }
        ]
    } );
} );

