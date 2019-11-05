$(document).ready(function() {
    $('#example1').DataTable( {
        "ajax": "../places/getPlaces",
        "columns": [
            { "data": "name" },
            { "data": "city" },
            { "data": "country" }
        ]
    } );
} );