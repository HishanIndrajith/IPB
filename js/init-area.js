// center of the map
var center = [7.253261904540173, 80.59216260910034];
// Create the map
var map2=null;
var drawPluginOptions;
var drawnItems;
var editableLayers;
var layer;
var coords;


$('#newProject').click(function () {
    $("#loading").hide();

    setTimeout(function () {
        map2 = L.map(
            "map2",
            {
                center: [7.253261904540173, 80.59216260910034],
                zoom: 8,
                zoomControl: true,
                preferCanvas: false
            }
        );

// Set up the OSM layer
        L.tileLayer(
            'http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                maxZoom: 18,

            }).addTo(map2);

        drawPluginOptions = {
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
        drawnItems = new L.featureGroup().addTo(
            map2
        );
        drawPluginOptions.edit.featureGroup = drawnItems;
// Initialise the FeatureGroup to store editable layers
        editableLayers = new L.FeatureGroup();
        map2.addLayer(editableLayers);

        map2.on(L.Draw.Event.CREATED, function(e) {
            layer = e.layer;
            type = e.layerType;
            coords = layer.toGeoJSON();
            drawnItems.addLayer(layer);
        });
        map2.on('draw:created', function(e) {
            drawnItems.addLayer(e.layer);
        });

// Initialise the draw control and pass it the FeatureGroup of editable layers
        var drawControl = new L.Control.Draw(drawPluginOptions);
        map2.addControl(drawControl);

        editableLayers = new L.FeatureGroup();
        map2.addLayer(editableLayers);

        map2.on('draw:created', function(e) {
            var type = e.layerType,
                layer = e.layer;

            if (type === 'marker') {
                layer.bindPopup('A popup!');
            }

            editableLayers.addLayer(layer);
        });

    }, 1000)
    // $("#loading-spinner").show();

});

function CreateNewProject(){
    document.getElementById("map").style.zIndex = "-1";
    document.getElementById("spinner").style.display="block";
    var element = document.getElementById("exampleInputProjectName");
    var name = element.value;
    // var name = document.getElementById('name').value;
    var jsonBody = {
        "top" : coords.geometry.coordinates[0][1][1],
        "left" : coords.geometry.coordinates[0][1][0],
        "bottom" : coords.geometry.coordinates[0][3][1],
        "right": coords.geometry.coordinates[0][3][0]
    };
    console.log(name);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 201) {
            window.open("index.html?battlefield="+name, "_self");
            //window.location = "map.html?battlefield="+name;
        }
    };
    xhttp.open("POST", "http://127.0.0.1:8082/battlefields/" + name , true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(JSON.stringify(jsonBody));
}

