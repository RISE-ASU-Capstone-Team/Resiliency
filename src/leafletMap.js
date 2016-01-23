//Default location ASU Polytechnic campus. See example here for finding coordinates: https://www.mapbox.com/mapbox.js/example/v1.0.0/mouse-position/
var map = L.map('map').setView([33.31, -111.68], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'jsd1710.oof23i94', //JDobkins personal Mapbox Project as placeholder. TODO: Register RISE project Mapbox. https://www.mapbox.com/studio/
    accessToken: 'pk.eyJ1IjoianNkMTcxMCIsImEiOiJjaWpuOGhlMGwwMGU1dmFseDllbWZ4ZTJtIn0.f_lRG59G0q9Or38C2cgz3Q' //JDobkins personal API AccessToken. TODO: Register RISE API Token.
}).addTo(map);

$.ajax({
    url: "\\data\\testpoints.json",
    success: function (data) {
        var obj = JSON.parse(data);
        console.log(obj);
    }
});
