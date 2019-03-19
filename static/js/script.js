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
});
