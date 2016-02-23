var Alert = (function ()
{
    "use strict";
    var instance;
    var log_element = document.getElementById("logged_information");
    var log_ticker_element = document.getElementById("log_ticker");


    function Alert()
    {
        if (!instance)
        {
          instance = this;
        }
        return instance;
    }

    Alert.getInstance = function ()
    {
        return instance || new Alert();
    }

    Alert.log = function(log_text) //Method for reporting general alerts.
    {
      let output = log_text;
      log_ticker_element.innerHTML = output;
      log_element.innerHTML = output + "</br>" + log_element.innerHTML;
      console.log(log_text);
    }

    Alert.warning = function(log_text) //Method for reporting warnings.
    {
      let output = "Warning: " + log_text;
      log_ticker_element.innerHTML = output;
      log_element.innerHTML = output + "</br>" + log_element.innerHTML;
      console.log(output);
    }

    Alert.error = function(log_text) //Method for reporting errors.
    {
      let output = "Error: " + log_text;
      log_ticker_element.innerHTML = output;
      log_element.innerHTML = output + "</br>" + log_element.innerHTML;
      console.log(output);
    }

    return Alert;
}());
