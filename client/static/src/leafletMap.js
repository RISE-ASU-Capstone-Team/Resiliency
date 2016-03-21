//Default location ASU Polytechnic campus. See example here for finding coordinates: https://www.mapbox.com/mapbox.js/example/v1.0.0/mouse-position/
var map = L.map('map').setView([33.31, -111.68], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'jsd1710.oof23i94', //JDobkins personal Mapbox Project as placeholder. TODO: Register RISE project Mapbox. https://www.mapbox.com/studio/
    accessToken: 'pk.eyJ1IjoianNkMTcxMCIsImEiOiJjaWpuOGhlMGwwMGU1dmFseDllbWZ4ZTJtIn0.f_lRG59G0q9Or38C2cgz3Q' //JDobkins personal API AccessToken. TODO: Register RISE API Token.
}).addTo(map);

var defaultIconSize = new L.Point(64, 64);
var markers = [];
function addMarkerToMap(key, componentData, position, options) {
    var newMarker = L.marker(position, options).addTo(map);
    newMarker.componentData = componentData;
    newMarker.on('click', handleMarkerClick);
    markers[key] = newMarker;
}

var compIcon = L.Icon.extend({
      options: {
        iconSize: defaultIconSize,
        iconAnchor: [0, 0]
      }
    });

map.on('zoomend', handleMapZoom);

function handleMarkerClick(e) {
  var component = this.componentData;
  if (event.altKey && !connectionStarted)
  {
    connectionStarted = true;
    initialConnection = this;
  }
  else if (event.altKey && connectionStarted)
  {
    var polyLine = new L.Polyline([this._latlng, initialConnection._latlng], polylineOptions);
    polyLine.addTo(map);
    console.log(this);
    initialConnection = null;
    connectionStarted = false;
  }
}

function handleMapZoom(e) {
  resizeMarkers();
}

function resizeMarkers() {

  // use leaflet's internal methods to scale the size (a bit overkill for this case...)
  var transformation = new L.Transformation(1, 0, 1, 0);

  var currentZoom = map.getZoom();

  for (var key in markers) {
    var marker = markers[key];
    var newIconSize = transformation.transform(defaultIconSize, sizeFactor(currentZoom));

    // adjust the icon anchor to the new size
    var newIconAnchor = new L.Point(Math.round(newIconSize.x / 2), Math.round(newIconSize.y / 1));

    // finally, declare a new icon and update the marker
    var newIcon = new compIcon({
        iconUrl: marker._icon.src,
        iconSize: newIconSize,
        iconAnchor: newIconAnchor
      });
    marker.setIcon(newIcon);
  }
}

function sizeFactor(zoom) {
  if (zoom <= 8) return 0.3;
  else if (zoom == 9) return 0.4;
  else if (zoom == 10) return 0.5;
  else if (zoom == 11) return 0.7;
  else if (zoom == 12) return 0.85;
  else if (zoom == 13) return 1.0;
  else if (zoom == 14) return 1.3;
  else if (zoom == 15) return 1.6;
  else if (zoom == 16) return 1.9;
  else // zoom >= 17
  return 2.2;
}
