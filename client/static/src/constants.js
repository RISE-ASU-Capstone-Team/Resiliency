var Power = {
    LOAD : 0,
    SYNC_GENERATOR : 1,
    BUS : 2,
    UTILITY : 3,

    Con : {
        TRANSFORMER : 0,
        DIRECT : 1,
        CABLE : 2,
        OVERHEAD : 3,
        LINE_COLOR : '#E27A3F'
    }
};

var Water = {
    RESERVOIR: 4,
    Con : {
      PIPE: 4,
      LINE_COLOR : '#33A3ff'
    }
}

var Server = {
    HOSTNAME : 'localhost',
    PORT : '8000',
    ADDRESS : 'http://localhost:8000/',
}

var polylineOptions = {
  color: '#000000',
  weight: 6,
  opacity: 0.9
};

function isPowerConnection(type) {
  return (contains(Power.Con, type));
}

function isWaterConnection(type) {
  return (contains(Water.Con, type));
}

function nodeType(type){
    switch(type){
        case Power.LOAD:{
            return 'load';
        }
        case Power.SYNC_GENERATOR:{
            return 'genSynchronous'
        }
        case Power.BUS:{
            return  'bus'
        }
        case Power.UTILITY:{
            return  'utility'
        }
        case Water.RESERVOIR:{
            return  'reservoir'
        }
        default: {
            return 'load'
        }
    }
}

function nodeTypeDisplay(type){
    switch(type){
        case Power.LOAD:{
            return 'Load';
        }
        case Power.SYNC_GENERATOR:{
            return 'Synchronous Generator'
        }
        case Power.BUS:{
            return  'Bus'
        }
        case Power.UTILITY:{
            return  'Utility'
        }
        case Water.RESERVOIR:{
            return  'Reservoir'
        }
        default: {
            return 'Node'
        }
    }
}

function connectionType(type){
    switch(type){
        case Power.Con.TRANSFORMER:{
            return 'transformer';
        }
        case Power.Con.DIRECT:{
            return 'direct'
        }
        case Power.Con.CABLE:{
            return  'cable'
        }
        case Power.Con.OVERHEAD:{
            return  'overhead'
        }
        case Water.Con.PIPE:{
            return  'pipe'
        }
        default: {
            return 'connection'
        }
    }
}

function connectionTypeDisplay(type){
    switch(type){
        case Power.Con.TRANSFORMER:{
            return 'Two Winding Transformer';
        }
        case Power.Con.DIRECT:{
            return 'Direct Connection'
        }
        case Power.Con.CABLE:{
            return  'Cable'
        }
        case Power.Con.OVERHEAD:{
            return  'Overhead Line'
        }
        case Water.Con.PIPE:{
            return  'Pipe'
        }
        default: {
            return 'Connection'
        }
    }
}

function contains(array, value) {
  var found = false;
  for(var index in array) {
    if (array[index] == value) {
      found = true;
      break;
    }
  }

  return found;
};
