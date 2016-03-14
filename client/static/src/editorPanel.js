
var defaultComponentsArr = null;
function initEditorPanel() {
   defaultComponentsArr = new Array();
}

function loadPanelObjects(jsonobj) {

  for (var i = 0; i < jsonobj.Components.length; i++) {
    var component = jsonobj.Components[i]
    var img = document.createElement("img");
    img.class = "dragComponent";
    img.className = "dragComponent";
    img.src = component.Icon;
    img.style = "width:64px;height:64px;"
    img.draggable="true";
    img.dataset.RiseVariableName=component.RiseVariableName;
    img.title = component.Description;

    defaultComponentsArr[component.RiseVariableName] = component;

    var src = null;
    if (component.System = "Power") {
      src = document.getElementById("editor_power");
    } else if (component.System = "Water") {
      src = document.getElementById("editor_water");
    } else if (component.System = "Road") {
      src = document.getElementById("editor_road");
    }
    src.appendChild(img);
  }
}

var dragMousePositionX, dragMousePositionY;

$(document).ready(function() {

  initEditorPanel();

  $.getJSON( "/static/components.json" , function( result ){
      loadPanelObjects(result);
  });

  $("#editor").resize(function(ev) {
    $("#editor_content").width($("#editor").width() - $("#editor_content").left());
  });
  $("#editor_collapse").bind("click", function(ev) {

    if ($("#editor_content").is(":hidden")) {
      $("#log_ticker").hide();
      $("#editor").css({'height': 'auto'});
      $("#map").css({'height': $("#map").height()-100+'px'});
      $("#content").css({'height': $("#content").height()-100+'px'}, 1000);
    } else {
      $("#log_ticker").show();
      $("#editor").css({'height': '50px'});
      $("#map").css({'height': $("#map").height()+100+'px'});
      $("#content").css({'height': $("#content").height()+100+'px'}, 1000);
    }
    $("#editor_content").slideToggle(0);
  });
  $("#editor .tab-pane")
    .bind("dragstart", function(ev) {
      if (!$(ev.target).hasClass("dragComponent")) return true;

      var dt = ev.originalEvent.dataTransfer;
      var dragIcon = null;

    	//set a reference to the element that is currenly being dragged
    	dt.setData("id",ev.target.id);

    	//create a custom drag image
    	dragIcon = document.createElement('img');
    	dragIcon.src = ev.target.src;
      //dragIcon.width = 64;
      //dragIcon.height = 64;

    	//set the custom drag image
    	dt.setDragImage(dragIcon, dragIcon.width/2.0, dragIcon.height/2.0);
    });
  $("#editor .tab-pane")
    .bind("dragend", function(ev) {
      if (!$(ev.target).hasClass("dragComponent")) return true;

      var e = ev.originalEvent;
      var data = e.target.dataset.RiseVariableName;
      if (data != null) {
        var component = defaultComponentsArr[data];
        var rect = map._container.getBoundingClientRect();
        var x = dragMousePositionX - rect.left;
        var y = dragMousePositionY - rect.top;
        var latlng = map.containerPointToLatLng([x, y]);

        var newIcon = new compIcon({
            iconUrl: component.Icon,
            iconAnchor: [defaultIconSize.x/2.0, defaultIconSize.y/2.0]
          });

        var options = {
  						icon: newIcon,
  						clickable: true,
  						draggable: true,
              keyboard: false
            };

        addMarkerToMap(markers.length+1+"", component, latlng, options);
      }
    });
  $('#map')
    .bind("dragenter", function(ev) {
        ev.preventDefault();
      });
  $('#map')
    .bind("dragover", function(ev) {
      var e = ev.originalEvent;
      var potentialX, potentialY;
       potentialX=e.clientX||e.pageX;
       potentialY=e.clientY||e.pageY;
      if (potentialX > 0 || potentialY > 0) {
         dragMousePositionX=potentialX;
         dragMousePositionY=potentialY;
       }
    });
});
