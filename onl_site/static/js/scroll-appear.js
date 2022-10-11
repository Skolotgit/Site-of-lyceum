$(document).ready(function() {
	var windowHeight = $(window).height();
 
	$(document).on('scroll', function() {
		$('.left_outflow_element_before').each(function() {
			var self = $(this),
			height = self.offset().top;
			if ($(document).scrollTop() + windowHeight >= height) {
				self.addClass('left_outflow_element_after')
			}
		});
	});
});

$(document).ready(function() {
	var windowHeight = $(window).height();
 
	$(document).on('scroll', function() {
		$('.right_outflow_element_before').each(function() {
			var self = $(this),
			height = self.offset().top;
			if ($(document).scrollTop() + windowHeight >= height) {
				self.addClass('right_outflow_element_after')
			}
		});
	});
});