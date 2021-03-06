var jsonObjectTest = {
    "name": "IEEE 123 Bus Feeder",
    "type": "SG: Unbalanced",
    "format": "ANSI standard",
    "transformerDelta": "Dyn 1",
    "units": ["     Imperial","(kV) kilovolts","(kA) kiloamps","(kVA) kvolt-amp"],
    "frequency": "  60 Hz",
    "temperature": "(F) Fahrenheit",
    "description": "The IEEE 123 node test",

}

var networkWaterJSON = {
    "junctions":"4,000",
    "reservoirs":"15",
    "tanks":"5",
    "pipes":"5,000",
    "pumps":"10",
    "valves":"30"

}

var projectJSON = {
    "projectName":"Project 1",
    "projectCreation":"3/31/16",
    "projectDescription":"Rise Project: Test 1"
}

waterNetworkTable(networkWaterJSON);
projectDescriptionTable(projectJSON);
//jsontoTable(jsonObjectTest);



function projectDescriptionTable(projectJSON) {

    document.getElementById("projectName").innerHTML=projectJSON.projectName;
    document.getElementById("projectCreation").innerHTML=projectJSON.projectCreation;
    document.getElementById("projectDescription").innerHTML=projectJSON.projectDescription;


}
function jsontoTable(jsonObject) {
    // var jsOBject = {};
    // try {
    // jsOBject =
    //    JSON.parse(jsonObject);
    //    return JSON.parse(jsonObject);
    // } catch (e) {
    //     return null;
    //   console.log("Error when reading from Local Storage\n" + e);
    // }



}

function waterNetworkTable(JSON) {

    document.getElementById("junctions").innerHTML=JSON.junctions;
    document.getElementById("reservoirs").innerHTML=JSON.reservoirs;
    document.getElementById("tanks").innerHTML=JSON.tanks;
    document.getElementById("pipes").innerHTML=JSON.pipes;
    document.getElementById("pumps").innerHTML=JSON.pumps;
    document.getElementById("valves").innerHTML=JSON.valves;

}
