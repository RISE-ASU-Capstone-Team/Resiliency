$("#hamburger").click(function()
{
  $('nav').css('opacity', 1);

  //Push content off-page with same width rather than squeezing in remaining space.
  var contentWidth = $('#content').width();
  $('#contentLayer').css('width', contentWidth);

  //Lay contentLayer over page
  $('#contentLayer').css('display', 'block');

  $("#content").width(($(window).width() - $("#sideBar").width() - $('#leftBar').width() - 20));
  $("#map").width(($(window).width() - $("#sideBar").width() - $('#leftBar').width() - 20));
  $("#editor").width(($(window).width() - $("#sideBar").width() - $('#leftBar').width() - 20));
  $("#editor_content").width(($(window).width() - $("#sideBar").width() - $('#leftBar').width() - 20));
  //set margin for the whole container with a jquery UI animation
  $("#body").animate({
    "marginLeft": "15%"
  }, {
    duration: 70
  });



  $("#contentLayer").click(function()
  {
    //set margin for the whole container back to original state with a jquery UI animation
    $("#body").animate({
      "marginLeft": "-1"
    }, {
      duration: 70,
      complete: function() {
        $('nav').css('opacity', 0);
		$('#contentLayer').css('display', 'none');
		$("#content").width(($(window).width() - $("#sideBar").width() - 20));
        $("#map").width(($(window).width() - $("#sideBar").width()  - 20));
        $("#editor").width(($(window).width() - $("#sideBar").width()  - 20));
        $("#editor_content").width(($(window).width() - $("#sideBar").width()  - 20));
	}
    });
  });
});
