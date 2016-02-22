var polling = false;

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = $.cookie('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$("#map").height($(window).height() - $("#editor").height() - $("#hamburger").height() - 0).width(($(window).width() - $("#sideBar").width() - 20));
$("#content").height($("#map").height());
$("#editor").width($("#map").width());
$("#editor_content").width($("#editor").width() - $("#editor_tabs").width() - 40);
$("#leftBar").height($('#content').height);
$("#contentLayer").height($('#content').height);
$("#cmn-toggle-1").click(function(value){
    // TODO : UPDATE NODE STATUS
    $.post("http://localhost:8000/data/api/power/", {name: "Anywhere", type: 1,
            latitude: -35, longitude: 117.2, active: true}).
        done(function(data){
          // TODO : WHATEVER YOU WANT AFTER POST COMPLETED
        })
});

map.invalidateSize();

window.onresize = function (event) {
    $("#map").height($(window).height() - $("#editor").height() - $("#hamburger").height() - 0).width(($(window).width() - $("#sideBar").width() - 20));
    $("#content").height($("#map").height());
    $("#editor").width($("#map").width());
    $("#editor_content").width($("#editor").width() - $("#editor_tabs").width() - 40);
    $("#leftBar").height($('#content').height);
    $("#contentLayer").height($('#content').height);
    map.invalidateSize();
}

var monthNames = [
  "January", "February", "March",
  "April", "May", "June", "July",
  "August", "September", "October",
  "November", "December"
];

function formatTableName(name){
    var split = name.split('_');
    var ret = '';
    for(var i = 0; i < split.length; i++){
        ret+= split[i].charAt(0).toUpperCase() + split[i].slice(1) + ' ';
    }
    return ret.slice(0, -1);
}

// This is a code template for posting new node information to the server
// It applies specifically to Power nodes but is easily adaptable to others
/*
$.post("http://localhost:8000/data/api/power/", {name: "Anywhere", type: 1,
       latitude: -35, longitude: 117.2, active: true}).
    done(function(data){
        console.log("data: " + data);
    })
*/
