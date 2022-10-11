$(document).ready(function() {

    $("#owl-news").owlCarousel({
        slideSpeed : 300,
        paginationSpeed : 400,
        nav : false,
        loop : true,
        dots : true,
        dotsData : true,
        items : 2, 
        itemsDesktop : false,
        itemsDesktopSmall : false,
        itemsTablet: false,
        itemsMobile : false,
        dotsClass : 'cl_dots'

    });

    $("#owl-years").owlCarousel({
        margin: 10,
        slideSpeed : 300,
        paginationSpeed : 400,
        nav : false,
        dots : true,
        dotsData : true,
        items : 1, 
        itemsDesktop : false,
        itemsDesktopSmall : false,
        itemsTablet: false,
        itemsMobile : false,
        dotsClass : 'cl_dots'
   
    });
 
    $("#owl-photos").owlCarousel({
        smartSpeed : 2000,
        slideSpeed : 2000,
        paginationSpeed : 400,
        nav : false,
        dots : false,
        dotsData : false,
        autoplay : true,
        autoplayTimeout : 5000,
        loop : true,
        items : 1, 
        itemsDesktop : false,
        itemsDesktopSmall : false,
        itemsTablet: false,
        itemsMobile : false
   
    });
 
    $("#owl-quotes").owlCarousel({
        margin : 100,
        slideSpeed : 300,
        paginationSpeed : 400,
        nav : false,
        dots : true,
        dotsData : true,
        items : 1, 
        itemsDesktop : false,
        itemsDesktopSmall : false,
        itemsTablet: false,
        itemsMobile : false,
        dotsClass : 'cl_dots'
   
    });
   
});