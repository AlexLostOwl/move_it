$(document).ready(function() {
    $('#cities').DataTable( {
        "ajax": "../countries/getCountries",
        "columns": [
            { "data": "country" }
        ],
        "deferRender": true,
        "columnDefs": [
            {
                // The `data` parameter refers to the data for the cell (defined by the
                // `data` option, which defaults to the column being worked with, in
                // this case `data: 0`.
                "render": function ( data, type, row ) {
                    return "<a href='../admin/edit_country/" + row.id + "'> Редактировать </a>" +
                    "<a href='../admin/delete_country/" + row.id + "'> Удалить </a>";
                },
                "targets": 1
            }
        ]
    } );
} );

