$(document).ready(function(){
    console.log(1)
    if ($(this).val() != 'default') {
        console.log(2)
        var Country = $(this).find('option:selected').text();

        $.ajax({
            type: 'GET',
            url: "../country/getCities",
            data: { country: Country},
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                console.log(response)
                let options = [];
                const first_option = '<option value="" selected>Выберите из списка</option>'
                options.push(first_option)
                if (response.cities.length == 0){
                    $('select#citiesSelect').html(first_option);
                    $('#groupCityInput').hide();
                }

                else{
                    for (var i=0, l=response.cities.length; i<l; i++){
                        options.push('<option>'+response.cities[i]+'</option>');
                    }
                    
                    
                    $('select#citiesSelect').html(options.join(''));

                    $('#groupCityInput').show();
                }

            }
        });
    }

    $("select#countriesSelect").change(function() {

        if ($(this).val() != 'default') {

            var Country = $(this).find('option:selected').text();

            $.ajax({
                type: 'GET',
                url: "../country/getCities",
                data: { country: Country},
                contentType: 'application/json',
                dataType: 'json',
                success: function(response) {
                    console.log(response)
                    let options = [];
                    const first_option = '<option value="" selected>Выберите из списка</option>'
                    options.push(first_option)
                    if (response.cities.length == 0){
                        $('select#citiesSelect').html(first_option);
                        $('#groupCityInput').hide();
                    }

                    else{
                        for (var i=0, l=response.cities.length; i<l; i++){
                            options.push('<option>'+response.cities[i]+'</option>');
                        }
                        
                        
                        $('select#citiesSelect').html(options.join(''));

                        $('#groupCityInput').show();
                    }

                }
            });
        }
        else { 
            const first_option = '<option value="" disabled selected>Выберите из списка</option>'
            $('select#citiesSelect').html(first_option);
            $('#groupCityInput').hide();
        }
    });
});

function createOrChoose() {
    if (document.getElementById('country_input_method-0').checked) {
        document.getElementById('chooseLocation').style.display = '';
        document.getElementById('createLocation').style.display = 'none';
    } else {
        document.getElementById('chooseLocation').style.display = 'none';
        document.getElementById('createLocation').style.display = '';
    }
}
