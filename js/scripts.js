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

    loadOverlays();
	loadDrawerToolBox();


    function loadDrawerToolBox(){
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
	    map.on(L.Draw.Event.CREATED, function (e) {
	        var layer = e.layer,
	            type = e.layerType;
	        var coords = JSON.stringify(layer.toGeoJSON());
	        layer.on('click', function () {
	            console.log(coords);
	        });
	        drawnItems.addLayer(layer);
	    });
	    map.on('draw:created', function (e) {
	        drawnItems.addLayer(e.layer);
	        $("#myModal").modal();
	    });


    }

	function loadOverlays() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                var overlays = JSON.parse(this.responseText);
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
        xhttp.open("GET", "http://127.0.0.1:8080/overlays", true);
        xhttp.send();
    }

    function addProperties(){
    	type = document.getElementById('overlayType').value;
    	if(type ==='Water'){
    		//popup-body
    		alert(type);
    	}

    }