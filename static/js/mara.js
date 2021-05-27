// get data  from "/api/popGb" in json format and display to template as chart
// Endpoint '/api/popGb' population/Energyconsumption

// #####################################################
// create a function to get data from route (e.g popGB)
// const api_url = '/api/popGb'

// async function getData(){
//   const response = await fetch(api_url)
// const data = await response.json();
// console.log(data)

// }

getData();

const api_url = '/api/popGb'

async function getData(){
  const response = await fetch(api_url)
const data = await response.json();
// console.log(data)

for (var i = 0; i < data.length; i++) {
  // data.date = data[i].date;
  data.energy_consumption = data[i].energy_consumption;
  data.location = data[i].location;
  console.log(data.energy_consumption);
//  get states data by its index
var ctx = document.getElementById("plots").getContext('2d');
var myChart = new Chart(ctx, {
type: 'polarArea',
data: {
labels: [
data[1].location, 
data[2].location, 
data[3].location, 
data[4].location, 
data[5].location, 
data[6].location, 
data[7].location],
datasets: [
{
  label: "Energy Consumption (PJ)",
  backgroundColor: [
  "#003f5c",
  "#386cb0",
  "#bc5090",
  "#ef5675",
  "#7fc97f",
  "#ff764a",
  "#ffa600"
  ],
  data: [
  Math.round(data[1].energy_consumption), 
  Math.round(data[2].energy_consumption),
  Math.round(data[3].energy_consumption), 
  Math.round(data[4].energy_consumption), 
  Math.round(data[5].energy_consumption), 
  Math.round(data[6].energy_consumption),
  Math.round(data[7].energy_consumption)]
  
}
]
},
options: {
legend: {
display: true,
position: 'bottom',
},
title: {
display: true,
text: 'Average Energy Consumption by State (PJ)'
},
scale: {
ticks: {
   display: true,
   maxTicksLimit: 2
  }}
}
})}
}
getData();