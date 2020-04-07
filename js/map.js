//overlay styles
overlaystyles = {
    "buildings": {
        "type": "solid",
        "styleFeature": "status",
        "styles": {
            "enemy": {
                "stroke": true,
                "color": "red",
                "weight": 3,
                "opacity": 1
            },
            "friendly": {
                "stroke": true,
                "color": "green",
                "weight": 3,
                "opacity": 1
            },
            "neutral": {
                "stroke": true,
                "color": "orange",
                "weight": 3,
                "opacity": 1
            },
            "unknown": {
                "stroke": true,
                "color": "black",
                "weight": 3,
                "opacity": 1
            }
        }
    },
    "elevation": {
        "type": "function"
    },
    "roads": {
        "type": "solid",
        "styleFeature": "Road Type",
        "styles": {
            "motorway": {
                "stroke": true,
                "color": "#f53b00",
                "weight": 4
            },
            "trunk": {
                "stroke": true,
                "color": "#f53b00",
                "weight": 4
            },
            "primary": {
                "stroke": true,
                "color": "#f50000",
                "weight": 3
            },
            "secondary": {
                "stroke": true,
                "color": "#f50000",
                "weight": 3
            },
            "tertiary": {
                "stroke": true,
                "color": "#f50000",
                "weight": 2
            },
            "unclassified": {
                "stroke": true,
                "color": "#f59400",
                "weight": 2
            },
            "residential": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "motorway_link": {
                "stroke": true,
                "color": "#f53b00",
                "weight": 4
            },
            "trunk_link": {
                "stroke": true,
                "color": "#f53b00",
                "weight": 4
            },
            "primary_link": {
                "stroke": true,
                "color": "#f50000",
                "weight": 3
            },
            "secondary_link": {
                "stroke": true,
                "color": "#f50000",
                "weight": 3
            },
            "tertiary_link": {
                "stroke": true,
                "color": "#f50000",
                "weight": 2
            },
            "living_street": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "service": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "pedestrian": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "track": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "footway": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "bridleway": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "steps": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "path": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 1
            },
            "cycleway": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "track_grade1": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "track_grade2": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "track_grade3": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "track_grade4": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "track_grade5": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            },
            "unknown": {
                "stroke": true,
                "color": "#032a4f",
                "weight": 2
            }
        }
    },
    "vegetation": {
        "type": "pattern",
        "styleFeature": "Vegetation Type",
        "styles": {
            "grassland": {
                "pattern": {
                    "angle": 0,
                    "weight": 1,
                    "color": "#185c29",
                    "opacity": 1
                },
                "color": "#185c29"
            },
            "shrubland": {
                "pattern": {
                    "angle": 25,
                    "weight": 3,
                    "color": "#274e31",
                    "opacity": 1
                },
                "color": "#274e31"
            },
            "woodland": {
                "pattern": {
                    "angle": 50,
                    "weight": 5,
                    "color": "#2d4232",
                    "opacity": 1
                },
                "color": "#2d4232"
            },
            "medium density forest": {
                "pattern": {
                    "angle": 75,
                    "weight": 6,
                    "color": "#344539",
                    "opacity": 1
                },
                "color": "#344539"
            },
            "high density forest": {
                "pattern": {
                    "angle": 90,
                    "weight": 7,
                    "color": "#000000",
                    "opacity": 1
                },
                "color": "#000000"
            },
            "unknown": {
                "pattern": {
                    "angle": 90,
                    "weight": 7,
                    "color": "#bf003b",
                    "opacity": 1
                },
                "color": "#bf003b"
            }
        }
    },
    "water": {
        "type": "solid",
        "styleFeature": "water body type",
        "styles": {
            "water": {
                "stroke": true,
                "color": "blue",
                "weight": 3,
                "opacity": 1
            },
            "river": {
                "stroke": true,
                "color": "blue",
                "weight": 3,
                "opacity": 1
            },
            "wetland": {
                "stroke": true,
                "color": "blue",
                "weight": 3,
                "opacity": 1
            },
            "reservoir": {
                "stroke": true,
                "color": "blue",
                "weight": 3,
                "opacity": 1
            },
            "dock": {
                "stroke": true,
                "color": "blue",
                "weight": 3,
                "opacity": 1
            },
            "unknown": {
                "stroke": true,
                "color": "blue",
                "weight": 3,
                "opacity": 1
            }
        }
    }
};

let mainMapHTML = "<div id=\"mapId\">\n" +
    "    <div id=\"modeSelection\">\n" +
    "        <div>MODES</div>\n" +
    "        <button type=\"button\" id=\"viewBtn\" onclick=\"viewMode()\">\n" +
    "            VIEW <i class=\"fas fa-minus\"></i>\n" +
    "        </button>\n" +
    "        <button type=\"button\" id=\"drawBtn\" onclick=\"drawMode()\">\n" +
    "            DRAW <i class=\"fas fa-minus\"></i>\n" +
    "        </button>\n" +
    "        <button type=\"button\" id=\"dataBtn\" onclick=\"dataMode()\">\n" +
    "            DATA <i class=\"fas fa-minus\"></i>\n" +
    "        </button>\n" +
    "    </div>\n" +
    "    <div id=\"legend\">\n" +
    "        <div>LEGEND</div>\n" +
    "        <div class=\"tab\">\n" +
    "            <button class=\"tabLinks\" id=\"defaultOpen\" onclick=\"showLegend(this, 'buildings_legend')\">Bu</button>\n" +
    "            <button class=\"tabLinks\" onclick=\"showLegend(this, 'roads_legend')\">Ro</button>\n" +
    "            <button class=\"tabLinks\" onclick=\"showLegend(this, 'vegetation_legend')\">Ve</button>\n" +
    "        </div>\n" +
    "\n" +
    "        <div id=\"buildings_legend\" class=\"tabContent\">\n" +
    "            <img alt=\"legend\" src=\"img/legend_building.png\">\n" +
    "        </div>\n" +
    "\n" +
    "        <div id=\"roads_legend\" class=\"tabContent\">\n" +
    "            <img alt=\"legend\" src=\"img/legend_roads.png\">\n" +
    "        </div>\n" +
    "\n" +
    "        <div id=\"vegetation_legend\" class=\"tabContent\">\n" +
    "            <img alt=\"legend\" src=\"img/legend_vegetation.png\">\n" +
    "        </div>\n" +
    "    </div>\n" +
    "</div>";

//get battlefield name
let battlefield = getBattlefieldName();
let lastDrawnShapeGeoJson;
let map;
let dataModeOn = false;
let viewModeOn = false;
//load overlays to map
loadOverlays();


function loadOverlays() {
    if(battlefield === undefined) {
        document.getElementById('parent-main-map').innerHTML = '<div id="mapId" style="background: linear-gradient(180deg, rgba(1,18,21,1) 0%, rgba(2,34,39,1) 75%, rgba(4,43,51,1) 100%);" ></div>';
        document.getElementById('logo-animation').style.visibility = 'visible';
        return;
    }
    document.getElementById('parent-main-map').innerHTML = mainMapHTML;
    document.getElementById('defaultOpen').click();
    // initiate map
    map = L.map(
        "mapId",
        {
            center: [7.796, 80.673],
            crs: L.CRS.EPSG3857,
            zoom: 7,
            zoomControl: true,
            preferCanvas: false,
        }
    );
    setMapBounds();
    // create the base map and add to map
    let openStreetMap = L.tileLayer(
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
    let satelliteMap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
    });

    // send XHR GET request to overlays endpoint to get all overlays.
    let xHttp = new XMLHttpRequest();
    xHttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let overlays = JSON.parse(this.responseText);
            let overlaysGeoJSON = {};
            // iterate all overlays
            overlays.forEach(function (overlay) {
                let geojson = L.geoJSON(overlay);
                // Add styles based on overlay
                geojson.setStyle(function (feature) {
                    //set water overlay depths
                    if (overlay.name === 'water') {
                        let depths = feature.properties.depths;
                        for (let depth in depths) {
                            if (depths.hasOwnProperty(depth) && depths[depth].length === 3) {
                                let marker = L.marker([depths[depth][0], depths[depth][1]]).addTo(map);
                                marker.on('click', function (e) {
                                    if (dataModeOn) {
                                        let popup = L.popup();
                                        let depth_form = "<div id=\"delete_water_depth\" ><button>" +
                                            "DELETE DEPTH</button></div>";
                                        popup
                                            .setLatLng(e.latlng)
                                            .setContent(depth_form)
                                            .openOn(map);
                                        setTimeout(() => {
                                             let delete_depth_button = document.getElementById('delete_water_depth').getElementsByTagName('button')[0];
                                            delete_depth_button.onclick = function () {
                                                showWaterDataDialog(feature, overlay.properties, "WATER", [], null, e.latlng);
                                            };
                                        },500);
                                    } else if (viewModeOn) {
                                        let popup = L.popup();
                                        let depth_form = "<a>Lat : " + e.latlng.lat + "</a><br>" +
                                            "<a>Long : " + e.latlng.lng + "</a><br>" +
                                            "<a>Depth : " + depths[depth][2] + "</a>";
                                        popup
                                            .setLatLng(e.latlng)
                                            .setContent(depth_form)
                                            .openOn(map);
                                    }

                                });
                            }
                        }
                    }
                    let style_type = overlaystyles[overlay.name].type;
                    if (style_type === 'solid') {
                        let styles = overlaystyles[overlay.name].styles;
                        let styleFeature = overlaystyles[overlay.name].styleFeature;
                        return styles[feature.properties[styleFeature]]
                    } else if (style_type === 'pattern') {
                        //pattern
                        let styles = overlaystyles[overlay.name].styles;
                        let styleFeature = overlaystyles[overlay.name].styleFeature;
                        let pattern = new L.StripePattern(styles[feature.properties[styleFeature]].pattern);
                        let color = styles[feature.properties[styleFeature]].color;
                        pattern.addTo(map);
                        return {fillPattern: pattern, color: color}
                    } else if (style_type === 'function') {
                        let opacity = (0.5 / 2525) * feature.properties.elevation + 0.5;
                        return {color: 'blue', "opacity": opacity, "weight": 1};
                    }
                });
                geojson.on('click', function (e) {
                    if (dataModeOn) {
                        if (overlay.name === 'water') {
                            let popup = L.popup();
                            let depth_form = "<div id=\"water_depth\" ><select class=\"form-control\">" +
                                "<option value=\"shallow\">shallow</option>" +
                                "<option value=\"deep\">deep</option></select>" +
                                "<button>" +
                                "<i class=\"fas fa-check\"></i></button></div>";
                            popup
                                .setLatLng(e.latlng)
                                .setContent(depth_form)
                                .openOn(map);

                             setTimeout(() => {
                                    let water_depth_div = document.getElementById('water_depth');
                                    let depth_select = water_depth_div.getElementsByTagName('select')[0];
                                    let depth_button = water_depth_div.getElementsByTagName('button')[0];
                                    depth_button.onclick = function () {
                                           showWaterDataDialog(e.layer.feature, overlay.properties, "WATER", e.latlng, depth_select.value, []);
                                    };
                             },500);
                        } else if (overlay.name === 'buildings') {
                            showBuildingRoadsVegetationDataDialog(e.layer.feature, overlay.properties, overlay.name, "BUILDING");
                        } else if (overlay.name === 'roads')
                            showBuildingRoadsVegetationDataDialog(e.layer.feature, overlay.properties, overlay.name, "VEGETATION");
                        else if (overlay.name === 'vegetation')
                            showBuildingRoadsVegetationDataDialog(e.layer.feature, overlay.properties, overlay.name, "ROAD");

                    } else if (viewModeOn) {
                        let popup = L.popup();
                        let viewHTML = getViewHTML(e.layer.feature);
                        popup
                            .setLatLng(e.latlng)
                            .setContent(viewHTML)
                            .openOn(map);
                    }
                });

                // add overlay to map
                geojson.addTo(map);
                // collect overlays to layer control
                overlaysGeoJSON[overlay.name] = geojson;
            });
            // display layer control
            let controller = L.control.layers(
                {
                    "openStreetMap": openStreetMap,
                    "Satellite map": satelliteMap
                },
                overlaysGeoJSON,
                {"autoZIndex": true, "collapsed": false, "position": "topright"}
            );
            controller.addTo(map);
            //Overlay selector style set
            controllerStyleSet();
            loadDrawerToolBox(map);
            initiateModeSelector();
        }else if(this.readyState === 4)
            showErrorsMessage("LOAD ERROR");
    };
    xHttp.open("GET", "http://127.0.0.1:8082/battlefields/" + battlefield + "/overlays", true);
    xHttp.send();
}

function setMapBounds() {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let bounds = JSON.parse(this.responseText);
            map.fitBounds([
                [bounds.top, bounds.left],
                [bounds.bottom, bounds.right]
            ]);
        }else if(this.readyState === 4)
            showErrorsMessage("LOAD ERROR");
    };
    request.open("GET", "http://127.0.0.1:8082/battlefields/" + battlefield, true);
    request.send();
}

function loadDrawerToolBox(map) {
    let options = {
        position: "topleft",
        draw: {
            "polyline": {"allowIntersection": false},
            circlemarker: false,
            circle: false
        },
        edit: {
            "poly": {"allowIntersection": false},
            edit: false,
            remove: false
        },
    };
    // FeatureGroup is to store editable layers.
    let drawnItems = new L.featureGroup().addTo(
        map
    );
    options.edit.featureGroup = drawnItems;
    new L.Control.Draw(
        options
    ).addTo(map);
    let layer;
    map.on(L.Draw.Event.CREATED, function () {
        drawnItems.addLayer(layer);
        $("#overlayTypeSelector").modal();
        lastDrawnShapeGeoJson = JSON.stringify(layer.toGeoJSON());
    });
    map.on('draw:drawstart', function () {
        map.addEventListener('mousemove', showCoordinates);
    });
    map.on('draw:drawstop ', function () {
        map.removeEventListener("mousemove", showCoordinates);
    });

    $('#overlayTypeSelector').on('hidden.bs.modal', function () {
        drawnItems.removeLayer(layer);
    })
}

function showCoordinates(ev) {
    // show coordinates as tool tip when drawing
    let lat = ev.latlng.lat;
    let lng = ev.latlng.lng;
    let coordinates = "" + lat + " ," + lng;
    L.drawLocal.draw.handlers.polygon.tooltip.cont = coordinates;
    L.drawLocal.draw.handlers.polygon.tooltip.end = coordinates;
}

function getBattlefieldName() {
    let vars = {};
    window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars["battlefield"];
}

let viewBtn;
let drawBtn;
let dataBtn;
let legend;
let tools;
let toolBar;

function initiateModeSelector() {
    //Mode selector
    viewBtn = document.getElementById('viewBtn');
    drawBtn = document.getElementById('drawBtn');
    dataBtn = document.getElementById('dataBtn');
    legend = document.getElementById('legend');
    tools = document.getElementById('tools');
    toolBar = document.getElementsByClassName('leaflet-draw-toolbar')[0];
    //select default mode
    viewBtn.click();
}

function viewMode() {
    modeStyleSet(viewBtn, drawBtn, dataBtn);
    legend.style.visibility = "visible";
    toolBar.style.visibility = "hidden";
    dataModeOn = false;
    viewModeOn = true;
}

function drawMode() {
    modeStyleSet(drawBtn, viewBtn, dataBtn);
    legend.style.visibility = "hidden";
    toolBar.style.visibility = "visible";
    dataModeOn = false;
    viewModeOn = false;
}

function dataMode() {
    modeStyleSet(dataBtn, drawBtn, viewBtn);
    legend.style.visibility = "hidden";
    toolBar.style.visibility = "hidden";
    dataModeOn = true;
    viewModeOn = false;
}

// Legend

function showLegend(button, overlayName) {
    let i, tabContent, tabLinks;
    tabContent = document.getElementsByClassName("tabContent");
    for (i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }
    tabLinks = document.getElementsByClassName("tabLinks");
    for (i = 0; i < tabLinks.length; i++) {
        tabLinks[i].className = tabLinks[i].className.replace(" active", "");
    }
    document.getElementById(overlayName).style.display = "block";
    button.className += " active";
}

function saveBuildingOverlay() {
    let lastDrawnShapeJson = JSON.parse(lastDrawnShapeGeoJson);
    if (lastDrawnShapeJson.geometry.type !== 'Polygon') {
        showErrorsMessage("OVERLAY TYPE MISMATCH");
    } else {
        lastDrawnShapeJson.properties = {
            "Building Type": "unknown",
            "No of occupants": "unknown",
            "status": "unknown",
            "Material": "unknown",
            "No of stories": 0
        };
        saveOverlay("POST", "buildings", lastDrawnShapeJson)
    }
}

function saveRoadsOverlay() {
    let lastDrawnShapeJson = JSON.parse(lastDrawnShapeGeoJson);
    if (lastDrawnShapeJson.geometry.type !== 'LineString') {
        showErrorsMessage("OVERLAY TYPE MISMATCH");
    } else {
        lastDrawnShapeJson.properties = {"Road Type": "unknown"};
        saveOverlay("POST", "roads", lastDrawnShapeJson)
    }
}

function saveVegetationOverlay() {
    let lastDrawnShapeJson = JSON.parse(lastDrawnShapeGeoJson);
    if (lastDrawnShapeJson.geometry.type !== 'Polygon') {
        showErrorsMessage("OVERLAY TYPE MISMATCH");
    } else {
        lastDrawnShapeJson.properties = {"Vegetation Type": "unknown"};
        saveOverlay("POST", "vegetation", lastDrawnShapeJson)
    }
}

function saveWaterOverlay() {
    let lastDrawnShapeJson = JSON.parse(lastDrawnShapeGeoJson);
    if (lastDrawnShapeJson.geometry.type === 'Point') {
        showErrorsMessage("OVERLAY TYPE MISMATCH");
    } else {
        lastDrawnShapeJson.properties = {"water body type": "unknown", "depths": []};
        saveOverlay("POST", "water", lastDrawnShapeJson)
    }
}

function saveOverlay(request_type, overlayName, geojsonFeature) {
    let request = new XMLHttpRequest();
    let url = "";
    let success_message = "";
    if (request_type === 'POST') {
        success_message = "SAVE SUCCESSFUL";
        url = "http://127.0.0.1:8082/battlefields/" + battlefield + "/overlays/" + overlayName + "/features";
    } else if (request_type === 'PUT') {
        success_message = "EDIT SUCCESSFUL";
        url = "http://127.0.0.1:8082/battlefields/" + battlefield + "/overlays/" + overlayName + "/features/" + geojsonFeature.id;
    }
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 201) {
            showSuccessMessage(success_message);
            //reload the screen
            loadOverlays();
        }else if(this.readyState === 4)
            showErrorsMessage("UNSUCCESSFUL");
    };
    request.open(request_type, url, true);
    request.setRequestHeader("Content-type", "application/json");
    request.send(JSON.stringify(geojsonFeature));
}

function deleteOverlay(overlayName, id) {
    let request = new XMLHttpRequest();
    let url = "http://127.0.0.1:8082/battlefields/" + battlefield + "/overlays/" + overlayName + "/features/" + id;
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 201) {
            showSuccessMessage("DELETE SUCCESSFUL");
            //reload the screen
            loadOverlays();
        }else if(this.readyState === 4)
            showErrorsMessage("UNSUCCESSFUL");
    };
    request.open("DELETE", url, true);
    request.send();
}

function createNewBattlefield(json_body) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function () {
       let logoAnimation = $('#logo-animation');
       logoAnimation.hide();
       let loadingModal = $('#loading-modal');
       loadingModal.modal({
            backdrop: 'static',
            keyboard: false
        });
        if (this.readyState === 4 && this.status === 201) {
            window.open("map.html?battlefield="+json_body.name, "_self");
        }else if(this.readyState === 4){
            loadingModal.modal('hide');
            logoAnimation.show();
            showErrorsMessage("UNSUCCESSFUL");
        }
    };
    request.open("POST", "http://127.0.0.1:8082/battlefields" , true);
    request.setRequestHeader("Content-type", "application/json");
    request.send(JSON.stringify(json_body));
}


function showBuildingRoadsVegetationDataDialog(layer, properties, overlayName, header) {
    $("#dataModeBox").modal();
    document.getElementById('data-mode-header').innerHTML = header + " <i class=\"fas fa-minus\"></i>";
    document.getElementById('dm-body').innerHTML = getFormHTML(layer, properties);
    let gif = document.getElementById('dm-gif').children[0];
    gif.src = "img/" + overlayName + "_anim.gif";
    document.getElementById('save_edited_feature').onclick = function () {
        let layer_properties = {};
        for (let property in layer.properties) {
            if (layer.properties.hasOwnProperty(property))
                layer_properties[property] = document.getElementById(property.replace(/\s/g, '_')).value;
        }
        let feature_new = {
            "type": layer.type,
            "id": layer.id,
            "properties": layer_properties,
            "geometry": layer.geometry
        };
        saveOverlay("PUT", overlayName, feature_new);
    };
    document.getElementById('delete_feature').onclick = function () {
        deleteOverlay(overlayName, layer.id);
    };
}

function showWaterDataDialog(layer, properties, header, coords_add, depth, coords_del) {
    $("#dataModeBox").modal();
    let coordinate_description = "";
    let depths_new;
    if (coords_add.length === 0) {
        //   after delete depth
        coordinate_description = "<a>REMOVED DEPTH COORDINATE</a>\n" +
            "<br><a style=\"color: #8affbd !important;\">" + coords_del.lat + ", " + coords_del.lng + "</a><br>";
        depths_new = remove_depth(layer.properties.depths, coords_del);
    } else if (coords_del.length === 0) {
        //   after add depth
        coordinate_description = "<a>NEW DEPTH COORDINATE</a>\n" +
            "<br><a style=\"color: #8affbd !important;\">" + coords_add.lat + ", " + coords_add.lng + "</a><br>";
        depths_new = add_depth(layer.properties.depths, coords_add, depth);
    }
    document.getElementById('data-mode-header').innerHTML = header + " <i class=\"fas fa-minus\"></i>";
    document.getElementById('dm-body').innerHTML = coordinate_description + getFormHTML(layer, properties);
    let gif = document.getElementById('dm-gif').children[0];
    gif.src = "img/water_anim.gif";
    document.getElementById('save_edited_feature').onclick = function () {
        let layer_properties = {};
        layer_properties['water body type'] = document.getElementById('water_body_type').value;
        layer_properties['depths'] = depths_new;
        let feature_new = {
            "type": layer.type,
            "id": layer.id,
            "properties": layer_properties,
            "geometry": layer.geometry
        };
        saveOverlay("PUT", "water", feature_new);
    };
    document.getElementById('delete_feature').onclick = function () {
        deleteOverlay("water", layer.id);
    };
}

function remove_depth(depths_array, coord) {
//    return a new array without depth with given coord
    let new_array = [];
    for (let depth in depths_array) {
        if (depths_array.hasOwnProperty(depth) && (depths_array[depth][0] !== coord.lat || depths_array[depth][1] !== coord.lng))
            new_array.push(depths_array[depth]);
    }
    return new_array;
}

function add_depth(depths_array, coord, depth) {
//    return a new array after adding given coord
    let new_array = [];
    for (let old_depth in depths_array) {
        if (depths_array.hasOwnProperty(old_depth)) {
            new_array.push(depths_array[old_depth]);
        }
    }
    new_array.push([coord.lat, coord.lng, depth]);
    return new_array;
}

function getFormHTML(layer, properties) {
    let formHTML = "";
    let propertyListOptions = properties['attributes_options'];
    for (let property in propertyListOptions) {
        if(propertyListOptions.hasOwnProperty(property)){
            let propertyName = propertyListOptions[property].name;
        let optionElementHTML = "<a>" + propertyName + "</a>" +
            "<select id=\"" + propertyName.replace(/\s/g, '_') + "\" class=\"form-control\">";
        let optionList = propertyListOptions[property].options;
        for (let option in optionList) {
            if(optionList.hasOwnProperty(option)){
                let optionName = optionList[option];
                let selectedWord = "";
                if (layer.properties[propertyName] === optionName)
                    selectedWord = "selected";
                let optionHTML = "<option value=\"" + optionName + "\" " + selectedWord + ">" + optionName + "</option>";
                optionElementHTML += optionHTML;
            }
        }
        optionElementHTML = optionElementHTML + "</select>";
        formHTML += optionElementHTML;
        }
    }
    let propertyListDirect = properties['attributes_direct'];
    for (let property in propertyListDirect) {
        if(propertyListDirect.hasOwnProperty(property)){
            let propertyName = propertyListDirect[property].name;
            let inputType = propertyListDirect[property].type;
            let inputElementHTML = "<a>" + propertyName + "</a>" +
                "<input type=\"" + inputType + "\" class=\"form-control\" value=\"" + layer.properties[propertyName] + "\" id= \"" + propertyName.replace(/\s/g, '_') + "\">";
            formHTML += inputElementHTML;
        }
    }
    return formHTML;
}

function getViewHTML(layer) {
    let viewHTML = "";
    for (let property in layer.properties) {
        if (layer.properties.hasOwnProperty(property) && property !== 'depths') {
            let optionElementHTML = "<a>" + property + " : " + layer.properties[property] + "</a><br>";
            viewHTML += optionElementHTML;
        }
    }
    return viewHTML;
}

let map2;

function showNewMapWindow() {
    let coords = null;
    let newMapModal = $("#newMapModal");
    newMapModal.modal();

    setTimeout(() => {
        map2 = L.map(
            "new-map-mapId",
            {
                center: [7.796, 80.673],
                zoom: 7,
                zoomControl: true,
                preferCanvas: false
            }
        );

        L.tileLayer.grayscale(
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
        ).addTo(map2);

        let options = {
            position: "topleft",
            draw: {
                rectangle: {
                    shapeOptions: {
                        color: '#368e95'
                    }
                },
                circlemarker: false,
                circle: false,
                marker:false,
                polygon:false,
                polyline:false
            },
            edit: {
                "poly": {"allowIntersection": false},
                edit: false,
                remove: false
            }
        };
        // FeatureGroup is to store editable layers.
        let drawnItems = new L.featureGroup().addTo(
            map2
        );
        options.edit.featureGroup = drawnItems;
        new L.Control.Draw(
            options
        ).addTo(map2);
        let old_layer = null;
        map2.on(L.Draw.Event.CREATED, function (e) {
            coords = e.layer.toGeoJSON();
            old_layer = e.layer;
            drawnItems.addLayer(e.layer);
        });
        map2.on('draw:drawstart', function () {
            if(old_layer !== null)
                drawnItems.removeLayer(old_layer);
        });
    }, 500);

    newMapModal.on('hidden.bs.modal', function () {
        document.getElementById('map-parent').innerHTML = '<div id = "new-map-mapId" ></div>';
    });

    document.getElementById('save_new_map').onclick = function () {
        let name = document.getElementById("battlefield-name").value;
        if(name.trim() === "" ||  coords === null){
            showErrorsMessage("INPUTS ARE INCORRECT")
        }else{
            let jsonBody = {
                "name": name,
                "top" : coords.geometry.coordinates[0][1][1],
                "left" : coords.geometry.coordinates[0][1][0],
                "bottom" : coords.geometry.coordinates[0][3][1],
                "right": coords.geometry.coordinates[0][3][0]
            };
            createNewBattlefield(jsonBody);
        }
    };

}

function showOpenMapWindow(){
    let battlefield_selector;
    let request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            $("#openMapModal").modal();
            let element = '';
            for (let battlefield of JSON.parse(this.response)) {
                element = element + '<option>' + battlefield + '</option>';
            }
            battlefield_selector = document.getElementById('battlefield-select');
            battlefield_selector.innerHTML = element;
        }else if(this.readyState === 4)
            showErrorsMessage("SERVER NOT FOUND");
    };
    request.open("GET", "http://127.0.0.1:8082/battlefields", true);
    request.setRequestHeader("Content-type", "application/json");
    request.send();

    document.getElementById('open_map').onclick = function () {
        window.open("map.html?battlefield="+battlefield_selector.value, "_self");
    };
}

function showSuccessMessage(message) {
    $("#success-modal").modal();
    document.getElementById("success-modal-body").children[1].innerHTML = message;
}

function showErrorsMessage(message) {
    $("#warning-modal").modal();
    document.getElementById("warning-modal-body").children[1].innerHTML = message;
    document.getElementsByTagName('body')[0].style.backgroundColor = '#ff8181';
    $('#warning-modal').on('hidden.bs.modal', function () {
        document.getElementsByTagName('body')[0].style.backgroundColor = '#a4ead1';
    })
}