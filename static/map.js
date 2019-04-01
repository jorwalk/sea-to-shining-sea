var map = new ol.Map({
  layers: [
    new ol.layer.Tile({
      source: new ol.source.Stamen({
        layer: 'terrain'
      })
    })
  ],
  target: 'map',
  view: new ol.View({
    center: ol.proj.fromLonLat([-98.5795, 39.828175]),
    zoom: 4
  })
});

var style = new ol.style.Style({
  stroke: new ol.style.Stroke({
    color: '#000',
    width: 2
  })
});

var flightsSource = new ol.source.Vector({
  wrapX: false,
  loader: function() {
    var url = 'flight-data';
    fetch(url).then(function(response) {
      return response.json();
    }).then(function(json) {
      var flightsData = json.flights;
      for (var i = 0; i < flightsData.length; i++) {
        var flight = flightsData[i];
        var from = flight[0];
        var to = flight[1];

        // create an arc circle between the two locations
        var arcGenerator = new arc.GreatCircle({
          x: from[1],
          y: from[0]
        }, {
          x: to[1],
          y: to[0]
        });

        var arcLine = arcGenerator.Arc(100, {
          offset: 10
        });
        if (arcLine.geometries.length === 1) {
          var line = new ol.geom.LineString(arcLine.geometries[0].coords);
          line.transform('EPSG:4326', 'EPSG:3857');

          var feature = new ol.Feature({
            geometry: line,
            finished: false
          });
          // add the feature with a delay so that the animation
          // for all features does not start at the same time
          addLater(feature, i * 50);
        }
      }
      map.on('postcompose', animateFlights);
    });
  }
});


var flightsLayer = new ol.layer.Vector({
  source: flightsSource,
  style: function(feature) {
    // if the animation is still active for a feature, do not
    // render the feature with the layer style
    if (feature.get('finished')) {
      return style;
    } else {
      return null;
    }
  }
});

map.addLayer(flightsLayer);

var pointsPerMs = 0.1;

function animateFlights(event) {
  var vectorContext = event.vectorContext;
  var frameState = event.frameState;
  vectorContext.setStyle(style);

  var features = flightsSource.getFeatures();
  for (var i = 0; i < features.length; i++) {
    var feature = features[i];
    if (!feature.get('finished')) {
      // only draw the lines for which the animation has not finished yet
      var coords = feature.getGeometry().getCoordinates();
      var elapsedTime = frameState.time - feature.get('start');
      var elapsedPoints = elapsedTime * pointsPerMs;

      if (elapsedPoints >= coords.length) {
        feature.set('finished', true);
      }

      var maxIndex = Math.min(elapsedPoints, coords.length);
      var currentLine = new ol.geom.LineString(coords.slice(0, maxIndex));

      // directly draw the line with the vector context
      vectorContext.drawGeometry(currentLine);
    }
  }
  // tell OpenLayers to continue the animation
  map.render();
}

function addLater(feature, timeout) {
  window.setTimeout(function() {
    feature.set('start', new Date().getTime());
    flightsSource.addFeature(feature);
  }, timeout);
}