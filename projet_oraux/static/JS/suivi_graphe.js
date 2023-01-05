google.charts.load('current', {'packages':['line']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {
	var data = new google.visualization.DataTable();
	data.addColumn('number', 'Day');
	data.addColumn('number', 'Guardians of the Galaxy');
	data.addColumn('number', 'The Avengers');
	data.addColumn('number', 'Transformers: Age of Extinction');
	data.addRows([
		[1,37.8,80.8,41.8],
		[2,30.9,69.5,32.4],
		[3,25.4,57,25.7],
		[4,11.7,18.8,10.5],
		[5,11.9,17.6,10.4],
		[6,8.8,13.6,7.7],
		[7,7.6,12.3,9.6],
		[8,12.3,29.2,10.6],
		[9,16.9,42.9,14.8],
		[10,12.8,30.9,11.6],
		[11,5.3,7.9,4.7],
		[12,6.6,8.4,5.2]
	]);
var options = {
 chart: {
 title: 'Ecart par rapport à la moyenne de la promo',
 subtitle: 'en nombre'
 },
 width: 900,
 height: 500
 };
 var chart = new google.charts.Line(document.getElementById('linechart_material'));
 chart.draw(data, google.charts.Line.convertOptions(options));
 }