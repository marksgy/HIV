        var map;  
        var gpsPoint;  
        var baiduPoint;  
        var gpsAddress;  
        var baiduAddress; 
        // var points =[]; 
        var myGeo = new BMap.Geocoder();
  
        function getLocation() {  
            //根据IP获取城市  
            var myCity = new BMap.LocalCity();  
            myCity.get(getCityByIP);  
  
            //获取GPS坐标  
            if (navigator.geolocation) {  
                navigator.geolocation.getCurrentPosition(showMap, handleError, { enableHighAccuracy: true, maximumAge: 1000 });  
            } else {  
                alert("您的浏览器不支持使用HTML 5来获取地理位置服务");  
            }  
        }  
        
        function showMap(value) {  
            var longitude = value.coords.longitude;  
            var latitude = value.coords.latitude;  
            map = new BMap.Map("map");  
            //alert("坐标经度为：" + latitude + "， 纬度为：" + longitude );  
            gpsPoint = new BMap.Point(longitude, latitude);    // 创建点坐标  
            map.centerAndZoom(gpsPoint, 15);  
  
        
            //根据坐标逆解析地址  
            var geoc = new BMap.Geocoder();  
            geoc.getLocation(gpsPoint, getCityByCoordinate);  
  
            BMap.Convertor.translate(gpsPoint, 0, translateCallback);  
        }  
  
            translateCallback = function (point) {  
            baiduPoint = point;  
            var geoc = new BMap.Geocoder();  
            geoc.getLocation(baiduPoint, getCityByBaiduCoordinate);  
        }  
  
        function getCityByCoordinate(rs) {  
            gpsAddress = rs.addressComponents;  
            var address = "GPS标注：" + gpsAddress.province + "," + gpsAddress.city + "," + gpsAddress.district + "," + gpsAddress.street + "," + gpsAddress.streetNumber;  
            var marker = new BMap.Marker(gpsPoint);  // 创建标注  
            map.addOverlay(marker);              // 将标注添加到地图中  
            var labelgps = new BMap.Label(address, { offset: new BMap.Size(20, -10) });  
            marker.setLabel(labelgps); //添加GPS标注      
        }  
  
        function getCityByBaiduCoordinate(rs) {  
            baiduAddress = rs.addressComponents;  
            var address = baiduAddress.province + "," + baiduAddress.city + "," + baiduAddress.district + "," + baiduAddress.street + "," + baiduAddress.streetNumber;  
            var marker = new BMap.Marker(baiduPoint,{
             // 指定Marker的icon属性为Symbol
             icon: new BMap.Symbol(BMap_Symbol_SHAPE_POINT, {
             scale: 1,//图标缩放大小
              fillColor: "orange",//填充颜色
             fillOpacity: 0.8//填充透明度
                })
            });
            map.addOverlay(marker);              // 将标注添加到地图中  
            marker.setAnimation(BMAP_ANIMATION_BOUNCE);  
            var labelbaidu = new BMap.Label(address, { offset: new BMap.Size(20, -10) }); 
            labelbaidu.setStyle({
			 color : "orange",
			 fontSize : "12px",
			 height : "20px",
			 lineHeight : "20px",
			 fontFamily:"微软雅黑"
             
		     });  
            marker.setLabel(labelbaidu); //添加百度标注   
        }  
        

        // function(points){	
		// var pt = points[index];
		// geocodeSearch(pt);
		// index++;
	    // }

	    // function geocodeSearch(pt){
		//     if(index < adds.length-1){
		// 	setTimeout(window.bdGEO,400);
		//     } 
		//     myGeo.getLocation(pt, function(rs){
		// 	var addComp = rs.addressComponents;
		//     var marker = new BMap.Marker(points[i]);
        //     var add = addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber;
		//     map.addOverlay(marker);
		//     marker.setLabel(new BMap.Label(add,{offset:new BMap.Size(20,-10)}));
	    // 	    });
	    // }
        //根据IP获取城市  
        function getCityByIP(rs) {  
            var cityName = rs.name;  
            alert("根据IP定位您所在的城市为:" + cityName);  
        }  
        function getCityByIP(rs) {  
            var cityName = rs.name;  
            alert("根据IP定位您所在的城市为:" + cityName);  
        }  
  
        function handleError(value) {  
            switch (value.code) {  
                case 1:  
                    alert("位置服务被拒绝");  
                    break;  
                case 2:  
                    alert("暂时获取不到位置信息");  
                    break;  
                case 3:  
                    alert("获取信息超时");  
                    break;  
                case 4:  
                    alert("未知错误");  
                    break;  
            }  
        }  
  
        function init() {  
            getLocation();  
        }  
  
        window.onload = init; 
// //sessionStorage
// var getinfor = window.sessionStorage.getItem("inpt")
// $("#save").click(function(){
// window.sessionStorage.setItem("inpt",$("#inpt").val());
// });
// $("#clickb").click(function(){
// alert("您输入的内容是：" + getinfor);
// });
// $("#delect").click(function(){
// window.sessionStorage.removeItem("inpt");//清除缓存
// });

// //localstorage
// $("#save").click(function(){
// localStorage.setItem("inpt",$("#inpt").val());
// });
// $("#delect").click(function(){
// localStorage.removeItem("inpt");
// });
// $("#clickb").click(function(){
// alert("您输入的内容是：" + localStorage.getItem("inpt"));//清除缓存
// });