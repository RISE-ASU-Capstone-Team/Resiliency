var jsonObjectTest = 
{
    "project": {
        "name": "IEEE 123 Bus Feeder",
        "type": "SG: Unbalanced",
        "format": "ANSI standard",
        "transformerDelta": "Dyn 1",
        "units": ["     Imperial","(kV) kilovolts","(kA) kiloamps","(kVA) kvolt-amp"],
        "frequency": "  60 Hz",
        "temperature": "(F) Fahrenheit",
        "description": "The IEEE 123 node test",
    }
}

var networkWaterJSON=
{
    "junctions":"4,000",
    "reservoirs":"15",
    "tanks":"5",
    "pipes":"5,000",
    "pumps":"10",
    "valves":"30"

}


jsontoTable(jsonObjectTest)
waterNetworkTable(networkWaterJSON)

function jsontoTable(jsonObject){
    // var jsOBject = {};
    // try {
    // jsOBject =
    //    JSON.parse(jsonObject);
    //    return JSON.parse(jsonObject);
    // } catch (e) {
    //     return null;
    //   console.log("Error when reading from Local Storage\n" + e);        
    // }

	document.getElementById("name").innerHTML=jsonObject.project.name;
	document.getElementById("type").innerHTML=jsonObject.project.type;
	document.getElementById("format").innerHTML=jsonObject.project.format;
	document.getElementById("transformerDelta").innerHTML=jsonObject.project.transformerDelta;
	document.getElementById("units").innerHTML=jsonObject.project.units;
	document.getElementById("frequency").innerHTML=jsonObject.project.frequency;
	document.getElementById("temperature").innerHTML=jsonObject.project.temperature;
	document.getElementById("description").innerHTML=jsonObject.project.description;
	
}

function waterNetworkTable(networkWaterJSON){

    document.getElementById("junctions").innerHTML=networkWaterJSON.junctions;
    document.getElementById("reservoirs").innerHTML=networkWaterJSON.reservoirs;
    document.getElementById("tanks").innerHTML=networkWaterJSON.tanks;
    document.getElementById("pipes").innerHTML=networkWaterJSON.pipes;
    document.getElementById("pumps").innerHTML=networkWaterJSON.pumps;
    document.getElementById("valves").innerHTML=networkWaterJSON.valves;




    
}