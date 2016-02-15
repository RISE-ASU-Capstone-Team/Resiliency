var Alert = (function ()
{
    "use strict";
    var instance;

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
      console.log(log_text);
    }

    Alert.warning = function(log_text) //Method for reporting warnings.
    {
      console.log("Warning: " + log_text);
    }

    Alert.error = function(log_text) //Method for reporting errors.
    {
      console.log("Error: " + log_text);
    }

    return Alert;
}());
