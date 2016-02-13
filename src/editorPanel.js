

 $.ajax({
     url: "\\data\\components.json",
     success: function (data) {
         var obj = JSON.parse(data);
         loadPanelObjects(obj);
     }
 });

 var testData = "{ \
   \"Components\" : [ \
     { \
       \"System\": \"Power\", \
       \"Subsystem\": \"Generation Subsystem\", \
       \"RiseVariableName\": \"genSynchronous\", \
       \"Description\": \"Synchronous Generator\", \
       \"OpenDssName\": \"null\", \
       \"Icon\": \"data/MultiCell-Icon.png\", \
       \"Variables\": [ \
         { \
           \"VariableName\": \"status\", \
           \"OpenDssVariable\": \"\", \
           \"Units\": \"none\", \
           \"Type\": \"boolean\", \
           \"OpenDssType\": \"\", \
           \"ValueRange\": \"on/off\", \
           \"Description\": \"Status\", \
           \"OpenDssV_Name\": \"\", \
           \"Comments\": \"\" \
         }, \
         { \
           \"VariableName\": \"connectBusNumber\", \
           \"OpenDssVariable\": \"\", \
           \"Units\": \"none\", \
           \"Type\": \"integer\", \
           \"OpenDssType\": \"\", \
           \"ValueRange\": \"positive\", \
           \"Description\": \"Bus number (connected)\", \
           \"OpenDssV_Name\": \"\", \
           \"Comments\": \"\" \
         } \
       ] \
     }, \
     { \
       \"System\": \"Power\", \
       \"Subsystem\": \"Generation Subsystem\", \
       \"RiseVariableName\": \"genSolarPVMod\", \
       \"Description\": \"Solar PV Module\", \
       \"OpenDssName\": \"null\", \
       \"Icon\": \"data/FixedResister-Icon.png\", \
       \"Variables\": [ \
         { \
           \"VariableName\": \"capacity\", \
           \"OpenDssVariable\": \"\", \
           \"Units\": \"kW\", \
           \"Type\": \"double\", \
           \"OpenDssType\": \"\", \
           \"ValueRange\": \"zero or positive\", \
           \"Description\": \"Capacity\", \
           \"OpenDssV_Name\": \"\", \
           \"Comments\": \"Rated DC output, also known as 'maximum power'\" \
         }, \
         { \
           \"VariableName\": \"azimuth\", \
           \"OpenDssVariable\": \"\", \
           \"Units\": \"degrees\", \
           \"Type\": \"double\", \
           \"OpenDssType\": \"\", \
           \"ValueRange\": \"-180 to 180\", \
           \"Description\": \"Azimuth\", \
           \"OpenDssV_Name\": \"\", \
           \"Comments\": \"0 degrees is due South, positive degrees rotation clockwise\" \
         } \
       ] \
     } \
   ] \
 }";

 var componentsArr = null;

 initEditorPanel();

 function initEditorPanel() {
   var testObj = JSON.parse(testData);
   componentsArr = new Array();

   loadPanelObjects(testObj);
}

function loadPanelObjects(jsonobj) {
  //console.log(jsonobj);

  for (var i = 0; i < jsonobj.Components.length; i++) {
    var component = jsonobj.Components[i]
    var img = document.createElement("img");
    img.class = "dragComponent";
    img.src = component.Icon;
    img.style = "width:64px;height:64px;"
    img.draggable="true";
    img.dataset.RiseVariableName=component.RiseVariableName;
    img.ondragstart = dragStartComponent;
    //img.ondrag = dragComponent;
    img.ondragend = dropComponent;

    componentsArr[component.RiseVariableName] = component;

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
//function dragComponent(ev) {
//}

function allowDropComponent(ev) {
    ev.preventDefault();
}

function dragStartComponent(ev) {
    //ev.dataTransfer.setData("componentVariableName", ev.target.dataset.RiseVariableName);
    ev.dataTransfer.setDragImage(ev.target, ev.target.width/2.0, ev.target.height/2.0);
}

function mapDragEnter(ev) {
    ev.preventDefault();
}

function mapDragOver(ev) {
  //ev=ev.originalEvent;
  //console.log(ev);
  var potentialX, potentialY;
   potentialX=ev.clientX||ev.pageX;
   potentialY=ev.clientY||ev.pageY;
  if (potentialX > 0 || potentialY > 0) {
     dragMousePositionX=potentialX;
     dragMousePositionY=potentialY;
     //console.log('clientX:' + ev.clientX + " clientY:" + ev.clientY + ' || pageX:' + ev.pageX + " pageY:" + ev.pageY);
   }
}

function dropComponent(ev) {
    ev.preventDefault();
    //var data = ev.dataTransfer.getData("componentVariableName");
    var data = ev.target.dataset.RiseVariableName;
    if (data != null) {
      var component = componentsArr[data];
      var rect = map._container.getBoundingClientRect();
      //var x = ev.pageX - rect.left;
      //var y = ev.pageY - rect.top;
      var x =dragMousePositionX - rect.left;
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

      addMarkerToMap(latlng, options);
    }
}
