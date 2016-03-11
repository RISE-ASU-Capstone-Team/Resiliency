var polling = false;
var loadEditableCount = 13;
var syncGenEditableCount = 11;
var busEditableCount = 5;

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
$("#cmn-toggle-1").click(function(value){
    // TODO : UPDATE NODE STATUS
    $.post("http://localhost:8000/data/api/power/", {name: "Anywhere", type: 1,
            latitude: -35, longitude: 117.2, active: true}).
        done(function(data){
          // TODO : WHATEVER YOU WANT AFTER POST COMPLETED
        })
});

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
    console.log(row);
    console.log(cell);
    var input = document.createElement("td");
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
        cell.className = "rowData";
        cell.onclick = function(e){editComponent(this)};
        row.appendChild(cell);
        $.ajax({
            url: "http://localhost:8000/data/api/power/1/",
            type: 'PUT',
            data: "name=Anywhere",
            success: function(result) {
                // Do something with the result
            }
        });
    }
}

// This is a code template for posting new node information to the server
// It applies specifically to Power nodes but is easily adaptable to others
/*
$.post("http://localhost:8000/data/api/power/", {name: "Anywhere", type: 1,
       latitude: -35, longitude: 117.2, active: true}).
    done(function(data){
        console.log("data: " + data);
    })
*/
