//Default location ASU Polytechnic campus. See example here for finding coordinates: https://www.mapbox.com/mapbox.js/example/v1.0.0/mouse-position/
var map = L.map('map').setView([33.31, -111.68], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'jsd1710.oof23i94', //JDobkins personal Mapbox Project as placeholder. TODO: Register RISE project Mapbox. https://www.mapbox.com/studio/
    accessToken: 'pk.eyJ1IjoianNkMTcxMCIsImEiOiJjaWpuOGhlMGwwMGU1dmFseDllbWZ4ZTJtIn0.f_lRG59G0q9Or38C2cgz3Q' //JDobkins personal API AccessToken. TODO: Register RISE API Token.
}).addTo(map);

var defaultIconSize = new L.Point(64, 64);
var defaultConnectionIconSize = new L.Point(30, 30);

var markers = [];
var connections = [];
var connectionMarkers = [];

function addMarkerToMap(key, componentData, position, options) {
    var newMarker = L.marker(position, options).addTo(map);
    newMarker.componentData = componentData;
    newMarker.on('click', handleMarkerClick);
    newMarker.on('dragend', function(){
      repositionConnectionsFromMarker(newMarker);
      $.ajax({
            url: Server.ADDRESS + "data/api/" + nodeType(newMarker.componentData.Type) + '/'
                + newMarker.id + "/" ,
            type: 'PUT',
            data: {"id": newMarker.id, "type": newMarker.componentData.Type,
      "latitude": newMarker._latlng.lat, "longitude": newMarker._latlng.lng, active: true},
            success: function(result) {
                // Do something with the result
            }
        });

    });
    newMarker.id = key;
    markers[key] = newMarker;
    resizeMarkers();
    Alert.log("Node: '" + newMarker.id + "' created at " + newMarker._latlng);
    return newMarker;
}

var nodeIcon = L.Icon.extend({
      options: {
        iconSize: defaultIconSize,
        iconAnchor: [defaultIconSize.x / 2.0, defaultIconSize.y]
      }
    });
var connectionIcon = L.Icon.extend({
      options: {
        iconSize: defaultConnectionIconSize,
        iconAnchor: [defaultConnectionIconSize.x / 2.0, defaultConnectionIconSize.y / 2.0]
      }
    });

map.on('zoomend', handleMapZoom);

function handleConnectionClick(e) {
  var id = e.target.id;
  var type = e.target.type;
  $.get(Server.ADDRESS + 'data/api/' + connectionType(e.target.type) + '/'
        + e.target.id + '/?format=json').success(function(d){
       loadComponent(d, false);
    });


  document.getElementById('deleteConnectionButton').style.display = "block";
  document.getElementById('deleteNodeButton').style.display = "none";
  document.getElementById('deleteConnectionButton').onclick = function deleteNode(){
    map.removeLayer(connections[id].middleMarker);
    map.removeLayer(connections[id]);

    connections
    $.ajax({
        url: Server.ADDRESS + "data/api/" + connectionType(type) + '/'
            + id + "/" ,
        type: 'delete',
        success: function(result) {
            connections.splice(id, 1);
        }
    });
document.getElementById('deleteConnectionButton').style.display = "none";
  }

}

function handleMarkerClick(e) {
  var component = this.componentData;
  var typeNumer = this.componentData.Type;
  var id = this.id

  if (event.altKey && !connectionStarted)
  {
    connectionStarted = true;
    initialConnection = this;
  }
  else if (event.altKey && connectionStarted)
  {
    if (this.id != initialConnection.id)
      {
        destinationConnection = this;
        var dialog = document.getElementById('dialogContainer');
        dialog.style.display = "block";
      }
    connectionStarted = false;
  }else{
    $.get(Server.ADDRESS + 'data/api/' + nodeType(component.Type) + '/'
        + e.target.id + '/?format=json').success(function(d){
       loadComponent(d, true);
    });
  }

  document.getElementById('deleteNodeButton').style.display = "block";
  document.getElementById('deleteConnectionButton').style.display = "none";

  document.getElementById('deleteNodeButton').onclick = function deleteNode(){
    map.removeLayer(markers[id]);
    markers.splice(id, 1);
    $.ajax({
        url: Server.ADDRESS + "data/api/" + nodeType(typeNumer) + '/'
            + id + "/" ,
        type: 'delete',
        success: function(result) {
            markers.splice(id, 1);
        }
    });

    document.getElementById('deleteNodeButton').style.display = "none";
  }
}


function doneConnectionDialog(dialog){
    var select = document.getElementById("conSelect");
    var con_type = select.options[select.selectedIndex].value;
    $.post(Server.ADDRESS + "data/api/"
           + connectionType(con_type)
           + "/", {from_bus_id: initialConnection.id, to_bus_id: destinationConnection.id, type: con_type}).
         done(function(data){
            addConnectionToMap(data.id, data.type, destinationConnection, initialConnection, polylineOptions);
        });
    dialog.style.display = 'none';
}

function closeConnectionDialog(dialog){
    dialog.style.display = 'none';
}

function addConnectionToMap(key, type, markerA, markerB, options) {
  if (isPowerConnection(type)) {
    options.color = Power.Con.LINE_COLOR;
  } else if (isWaterConnection(type)) {
    options.color = Water.Con.LINE_COLOR;
  }
  var polyLine = new L.Polyline([markerA._latlng, markerB._latlng], options);
  polyLine.addTo(map);
  polyLine.on('click', handleConnectionClick);
  polyLine.id = key;
  polyLine.type = type;
  polyLine.markerA = markerA;
  polyLine.markerB = markerB;

  if (type == Power.Con.TRANSFORMER) {

    var newIcon = new connectionIcon({
        iconUrl: "/static/icons/Transformer.png"
      });

    var options = {
          icon: newIcon,
          clickable: true,
          draggable: false,
          keyboard: false
        };
      var position = L.latLng((markerA._latlng.lat + markerB._latlng.lat) / 2.0,
                              (markerA._latlng.lng + markerB._latlng.lng) / 2.0);
      polyLine.middleMarker = L.marker(position, options).addTo(map);
      polyLine.middleMarker.parentConnection = polyLine;
      connectionMarkers[key] = polyLine.middleMarker;
  }
  if(!markerA.connections)
  {
    markerA.connections = new Array();
  }
  if (markerA.connections.indexOf(polyLine.id) == -1)
  {
    markerA.connections.push(polyLine.id);
  }

  if(!markerB.connections)
  {
    markerB.connections = new Array();
  }
  if (markerB.connections.indexOf(polyLine.id) == -1)
  {
    markerB.connections.push(polyLine.id);
  }

  Alert.log("Connection: '" + polyLine.id + "' created from Node '" + markerA.id + "' to '" + markerB.id + "'");
  connections[key] = polyLine;
}

function repositionConnectionsFromMarker(marker)
{
  if (!marker.connections)
  {
    return;
  }
  marker.connections.forEach(function(id){
    var type = connections[id].type;
    var markerA = connections[id].markerA;
    var markerB = connections[id].markerB;
    var options = connections[id].options;
    if (connections[id].middleMarker)
    {
      map.removeLayer(connections[id].middleMarker);
    }
    map.removeLayer(connections[id]);
    delete connections[id];
    addConnectionToMap(id, type, markerA, markerB, options);
  });
  {

  }
}

function handleMapZoom(e) {
  resizeMarkers();
}

function resizeMarkers() {

  // use leaflet's internal methods to scale the size (a bit overkill for this case...)
  var transformation = new L.Transformation(1, 0, 1, 0);

  var currentZoom = map.getZoom();

  // Resize Normal Node Map Markers
  for (var key in markers) {
    var marker = markers[key];
    resizeMarker(marker, defaultIconSize, 0.5, 1.0);
  }

  // Resize Connection Markers
  for (var key in connectionMarkers) {
    var marker = connectionMarkers[key];
    resizeMarker(marker, defaultConnectionIconSize, 0.5, 0.5);
  }
}

function resizeMarker(marker, iconSize, xPercentage, yPercentage) {

  var transformation = new L.Transformation(1, 0, 1, 0);
  var currentZoom = map.getZoom();

  var newIconSize = transformation.transform(iconSize, sizeFactor(currentZoom));

  // adjust the icon anchor to the new size
  var newIconAnchor = new L.Point(Math.round(newIconSize.x * xPercentage),
                                  Math.round(newIconSize.y * yPercentage));

  // finally, declare a new icon and update the marker
  var newIcon = new L.Icon({
      iconUrl: marker._icon.src,
      iconSize: newIconSize,
      iconAnchor: newIconAnchor
    });
  marker.setIcon(newIcon);
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
