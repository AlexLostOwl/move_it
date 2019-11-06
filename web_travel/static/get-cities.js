$(document).ready(function(){
    console.log(2)
    const getAjax = (country) => {
        console.log(4)
        $.ajax({
            type: 'GET',
            url: "../country/getCities",
            data: { country: country},
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
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

    if ($(this).val() != 'default') {
        var country = $(this).find('option:selected').text();
        console.log(3)

        getAjax(country)
    }

    $("select#countriesSelect").change(function() {

        if ($(this).val() != 'default') {

            var country = $(this).find('option:selected').text();
            console.log(1)
            getAjax(country);
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
