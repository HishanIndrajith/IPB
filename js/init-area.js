// center of the map
var center = [7.253261904540173, 80.59216260910034];

// Create the map
var map = L.map(
    "map",
    {
        center: [7.253261904540173, 80.59216260910034],
        crs: L.CRS.EPSG3857,
        zoom: 8,
        zoomControl: true,
        preferCanvas: false,
    }
);

// Set up the OSM layer
L.tileLayer(
  'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Data © <a href="http://osm.org/copyright">OpenStreetMap</a>',
    maxZoom: 18,

  }).addTo(map);

// Initialise the FeatureGroup to store editable layers
var editableLayers = new L.FeatureGroup();
map.addLayer(editableLayers);

var drawPluginOptions = {
  position: 'topright',
  draw: {
    polygon: {
      allowIntersection: false, // Restricts shapes to simple polygons
      drawError: {
        color: '#e1e100', // Color the shape will turn when intersects
        message: '<strong>Oh snap!<strong> you can\'t draw that!' // Message that will show when intersect
      },
      shapeOptions: {
        color: '#97009c'
      }
    },
    // disable toolbar item by setting it to false
    polyline: false,
    circle: false, // Turns off this drawing tool
    rectangle: true,
    marker: true,
    polygon: false,
    circlemarker: false,
    },
  edit: {
    featureGroup: editableLayers, //REQUIRED!!
    remove: false
  }
};
var drawnItems = new L.featureGroup().addTo(
                map
         );
            drawPluginOptions.edit.featureGroup = drawnItems;

map.on(L.Draw.Event.CREATED, function(e) {
                var layer = e.layer,
                    type = e.layerType;
                var coords = layer.toGeoJSON();
                layer.on('click', function() {
                    alert(coords);
                    console.log(coords.geometry.coordinates[0]);
                    console.log(coords.geometry.coordinates[0][0][0]);
                    var
                        name = "bf1";
                    // var name = document.getElementById('name').value;
                      var jsonBody = {
                            "top" : coords.geometry.coordinates[0][0][0],
                            "left" : coords.geometry.coordinates[0][0][1],
                            "bottom" : coords.geometry.coordinates[0][2][0],
                            "right": coords.geometry.coordinates[0][2][1]
                      };
                      console.log(jsonBody);
                      var xhttp = new XMLHttpRequest();
                      xhttp.onreadystatechange = function () {
                            if (this.readyState == 4 && this.status == 201) {
                                // hide popup and reload the folder
                                top = 7.268736;
                                left = 80.585189;
                                bottom = 7.250260;
                                right = 80.612311;
                                window.location = "map.html?battlefield="+name;
                            }
                      };
                      xhttp.open("POST", "http://127.0.0.1:8082/battlefields/" + name , true);
                      xhttp.setRequestHeader("Content-type", "application/json");
                      xhttp.send(JSON.stringify(jsonBody));
                });
                drawnItems.addLayer(layer);
             });
            map.on('draw:created', function(e) {
                drawnItems.addLayer(e.layer);
            });

// Initialise the draw control and pass it the FeatureGroup of editable layers
var drawControl = new L.Control.Draw(drawPluginOptions);
map.addControl(drawControl);

var editableLayers = new L.FeatureGroup();
map.addLayer(editableLayers);

map.on('draw:created', function(e) {
  var type = e.layerType,
    layer = e.layer;

  if (type === 'marker') {
    layer.bindPopup('A popup!');
  }

  editableLayers.addLayer(layer);
});
