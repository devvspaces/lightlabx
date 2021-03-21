(function($){
  "use strict";

  var $window = $(window);

  $window.on('load', function() {
    // Preloader
    $('.loader').fadeOut();
    $('.loader-mask').delay(350).fadeOut('slow');
    initOwlCarousel();

    $window.trigger("resize");
  });


  $window.resize(function(){
    stickyNavRemove();
  });


  /* Detect Browser Size
  -------------------------------------------------------*/
  var minWidth;
  if (Modernizr.mq('(min-width: 0px)')) {
    // Browsers that support media queries
    minWidth = function (width) {
      return Modernizr.mq('(min-width: ' + width + 'px)');
    };
  }
  else {
    // Fallback for browsers that does not support media queries
    minWidth = function (width) {
      return $window.width() >= width;
    };
  }

  /* Mobile Detect
  -------------------------------------------------------*/
  if (/Android|iPhone|iPad|iPod|BlackBerry|Windows Phone/i.test(navigator.userAgent || navigator.vendor || window.opera)) {
    $("html").addClass("mobile");
  }
  else {
    $("html").removeClass("mobile");
  }

  /* IE Detect
  -------------------------------------------------------*/
  if(Function('/*@cc_on return document.documentMode===10@*/')()){ $("html").addClass("ie"); }



  /* Sticky Navigation
  -------------------------------------------------------*/
  $window.scroll(function(){

    scrollToTop();
    var $navHolder = $('.nav__holder');

    if ($window.scrollTop() > 10 & minWidth(992)) {
      $navHolder.addClass('nav__holder--sticky');
    } else {
      $navHolder.removeClass('nav__holder--sticky');
    }
    
  });


  function stickyNavRemove() {
    var $navHolder = $('.nav__holder');
    if (!minWidth(992)) {
      $navHolder.removeClass('nav--sticky');
    } else {
      $navHolder.addClass('nav--sticky');
    }
  }
  

  /* Mobile Navigation
  -------------------------------------------------------*/
  $('.nav__dropdown-trigger').on('click', function() {
    if ($(this).hasClass("active")) {
      $(this).removeClass("active");
    }
    else {
      $(this).addClass("active");
    }
  });  

  if ( $('html').hasClass('mobile') ) {
    $('body').on('click',function() {
      $('.nav__dropdown-menu').addClass('hide-dropdown');
    });

    $('.nav__dropdown').on('click', '> a', function(e) {
      e.preventDefault();
    });

    $('.nav__dropdown').on('click',function(e) {
      e.stopPropagation();
      $('.nav__dropdown-menu').removeClass('hide-dropdown');
    });
  }


  /* Material Inputs
  -------------------------------------------------------*/
  (function() {
    var $optinInput = $('.optin__input');
    $optinInput.on('blur', function() {
      if ( $(this).val() ) {
        $(this).parent('.optin__form-group').addClass('optin__form-group--active');
      } else {
        $(this).parent('.optin__form-group').removeClass('optin__form-group--active');
      }
    });
  })();

  /* Owl Carousel
  -------------------------------------------------------*/
  function initOwlCarousel(){

    /* Testimonials
    -------------------------------------------------------*/
    $("#owl-testimonials").owlCarousel({      
      center: false,
      items: 1,
      loop: true,
      nav: true,
      dots: false,
      margin: 40,
      lazyLoad: true,
      navSpeed: 500,
      navText: ['<i class="ui-arrow-left">','<i class="ui-arrow-right">'],
      responsive:{
        1200: {
          items:2
        },
        768:{
          items:2
        },
        540:{
          items:1
        }
      }
    })
  }


  /* Accordion
  -------------------------------------------------------*/
  var $accordion = $('.accordion');
  function toggleChevron(e) {
    $(e.target)
      .prev('.accordion__heading')
      .find("a")
      .toggleClass('accordion--is-open accordion--is-closed');
  }
  $accordion.on('hide.bs.collapse', toggleChevron);
  $accordion.on('show.bs.collapse', toggleChevron);


  /* Tabs
  -------------------------------------------------------*/
  $('.tabs__trigger').on('click', function(e) {
    var currentAttrValue = $(this).attr('href');
    $('.tabs__content-trigger ' + currentAttrValue).stop().fadeIn(1000).siblings().hide();
    $(this).parent('li').addClass('tabs__item--active').siblings().removeClass('tabs__item--active');
    e.preventDefault();
  });


  /* Sticky Socials
  -------------------------------------------------------*/
  (function() {
    var $stickyCol = $('.sticky-col');
    if($stickyCol) {
      $stickyCol.stick_in_parent({
        offset_top: 100
      });
    }
  })();


  /* Scroll to Top
  -------------------------------------------------------*/
  function scrollToTop() {
    var scroll = $window.scrollTop();
    var $backToTop = $("#back-to-top");
    if (scroll >= 50) {
      $backToTop.addClass("show");
    } else {
      $backToTop.removeClass("show");
    }
  }

  $('a[href="#top"]').on('click',function(){
    $('html, body').animate({scrollTop: 0}, 1350, "easeInOutQuint");
    return false;
  });


  // Codes for ajax setup for get and post requests to backend
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }


  let csrftoken = ''
  try{
    csrftoken = getCookie('csrftoken');
  } catch(e){}


  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }



  try{
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  } catch(e){
  }


  // THe image form
  let the_img_form = $('#the_img_form')
  let submit_form = $('#submit_form')
  let img_text = $('.img_text')
  let processing = $('#processing')

  // The image tag to show the selected image
  var the_image_view = document.getElementById("the_image_view");

  // The image input
  // let image_file = $('#image_file')
  let image_file = document.querySelector('#image_file')

  // When any element with the class btn_img is clicked the form is opened up
  let btn_img = $('.btn_img')
  btn_img.click(function(e){
    image_file.click()
  })


  // When an image is selected we want to view it and submit the form
  function showImage(src,target) {
    var fr=new FileReader();
    // when image is loaded, set the src of the image where you want to display it
    fr.onload = function(e) { target.src = this.result; };

    jQuery.noConflict();	
	  let formdata = new FormData();
    src.addEventListener("change",function() {
      // fill fr with image data    
      fr.readAsDataURL(src.files[0]);

      // Make the the_image_view displayed
      the_image_view.classList.remove('d-none')

      // Display none every other image
      img_text.css('display','none')

      // Send the image to the server
      var file = this.files[0];
      if (formdata) {
        formdata.append("pixel_image", file);

        let thisURL = window.location.href
        $.ajax({
          url: thisURL,
          type: "POST",
          data: formdata,
          processData: false,
          contentType: false,
          success: handleFormSuccess,
          error: handleFormError
        });

        // Show the processing modal
        processing.addClass('active')
      }
    });
  }

  showImage(image_file,the_image_view);

  let errors_box = document.querySelector('.errors-box')

  function handleFormSuccess(data, textStatus, jqXHR){
    // Kill the modal
    processing.removeClass('active')

    // Clean errors
    errors_box.innerHTML = ''

    // Parse the results into the required fields
    let dataKeys = Object.keys(data)

    dataKeys.forEach(i=>{
      let selector = "span.data[data-key='"+i+"']"
      let el = document.querySelector(selector)
      if (el){
        el.innerText = data[i]
      }
    })
  }
  
  function handleFormError(jqXHR, textStatus){
    // Kill the modal
    processing.removeClass('active')

    // Clean errors
    errors_box.innerHTML = ''

    // Get the data from the jqxhr
    let data = jqXHR.responseJSON

    // Show the error under the image if it is available
    let errors = data['error']
    errors.forEach(i=>{
      // <p class="error">This is an error</p>
      let new_el = document.createElement('p')
      new_el.classList.add('error')
      new_el.innerText = i

      // Adding the new element to the node
      errors_box.appendChild(new_el)
    })
  }



})(jQuery);