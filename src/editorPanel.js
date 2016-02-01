

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

 var testObj = JSON.parse(testData);
 loadPanelObjects(testObj);

function loadPanelObjects(jsonobj) {
  console.log(jsonobj);

  for (var i = 0; i < jsonobj.Components.length; i++) {
    var component = jsonobj.Components[i]
    var img = document.createElement("img");
    img.src = component.Icon;

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
