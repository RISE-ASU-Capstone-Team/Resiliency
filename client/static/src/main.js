$("#map").height($(window).height() - $("#editor").height()).width(($(window).width() - $("#sideBar").width() - 20));
$("#editor").width($("#map").width());
$("#editor_content").width($("#editor").width() - $("#editor_tabs").width() - 40);
map.invalidateSize();
window.onresize = function (event) {
    $("#map").height($(window).height() - $("#editor").height()).width(($(window).width() - $("#sideBar").width() - 20));
    $("#editor").width($("#map").width());
    $("#editor_content").width($("#editor").width() - $("#editor_tabs").width() - 40);
    map.invalidateSize();
}
