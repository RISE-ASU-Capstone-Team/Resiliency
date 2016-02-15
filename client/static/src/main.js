$("#map").height($(window).height() - $("#editor").height()).width(($(window).width() - $("#sideBar").width() - 20));
map.invalidateSize();
window.onresize = function (event) {
    $("#map").height($(window).height() - $("#editor").height()).width(($(window).width() - $("#sideBar").width() - 20));
    map.invalidateSize();
}
