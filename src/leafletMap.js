//Default location ASU Polytechnic campus. See example here for finding coordinates: https://www.mapbox.com/mapbox.js/example/v1.0.0/mouse-position/
var map = L.map('map').setView([33.31, -111.68], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'jsd1710.oof23i94', //JDobkins personal Mapbox Project as placeholder. TODO: Register RISE project Mapbox. https://www.mapbox.com/studio/
    accessToken: 'pk.eyJ1IjoianNkMTcxMCIsImEiOiJjaWpuOGhlMGwwMGU1dmFseDllbWZ4ZTJtIn0.f_lRG59G0q9Or38C2cgz3Q' //JDobkins personal API AccessToken. TODO: Register RISE API Token.
}).addTo(map);

$.ajax({
    url: "\\static\\testpoints.json",
    success: function (data) {
        var obj = JSON.parse(data);
        console.log(obj);
    }
});


$(document).ready(function() {

  initEditorPanel();

	// Drag & Drop
	$(".dragComponent").draggable({
		helper: 'clone',		// GJS - Sets that the item should be "cloned" instead of moved.
		containment: 'map', // Only can be dragged within the map element
		start: function(evt, ui) {
			//$('#box').fadeTo('fast', 0.6, function() {});
		},
		stop: function(evt, ui) {
			//$('#box').fadeTo('fast', 1.0, function() {});

			var options = {
				pid: guid(),
				type: ui.helper.attr('type'),
				icon: eval(ui.helper.attr('type') + 'Icon'),
				draggable: true
			};

			insertPoint(
				map.containerPointToLatLng([ui.offset.left, ui.offset.top]),
				options
			);
		}
	});
});

function insertPoint(position,options) {

	var point = L.marker(position,options).addTo(map);

	point.on('dragend', function(evt){
		updatePoint(point);
	});

	markers.push(point);
}

var icons = [];
function createLeafletIcon(key, imgPath) {
  var newIcon = new L.Icon({
		    options: {
		        iconSize: [30,30],
		        iconAnchor: [0,0],
            iconUrl:imgPath
		    }
		});
  icons[key] = newIcon;
}
