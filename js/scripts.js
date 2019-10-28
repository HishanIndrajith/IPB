
$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar, #content').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });


});


var map = L.map(
    "map",
    {
        center: [7.253261904540173, 80.59216260910034],
        crs: L.CRS.EPSG3857,
        zoom: 30,
        zoomControl: true,
        preferCanvas: false,
    }
);
var overlays = {}
var popup1_not_closed = false;
var lastDrawnShape;
var overlaySelected;

loadOverlays();
loadDrawerToolBox();

function loadOverlays() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            overlays = JSON.parse(this.responseText);
            var tile_layer = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {
                    "attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.",
                    "detectRetina": false,
                    "maxNativeZoom": 18,
                    "maxZoom": 18,
                    "minZoom": 0,
                    "noWrap": false,
                    "opacity": 1,
                    "subdomains": "abc",
                    "tms": false
                }
            ).addTo(map);
            var layer_control = {
                base_layers: {
                    "openstreetmap": tile_layer,
                },
                overlays: {},
            };
            for (i in overlays) {
                var geojson = L.geoJSON(overlays[i]);
                geojson.addTo(map);
                layer_control.overlays[overlays[i].name] = geojson;
            }
            L.control.layers(
                layer_control.base_layers,
                layer_control.overlays,
                {"autoZIndex": true, "collapsed": false, "position": "topright"}
            ).addTo(map);
        }
    };
    xhttp.open("GET", "http://127.0.0.1:8082/overlays", true);
    xhttp.setRequestHeader('Access-Control-Allow-Origin', 'http://localhost:63343');
    xhttp.send();
}

function loadDrawerToolBox() {
    var options = {
        position: "topleft",
        draw: {"polyline": {"allowIntersection": false}},
        edit: {"poly": {"allowIntersection": false}},
    }
    // FeatureGroup is to store editable layers.
    var drawnItems = new L.featureGroup().addTo(
        map
    );
    options.edit.featureGroup = drawnItems;
    var draw_control = new L.Control.Draw(
        options
    ).addTo(map);
    var layer;
    map.on(L.Draw.Event.CREATED, function (e) {
        popup1_not_closed = false;
        layer = e.layer,
            type = e.layerType;

        // layer.on('click', function () {
        //     console.log(coords);
        // });
        drawnItems.addLayer(layer);
    });
    map.on('draw:created', function (e) {
        $("#myModal").modal();
        lastDrawnShape = JSON.stringify(layer.toGeoJSON());
        modalContentSet(0);
    });

    $('#myModal').on('hidden.bs.modal', function () {
        if (!popup1_not_closed) {
            drawnItems.removeLayer(layer);
        }
    })

}

function addProperties() {
    // Get selected overlay type
    type = document.getElementById('overlayType').value;
    overlaySelected = overlays[type];
    if (overlay.name === "Water") {
        modalContentSet(1)
    } else {
        modalContentSet(2)
    }
}

function saveShape() {
    popup1_not_closed = true;
    var propertyObj = {};
    var propertyListOptions = overlaySelected.properties.answers_options;
    for (property in propertyListOptions) {
        var optionName = propertyListOptions[property].name;
        propertyObj[optionName] = document.getElementById(optionName).value;
    }
    var propertyListDirect = overlaySelected.properties.answers_direct;
    for (property in propertyListDirect) {
        var propertyName = propertyListDirect[property].name;
        propertyObj[propertyName] = document.getElementById(propertyName).value;
    }
    shapeObj = JSON.parse(lastDrawnShape);
    shapeObj.properties = propertyObj;
    var propertyJson = JSON.stringify(shapeObj);
    console.log(propertyJson);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("POST", "http://127.0.0.1:8082/overlays/" + overlaySelected.name, true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader('Access-Control-Allow-Origin', 'http://localhost:63343');
    xhttp.send(propertyJson);
    $("#myModal").modal('hide');
}

function modalContentSet(step) {
    var form = document.getElementById('popup-body')
    var modelHeading = document.getElementById('modelHeading')
    var modalFooter = document.getElementById('modal-footer')
    if (step === 0) {
        var optionHTML = "";
        for (overlay in overlays) {
            var option = "<option value=\"" + overlay + "\">" + overlays[overlay].name + "</option>";
            optionHTML += option;
        }
        modelHeading.innerHTML = "Select Overlay Type";
        form.innerHTML = "<label>Overlay Type</label>" +
            "<select id=\"overlayType\" class=\"form-control\">" +
            optionHTML +
            "</select>";

        modalFooter.innerHTML = " <button type=\"button\" class=\"btn btn-secondary\" data-dismiss=\"modal\">Close</button>" +
            "<button type=\"button\" class=\"btn btn-primary\" id = \"submitbtn\" onclick=\"addProperties()\">Next</button>";
    } else if (step === 1) {
        form.innerHTML = "Water Overlay";
    } else if (step === 2) {
        var formHTML = "";
        var propertyListOptions = overlaySelected.properties.answers_options;
        for (property in propertyListOptions) {
            var optionName = propertyListOptions[property].name;
            var optionElementHTML = "<label>" + optionName + "</label>" +
                "<select id=\"" + optionName + "\" class=\"form-control\">";
            var optionList = propertyListOptions[property].options;
            for (option in optionList) {
                var optionHTML = "<option value=\"" + optionList[option] + "\">" + optionList[option] + "</option>";
                optionElementHTML += optionHTML;
            }
            optionElementHTML = optionElementHTML + "</select>";
            formHTML += optionElementHTML;
        }
        var propertyListDirect = overlaySelected.properties.answers_direct;
        for (property in propertyListDirect) {
            var propertyName = propertyListDirect[property].name;
            var inputType = propertyListDirect[property].type;
            var inputElementHTML = "<label>" + propertyName + "</label>" +
                "<input type=\"" + inputType + "\" class=\"form-control\" id= \"" + propertyName + "\">";
            formHTML += inputElementHTML;
        }
        modelHeading.innerHTML = "Add " + overlaySelected.name + " properties";
        form.innerHTML = formHTML;
        modalFooter.innerHTML = " <button type=\"button\" class=\"btn btn-secondary\" data-dismiss=\"modal\">Close</button>" +
            "<button type=\"button\" class=\"btn btn-primary\" id = \"submitbtn\" onclick=\"saveShape()\">Save</button>";
    }

}
