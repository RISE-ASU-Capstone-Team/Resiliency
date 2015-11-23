var path = "/"; // STUDENT: set to "" to run on your computer, "/" for submitting code to Udacity

var camera, scene, renderer;
var cameraControls;
var clock = new THREE.Clock();

function fillScene() {
  scene = new THREE.Scene();

  var myPolygon = new SquareGeometry();
  var texture = THREE.ImageUtils.loadTexture('phx.jpg');
  texture.wrapS = THREE.ClampToEdgeWrapping;
  texture.wrapT = THREE.ClampToEdgeWrapping;
  var myPolygonMaterial = new THREE.MeshBasicMaterial({
    map: texture
  });
  var polygonObject = new THREE.Mesh(myPolygon, myPolygonMaterial);
  scene.add(polygonObject);
}

function SquareGeometry() {
  var geo = new THREE.PlaneGeometry(100, 100);

  return geo;
}

function addToDOM() {
  var container = document.getElementById('container');
  var canvas = container.getElementsByTagName('canvas');
  if (canvas.length > 0) {
    container.removeChild(canvas[0]);
  }
  container.appendChild(renderer.domElement);
}

function animate() {
  window.requestAnimationFrame(animate);
  render();
}

function render() {
  var delta = clock.getDelta();
  cameraControls.update(delta);
  renderer.render(scene, camera);
}

function init() {
  var canvasWidth = window.innerWidth - 375;
  var canvasHeight = window.innerHeight - 150;


  var canvasRatio = canvasWidth / canvasHeight;

  renderer = new THREE.WebGLRenderer({
    antialias: true
  });
  renderer.gammaInput = true;
  renderer.gammaOutput = true;
  renderer.setSize(canvasWidth, canvasHeight);

  // Camera: Y up, X right, Z up
  camera = new THREE.PerspectiveCamera(30, canvasWidth / canvasHeight, 1, 10000);
  camera.position.set(0, 0, 100);

  // CONTROLS
  cameraControls = new THREE.OrbitAndPanControls(camera, renderer.domElement);
  cameraControls.target.set(0, 0, 0);
}

$("#hamburger").click(function()
{
  $('nav').css('opacity', 1);

  //Push content off-page with same width rather than squeezing in remaining space.
  var contentWidth = $('#content').width();
  $('#content').css('width', contentWidth);

  $('#contentLayer').css('display', 'block');
  $('#container').css('pointer-events', 'none');
  //disable all scrolling on mobile devices while menu is shown
  $('#body').bind('touchmove', function(e) {
    e.preventDefault()
  });

  //set margin for the whole container with a jquery UI animation
  $("#body").animate({
    "marginLeft": "30%"
  }, {
    duration: 70
  });

  $("#contentLayer").click(function() {

    //enable all scrolling on mobile devices when menu is closed
    $('#body').unbind('touchmove');

    //set margin for the whole container back to original state with a jquery UI animation
    $("#body").animate({
      "marginLeft": "-1"
    }, {
      duration: 70,
      complete: function() {
        $('#content').css('width', 'auto');
        $('#contentLayer').css('display', 'none');
        $('#container').css('pointer-events', 'auto');
        $('nav').css('opacity', 0);
        $('#content').css('min-height', 'auto');

      }
    });
  });

});

try {
  init();
  fillScene();
  addToDOM();
  animate();
} catch (e) {
  var errorReport = "Your program encountered an unrecoverable error, can not draw on canvas. Error was:<br/><br/>";
  $('#container').append(errorReport + e);
}
