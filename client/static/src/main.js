$("#map").height($(window).height() - $("#editor").height() - $("#hamburger").height() -100).width(($(window).width() - $("#sideBar").width() - 20));
$("#editor").width($("#map").width());
$("#editor_content").width($("#editor").width() - $("#editor_tabs").width() - 40);
map.invalidateSize();
window.onresize = function (event) {
    $("#map").height($(window).height() - $("#editor").height() - $("#hamburger").height() -100).width(($(window).width() - $("#sideBar").width() - 20));
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
