var polling = false;
var selectedComponent = {};
var loadEditableCount = 12;
var syncGenEditableCount = 11;
var busEditableCount = 5;


//Connecting Nodes
var connectionStarted = false;
var initialConnection = null;
var destinationConnection = null;

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
var csrftoken = $.cookie('csrftoken');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$("#map").height($(window).height() - $("#editor").height() - $("#hamburger").height() - 0).width(($(window).width() - $("#sideBar").width() - 20));
$("#content").height($("#map").height());
$("#editor").width($("#map").width());
$("#editor_content").width($("#editor").width() - $("#editor_tabs").width() - 40);
$("#leftBar").height($('#content').height());
$("#sideBar").height($(window).height()-45);
$("#contentLayer").height($('#content').height());
$("#tab-content").height($(window).height()- $("#attributesTable").height() - 45);

map.invalidateSize();

window.onresize = function (event) {
    $("#map").height($(window).height() - $("#editor").height() - $("#hamburger").height() - 0).width(($(window).width() - $("#sideBar").width() - 20));
    $("#content").height($("#map").height());
    $("#editor").width($("#map").width());
    $("#editor_content").width($("#editor").width() - $("#editor_tabs").width() - 40);
    $("#leftBar").height($('#content').height);
    $("#sideBar").height($(window).height()-45);
    $("#tab-content").height($(window).height()- $("#attributesTable").height() - 45);
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

var editComponent = function(cell){
    var row = cell.parentNode;
    var input = document.createElement("td");
    input.id = cell.id;
    input.innerHTML = "<input class='componentInput' value='" + cell.innerHTML
        + "' onkeydown='postChange(this)'></input>";
    row.removeChild(cell);
    row.appendChild(input);
}

var postChange = function(input){
    if(event.keyCode == 13){
        var cell = input.parentNode;
        var row = cell.parentNode;
        row.removeChild(cell);
        cell.innerHTML = input.value;
        selectedComponent[cell.id] = input.value;
        cell.className = "rowData";
        cell.onclick = function(e){editComponent(this)};
        cell.id = input.id;

        row.appendChild(cell);
        $.ajax({
            url: Server.ADDRESS + "data/api/" + nodeType(selectedComponent.type) + '/'
                + selectedComponent.id + "/" ,
            type: 'PUT',
            data: selectedComponent,
            success: function(result) {
                // Do something with the result
            }
        });
    }
}

var toggleClicked = function(type){
    selectedComponent[type] = selectedComponent[type]? false : true;
    $.ajax({
        url: Server.ADDRESS + "data/api/" + nodeType(selectedComponent.type) + '/'
            + selectedComponent.id + "/" ,
        type: 'PUT',
        data: selectedComponent,
        success: function(result) {
            // Do something with the result
        }
    });
}

function doneConnectionDialog(dialog){
    $.post(Server.ADDRESS + "data/api/"
           + connectionType(document.getElementById("powerConSelect").selectedIndex)
           + "/", {from_bus_id: initialConnection.id, to_bus_id: destinationConnection.id}).
         done(function(data){
            addConnectionToMap(data.id, destinationConnection, initialConnection, polylineOptions);
        });
    dialog.style.display = 'none';
}

function closeConnectionDialog(dialog){
    dialog.style.display = 'none';
}

function powerConnectionClicked(){
    var list = document.getElementById("powerConSelect");
    list.style.display = 'block';
}

$(".toggle-btn:not('.noscript') input[type=radio]").addClass("visuallyhidden");
$(".toggle-btn:not('.noscript') input[type=radio]").change(function() {
    if( $(this).attr("name") ) {
        $(this).parent().addClass("success").siblings().removeClass("success")
    } else {
        $(this).parent().toggleClass("success");
    }
});


// This is a code template for posting new node information to the server
// It applies specifically to Power nodes but is easily adaptable to others
/*
$.post("http://localhost:8000/data/api/power/", {name: "Anywhere", type: 1,
       latitude: -35, longitude: 117.2, active: true}).
    done(function(data){
        console.log("data: " + data);
    })
*/
