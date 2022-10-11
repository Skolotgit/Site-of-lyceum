function findOffset(element) {
    var top = 0, left = 0;
  
    do {
      top += element.offsetTop  || 0;
      left += element.offsetLeft || 0;
      element = element.offsetParent;
    } while(element);
  
    return {
      top: top,
      left: left
    };
  }
  
  window.onscroll = function () {
    var stickyHeader = document.getElementById('sticky');
    var underHeader = document.getElementById('under_header');
    var headerOffset = findOffset(stickyHeader);
    
    window.onscroll = function() {
      // body.scrollTop is deprecated and no longer available on Firefox
      var bodyScrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  
      if (bodyScrollTop > headerOffset.top) {
        stickyHeader.classList.remove('after-fixed');
        stickyHeader.classList.add('fixed');
        underHeader.classList.add('under_header_active');
      } else {
        stickyHeader.classList.remove('fixed');
        stickyHeader.classList.add('after-fixed');
        underHeader.classList.remove('under_header_active');
      }
    };
  };