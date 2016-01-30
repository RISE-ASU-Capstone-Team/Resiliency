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


jsontoTable(jsonObjectTest)


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