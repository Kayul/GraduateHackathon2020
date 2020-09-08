<script type="text/javascript"
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBBzuRlMjqGU4wQK7URo0AW-9O6LHfXmmk&libraries=visualization">
</script>
let map, heatmap;
function initMap{
	map = new google.maps.Map(document.getElementById('map'), {
		center: new google.maps.LatLng(0, 0);
		zoom: 1,
		mapTypeId: 'satellite'
	  });
	heatmap = new google.maps.visualization.HeatmapLayer({
		data: getPoints(),
		map: map
	  });
}
function getPoints() {
const list = require( 'data_file.json');	
var data = ('.\data_file.json');
var points = []
var heatmapData = for (i in data){
	location: new google.maps.LatLng(data[i].longitude, data[i].latitude), weight: pollution/100}
	points.push(heatmapData)
return [new google.maps.LatLng(37.782551, -122.445368),
    new google.maps.LatLng(37.782745, -122.444586),
    new google.maps.LatLng(37.782842, -122.443688),
    new google.maps.LatLng(37.782919, -122.442815),
    new google.maps.LatLng(37.782992, -122.442112),
    new google.maps.LatLng(37.7831, -122.441461),
    new google.maps.LatLng(37.783206, -122.440829),
    new google.maps.LatLng(37.783273, -122.440324),
    new google.maps.LatLng(37.783316, -122.440023),
    new google.maps.LatLng(37.783357, -122.439794),
    new google.maps.LatLng(37.783371, -122.439687),
    new google.maps.LatLng(37.783368, -122.439666),
    new google.maps.LatLng(37.783383, -122.439594),
    new google.maps.LatLng(37.783508, -122.439525),
    new google.maps.LatLng(37.783842, -122.439591)];}

var heatmap = new google.maps.visualization.HeatmapLayer({
  data: heatMapData
});
heatmap.setMap(map);
