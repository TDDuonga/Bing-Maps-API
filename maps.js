// "use strict"
// const searchInput = document.querySelector(".search_input");
// const searchBtn = document.querySelector(".search_btn");

// let map, searchManager,sourcePin,destPin;

// searchBtn.addEventListener("click", ()=>{
//     map.entities.clear();
//     geocodeQuery(searchInput.value);
// });

// function getMap() {
//     // Bạn cần khóa Bing Maps của mình.
//     const credentials = 'AoSUH7WVIEiPvnqf8TwSppDbPkbYj0S3eeBUtk-NHFZy7iUFy8Vm_X80ZH7M8dH_';
  
//     // Tạo bản đồ Bing Maps.
//     const map = new Microsoft.Maps.Map('#map', { credentials });
  
//     // Đặt trung tâm và độ phóng to bản đồ.
//     map.setView({
//       center: new Microsoft.Maps.Location(10.825859244927047, 106.62970490571146),
//       zoom: 14,
//     });


//  // Tạo một hàm xử lý sự kiện khi người dùng nhấp vào bản đồ
// Microsoft.Maps.Events.addHandler(map, 'click', function (e) {
//     // Nếu chưa có điểm đầu, tạo điểm đầu và gán tọa độ
//     if (!sourcePin) {
//       sourcePin = new Microsoft.Maps.Pushpin(e.location, { color: 'red' });
//       map.entities.push(sourcePin);
  
//       // Lấy tọa độ của điểm đầu và lưu vào biến `sourceLocation`
//       sourceLocation = sourcePin.getPosition();
//     } else if (!destPin) {
//       // Nếu chưa có điểm cuối, tạo điểm cuối và gán tọa độ
//       destPin = new Microsoft.Maps.Pushpin(e.location, { color: 'blue' });
//       map.entities.push(destPin);
  
//       // Lấy tọa độ của điểm cuối và lưu vào biến `destLocation`
//       destLocation = destPin.getPosition();
      
//      // Tạo đối tượng Microsoft.Maps.Directions
//      directions = new Microsoft.Maps.Directions({
//         travelMode: Microsoft.Maps.TravelMode.Driving,
//         startLocation: sourceLocation,
//         endLocation: destLocation,
    
//   });
//  // Tính toán đường đi
//  directions.calculate();
//  // Thêm đường đi vào bản đồ
// if (directions) {
//   // Lấy mảng các điểm trên đường đi
//   const path = directions.path;

//   // Tạo một đối tượng Microsoft.Maps.Polyline
//   const line = new Microsoft.Maps.Polyline({
//     path: path,
//     stroke: { color: '#0000ff', width: 2 },
//   });

//   // Thêm đường đi vào bản đồ
//   map.entities.push(line);
// }
// }
// });
// // Thêm đường đi vào bản đồ
// if (directions) {
//     // Lấy mảng các điểm trên đường đi
//     const path = directions.path;
  
//     // Tạo một đối tượng Microsoft.Maps.Polyline
//     const line = new Microsoft.Maps.Polyline({
//       path: path,
//       stroke: { color: '#0000ff', width: 2 },
//     });
  
//     // Thêm đường đi vào bản đồ
//     map.entities.push(line);
// }

// function toggleBounce() {
//     // Nếu hoạt ảnh của điểm hiện tại không phải là null, hãy đặt hoạt ảnh thành null.
//     if (marker.getAnimation() !== null) {
//       marker.setAnimation(null);
//     } else {
//       // Nếu hoạt ảnh của điểm hiện tại là null, hãy đặt hoạt ảnh thành Microsoft.Maps.AnimationTypes.BOUNCE.
//       marker.setAnimation(Microsoft.Maps.AnimationTypes.BOUNCE);
//     }
//   }

// }


