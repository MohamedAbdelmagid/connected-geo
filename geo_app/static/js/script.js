let map = L.map("map").setView([15.5007, 32.5599], 8)
let layerOSM = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png")
map.addLayer(layerOSM)

let marker = L.marker([15.5007, 32.5599], {
  draggable: true,
  title: "Khartoum",
  opacity: 0.5
}).addTo(map)
marker.bindPopup("<h2>Khartoum Location</h2>").openPopup()

let OpenStreetMap_BZH = L.tileLayer('https://tile.openstreetmap.bzh/br/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles courtesy of <a href="http://www.openstreetmap.bzh/" target="_blank">Breton OpenStreetMap Team</a>',
})

let OpenTopoMap = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
  maxZoom: 17,
  attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
})

let Stamen_Watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
  attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  subdomains: 'abcd',
  minZoom: 1,
  maxZoom: 16,
  ext: 'jpg'
})

let Esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
})

let layers = {
  OpenStreetMap_BZH,
  OpenTopoMap,
  Stamen_Watercolor,
  Esri_WorldImagery
}

let area = L.geoJSON(khartoum).addTo(map)
let area2 = L.geoJSON(khartoum2, {
  onEachFeature: function (feature, layer) {
    let district = feature
    layer.bindPopup(feature["geometry"]["type"])
  }
}).addTo(map)

L.control.layers(layers, { area2 }).addTo(map)
map.fitBounds(area2.getBounds())
