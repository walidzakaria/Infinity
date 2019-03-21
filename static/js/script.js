const min = 300;
const max = 3600;
const mainmin = 200;
let sidebarWidth = 280;
let shownSidebar = true;
$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        //$('#sidebar').toggleClass('active');
        if (shownSidebar) {
            $('#sidebar').css("margin-left", -sidebarWidth);
            $('.main').css("left", 0);
            shownSidebar = false;
        } else {
            $('#sidebar').css("margin-left", 0);
            $('.main').css("left", sidebarWidth);
            shownSidebar = true;
        };
    });

    $('#split-bar').mousedown(function(e) {
        e.preventDefault();
        $(document).mousemove(function(e) {
            e.preventDefault();
            let x = e.pageX - $('#sidebar').offset().left;
            if (x > min && x < max && e.pageX < ($(window).width() - mainmin)) {
                $('#sidebar').css("min-width", x);
                $('.main').css("left", x);
                sidebarWidth = x
            }
        })
    });
    $(document).mouseup(function(e) {
        $(document).unbind('mousemove');
    });

    $(window).resize(function() {
        if ($(window).width() < 768) {
            $('#sidebar').css("margin-left", -sidebarWidth);
            $('.main').css("left", 0);
            shownSidebar = false;
        } else {
            $('#sidebar').css("margin-left", 0);
            $('.main').css("left", sidebarWidth);
            shownSidebar = true;
        }
    });

    $(".table-row").click(function() {
        window.document.location = $(this).data("href");
        //alert($(this).data("href"));
    });

    $('.search-result').on('click', function() {
        $('.search-result').removeClass('active');
        $(this).addClass('active');
    })

    $('#country').on('change', function(){
        fillRegions($(this).val());
    })

    $('#region').on('change', function(){
        fillCities($(this).val());
    })
});


function fillRegions(countryId) {
    $('#region').val('');
    $('#city').val('');
    $.ajax({
        type: "GET",
        url: "/api/region/"+countryId+"/",
        dataType: "json",
        success: function(response) {
            $('#region').text('');
            $('#region').append(new Option("Select...", "", true, false));
            $.each(response, function (index, region) {
                $('#region').append(new Option(region.region, region.region_id, false, false));
            });
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function fillCities(regionId) {
    $('#region').val('');
    $('#city').val('');
    $.ajax({
        type: "GET",
        url: "/api/city/"+regionId+"/",
        dataType: "json",
        success: function(response) {
            $('#city').text('');
            $('#city').append(new Option("Select...", "", true, false));
            $.each(response, function (index, city) {
                $('#city').append(new Option(city.city, city.city_id, false, false));
            });
        },
        error: function(error) {
            console.log(error);
        }
    });
}
