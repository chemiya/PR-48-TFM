/*global $,*/

$(function () {
    
    "use strict";
    
    var nav = $(".vertical-nav"),
        progressCheck = false,
        factsCheck = false;
	

		
    /*========== Loading  ==========*/
    $('.preloader').delay(200).fadeOut(700, function () {
        $(this).remove();
    });
    
    /*========== Active Menu  ==========*/
    $(".mobile-menu .toggle-menu").on("click", function () {
        nav.toggleClass("menu-active");
		$(".mobile-menu").toggleClass('push');
		$(".main-content").toggleClass('push');
		$(".project-content").toggleClass('push');
    });
	
	$(".vertical-nav .close-nav").on("click", function () {
        $(".mobile-menu .toggle-menu").click();
    });
    
    /*========== initializing page transition  ==========*/
	
	var ptPage = $('.subpages');
    if (ptPage[0]) {
        PageTransitions.init({
            menu: '.mini-menu ul',
        });
    }
	
	/*========== Skills Progress  ==========*/
	function skillsPogress() {
        $(".progress-container").each(function () {
            var progressBar = $(this).find(".progress-bar");
            progressBar.css("width", progressBar.attr("aria-valuenow") + "%");
        });
    }
    
    if (!progressCheck && $('.resume').scrollTop() >= $(".skills").offset().top + 150) {
        skillsPogress();
        progressCheck = true; 
    }
    
    $('.resume').on("scroll", function () {
        
        if (!progressCheck && $('.resume').scrollTop() >= $(".skills").offset().top + 150) {
            skillsPogress();
            progressCheck = true;
        }
        
    });
	
	var circleSkills = $('.circle-skills .skill');
    var myVal = $(this).attr('data-value');

    $(".circle-skills .skill").each(function () {

        circleSkills.circleProgress({
            startAngle: -Math.PI / 2 * 1,
            value: myVal,
            thickness: 5,
            size: 93
		});

    });
	
	/*========== Facts Counter  ==========*/
    if (!factsCheck && $('.about').scrollTop() >= $(".facts").offset().top + 200) {
        $(".facts .fact-number").countTo();
        factsCheck = true;
    }
    
    $('.about').on("scroll", function () {
        if (!factsCheck && $('.about').scrollTop() >= $(".facts").offset().top + 200) {
            $(".facts .fact-number").countTo();
            factsCheck = true;
        }
    });
	
	/*========== Slick Js  ==========*/
	$('.testimonials-slider').on('init', function (slick, slider) {
        var totalSlides = slider.$slides.length,
            nextSlideImg = $(slider.$slides[1]).find('img').attr('src'),
            prevSlideImg = $(slider.$slides[totalSlides - 1]).find('img').attr('src');
        $("#testimonials-nextArrow .testimonials-client-img").css('background-image', 'url(' + nextSlideImg + ')');
        $("#testimonials-prevArrow .testimonials-client-img").css('background-image', 'url(' + prevSlideImg + ')');
    });
    $('.testimonials-slider').on('beforeChange', function (event, slick, currentSlide, nextSlide) {
        var totalSlides = slick.$slides.length,
            nextSlideNum = (nextSlide + 1 === totalSlides) ? 0 : nextSlide + 1,
            prevSlideNum = (nextSlide === 0) ? totalSlides - 1 : nextSlide - 1,
            nextSlideImg = $(slick.$slides[nextSlideNum]).find('img').attr('src'),
            prevSlideImg = $(slick.$slides[prevSlideNum]).find('img').attr('src');
        $("#testimonials-nextArrow .testimonials-client-img").css('background-image', 'url(' + nextSlideImg + ')');
        $("#testimonials-prevArrow .testimonials-client-img").css('background-image', 'url(' + prevSlideImg + ')');
    });
    $('.testimonials-slider').slick({
        centerMode: true,
        centerPadding: '20px',
        slidesToShow: 1,
		autoplay: true,
        autoplaySpeed: 8000,
        arrows: true,
        nextArrow: $('#testimonials-nextArrow'),
        prevArrow: $('#testimonials-prevArrow'),
        appendDots: "#testimonial-paging",
        customPaging: function (slider, i) {
            var thumb = $(slider.$slides[i]).find('img').attr('src'),
                name = $(slider.$slides[i]).find('.testimonials-info h3').text();
            return '<i class="dot"><img src="' + thumb + '" class="img-fluid" data-toggle="tooltip" data-placement="top" title="' + name + '"></i>';
        },
        dots: true
    });
	
    /*========== Popup Js ==========*/
    $('.portfolio-content .item > a').on("click", function () {
		var dataType = $(this).attr('data-type');
		$('.' + dataType).addClass('active').siblings().removeClass('active');
    });
	
	$('.project-content .close').on("click", function () {
		$('.project-content').removeClass('active');
    });
	
	/*========== Ajax Contact Form  ==========*/
	$('.contact-form').on("submit", function () {
		
		var myForm = $(this),
			data = {};
		
		myForm.find('[name]').each(function () {
			
			var that = $(this),
				name = that.attr('name'),
				value = that.val();
			
			data[name] = value;
			
		});
		
		$.ajax({
			
			url: myForm.attr('action'),
			type: myForm.attr('method'),
			data: data,
			success: function (response) {
				
				if (response == "success") {
								
					$(".contact-form").find(".form-message").addClass("success");
					$(".form-message span").text("Message Sent!");
					
				} else {
					
					$(".contact-form").find(".form-message").addClass("error");
					$(".form-message span").text("Error Sending!");
					
				}
			}
			
		});
		
		return false;
		
	});
});

/*---- #ff8766 ---- #627af9 ----*/