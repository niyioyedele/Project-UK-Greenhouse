const api_url = 'api/source'

async function getData(){
  const response = await fetch(api_url)
const data = await response.json();
console.log(data)

for(var i = 0; i < data.lenght; i++) {
  data.Sector = data[i].Sector
  data._1990 = data[i]._1990
}


var x = data.Sector
var y = data._1990

function init() {

data = [{x ,y}];
 


Plotly.newpLot('plot', data)
}

// Call updatePlotly() when a change takes place to the DOM
d3.selectAll("#selDataset").on("change", updatePlotly);

// This function is called when a dropdown menu item is selected
function updatePlotly() {
  // Use D3 to select the dropdown menu
  var dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  var dataset = dropdownMenu.property("value");

  // Initialize x and y arrays
  // var x = [];
  var y = [];

  if (dataset === '_1990') {y = data._1990;}
  if (dataset === '_1991') {y = data._1991;}
  if (dataset === '_1992') {y = data._1992;}
  if (dataset === '_1993') {y = data._1993;}
  if (dataset === '_1994') {y = data._1994;}
  if (dataset === '_1995') {y = data._1995;}
  if (dataset === '_1996') {y = data._1996;}
  if (dataset === '_1997') {y = data._1997;}
  if (dataset === '_1998') {y = data._1998;}
  if (dataset === '_1999') {y = data._1999;}
  if (dataset === '_2000') {y = data._2000;}
  if (dataset === '_2001') {y = data._2001;}
  if (dataset === '_2002') {y = data._2002;}
  if (dataset === '_2003') {y = data._2003;}
  if (dataset === '_2004') {y = data._2004;}
  if (dataset === '_2005') {y = data._2005;}
  if (dataset === '_2006') {y = data._2006;}
  if (dataset === '_2007') {y = data._2007;}
  if (dataset === '_2008') {y = data._2008;}
  if (dataset === '_2009') {y = data._2009;}
  if (dataset === '_2010') {y = data._2010;}
  if (dataset === '_2011') {y = data._2011;}
  if (dataset === '_2012') {y = data._2012;}
  if (dataset === '_2013') {y = data._2013;}
  if (dataset === '_2014') {y = data._2014;}
  if (dataset === '_2015') {y = data._2015;}
  if (dataset === '_2016') {y = data._2016;}
  if (dataset === '_2017') {y = data._2017;}
  if (dataset === '_2018') {y = data._2018;}
  if (dataset === '_2019') {y = data._2019;}
  

 // Note the extra brackets around  'y'
 
 Plotly.restyle("plot", "y", [y]);
}
}




getData();  
init();    
