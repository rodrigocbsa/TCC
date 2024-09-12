$(function () {
  // init tooltip & popovers
  var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
  });


  // scroll top top
  var scrollTop = 0;
  $(window).scroll(function () {
      var scroll = $(window).scrollTop();
      
      if (scroll > 80) {
          if (scroll > scrollTop) {
              $('.smart-scroll').addClass('scrolling').removeClass('up');
          } else {
              $('.smart-scroll').addClass('up');
          }
      } else {
          // remove if scroll = scrollTop
          $('.smart-scroll').removeClass('scrolling').removeClass('up');
      }

      scrollTop = scroll;

      
      if (scroll >= 600) {
          $('.scroll-top').addClass('active');
      } else {
          $('.scroll-top').removeClass('active');
      }
      return false;
  });

  $('.scroll-top').click(function () {
      $('html, body').stop().animate({
          scrollTop: 0
      }, 1000);
  });

  // download
  document.getElementById('download').addEventListener('click',() => window.print());
})