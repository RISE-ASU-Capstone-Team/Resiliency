var jsonObjectTest = {

        name: "IEEE 123 Bus Feeder",
        type: "SG: Unbalanced",
        format: "ANSI standard",
        transformerDelta: "Dyn 1",
        units: "Imperial,(kV) kilovolts ,(kA) kiloamps, (kVA) kvolt-amp",
        frequency: "  60 Hz",
        temperature: "(F) Fahrenheit",
        description: "The IEEE 123 node test",
    
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

	document.getElementById("name").innerHTML=jsonObject.name;
	document.getElementById("type").innerHTML=jsonObject.type;
	document.getElementById("format").innerHTML=jsonObject.format;
	document.getElementById("transformerDelta").innerHTML=jsonObject.transformerDelta;
	document.getElementById("units").innerHTML=jsonObject.units;
	document.getElementById("frequency").innerHTML=jsonObject.frequency;
	document.getElementById("temperature").innerHTML=jsonObject.temperature;
	document.getElementById("description").innerHTML=jsonObject.description;
	
}