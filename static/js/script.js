const min = 300;
const max = 3600;
const mainmin = 200;
let sidebarWidth = 280;
let shownSidebar = true;
$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
        
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

    $('#search-list').on('click', '.search-result', function() {
        alert('w');
        $('.search-result').removeClass('active');
        $(this).addClass('active');
    })
    
    var searchApp = new Vue({
        el: '#search-container',
        delimiters: ['{', '}'],
        data: {
            search: '',
            hotels: []
        },
        mounted: function() {
            this.hotels= [];
        },
        methods: {
            getHotels: function() {
                $('.search-result').removeClass('active');
                var searchInput = this.search;

                searchInput = $.trim(searchInput);
                searchInput = searchInput.replace(' ', '+');
                

                if (!searchInput) {
                   this.hotels = [];
                    return;
                }
                this.$http.get('/hotel/search/'+searchInput+'/')
                    .then((response) => {
                    this.hotels = response.data;
                    })
                    .catch((err) => {
                        this.hotels= [];
                    console.log(err);
                })
            },
            setClicked: function(object) {
                var currentId = object.srcElement.id;
                GetSelected(currentId);
            }
    }})


    var appPlaces = new Vue({
        el: '#places',
        delimiters: ['{', '}'],
        data: {
            currentCountry: '',
            regions: [],
            cities: []
        },
        methods: {
            getRegions: function() {

            },
            getCities: function() {

            }
        }
    })
    
});

function GetSelected(objectId) {
    $('.search-result').removeClass('active');
    $('#'+objectId).addClass('active');
}

//function fillRegions(countryId) {
//    $('#region').val('');
//    $('#city').val('');
//    $.ajax({
//        type: "GET",
//        url: "/api/region/"+countryId+"/",
//        dataType: "json",
//        success: function(response) {
//            $('#region').text('');
//            $('#region').append(new Option("Select...", "", true, false));
//            $.each(response, function (index, region) {
//                $('#region').append(new Option(region.region, region.region_id, false, false));
//            });
//        },
//        error: function(error) {
//            console.log(error);
//        }
//    });
//}

//function fillCities(regionId) {
//    $('#city').val('');
 //   $.ajax({
   //     type: "GET",
    //    url: "/api/city/"+regionId+"/",
 //       dataType: "json",
      //  success: function(response) {
   //         $('#city').text('');
     //       $('#city').append(new Option("Select...", "", true, false));
       //     $.each(response, function (index, city) {
         //       $('#city').append(new Option(city.city, city.city_id, false, false));
           // });
   //     },
   //     error: function(error) {
    //        console.log(error);
     //   }
 //   });
//}

//function searchHotels(searchText) {
//    searchText = $.trim(searchText);
//    searchText = searchText.replace(' ', '+');
//    $('.search-result').remove();

//    if (searchText == '') {
//        return;
//    }

//    $.ajax({
//        type: "GET",
//        url: "/hotel/search/"+searchText+"/",
//        dataType: "json",
//        success: function(response) {
//            for (item of response) {
//                $('#search-list').prepend('<li id="'+item.hotel_id+'" class="search-result">'+item.hotel_code+'; '+item.hotel+'</li>');
//            }
//        },
//        error: function(error) {
//            console.log(error);
//        }
//    });
//}
