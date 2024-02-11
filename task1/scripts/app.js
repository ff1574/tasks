// declaring constants for the data URL, the map target, the center coordinates and the zoom level
const DATA_URL = 'data/polygon.json';
const MAP_TARGET = 'map';
const CENTER_COORDINATES = [17.385044, 46.055556];
const ZOOM_LEVEL = 10;

// function to fetch the polygon data from the file
function fetchData(url) {
  return fetch(url)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .catch(error => console.error('Error fetching the polygon data:', error));
}

// function to create a polygon feature from the coordinates
function createPolygonFeature(coordinates) {
  const polygonCoordinates = coordinates.map(coord => ol.proj.fromLonLat(coord));
  return new ol.Feature({
    geometry: new ol.geom.Polygon([polygonCoordinates])
  });
}

// function to initialize the map with the layers and the view
function initializeMap(target, layers, view) {
  return new ol.Map({
    target,
    layers,
    view
  });
}

// function to create a text overlay with a given position, text and rotation
function createTextOverlay(position, text, rotationDegrees) {
  const element = document.createElement('div');
  element.innerHTML = text;
  element.style.transform = `rotate(${rotationDegrees}deg)`;
  return new ol.Overlay({
    element,
    position,
    positioning: 'center-center'
  });
}


// function to fetch the data, create the polygon feature, initialize the map and add the text overlay
fetchData(DATA_URL)
  .then(data => {
    const polygonFeature = createPolygonFeature(data.polygon);
    // Create a vector source and layer with the polygon feature
    const vectorSource = new ol.source.Vector({
      features: [polygonFeature]
    });
    const vectorLayer = new ol.layer.Vector({
      source: vectorSource
    });
    // Create an OSM layer and initialize the map with the layers and the view
    const mapLayer = new ol.layer.Tile({
      source: new ol.source.OSM()
    });
    const view = new ol.View({
      center: ol.proj.fromLonLat(CENTER_COORDINATES),
      zoom: ZOOM_LEVEL
    });
    // initialize the map with the layers and the view
    const map = initializeMap(MAP_TARGET, [mapLayer, vectorLayer], view);
    map.getView().fit(vectorSource.getExtent(), { padding: [100, 100, 100, 100] });

    // Create a text overlay and add it to the map
    const textOverlay = createTextOverlay(ol.proj.fromLonLat(data.polygon[0]), 'Give me a job pls', 39);
    map.addOverlay(textOverlay);

    // set the position of the text overlay and set it 
    const textCoordinates = [15.9, 45.6];
    const newPosition = ol.proj.fromLonLat(textCoordinates);
    textOverlay.setPosition(newPosition);
  });
