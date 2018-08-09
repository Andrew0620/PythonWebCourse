// 事件處理機制, 就線監聽 button, 當點擊時, 需做什麼事情 //

var button = document.getElementById('abbutton');
var result = document.getElementById('result');

button.addEventListener('click', function() {
    var xhr = new XMLHttpRequest();
    var handleOnload = function() {
        var data = JSON.parse(xhr.responseText);
        var htmlStr = '';
        console.log(data);
        data.forEach(function(value, index) {
            htmlStr += '<div>name:' + value['Name'] + '</div>'
        });
        result.innerHTML = htmlStr;
    }

    xhr.open('GET', 'http://163.29.157.32:8080/dataset/6a3e862a-e1cb-4e44-b989-d35609559463/resource/f4a75ba9-7721-4363-884d-c3820b0b917c/download/393625397fc043188a3f8237c1da1c6f.json,true')
    xhr.send();
    xhr.onload = handleOnload;
});      // 點擊時, 會出現 {} 的設定, true 表非同步處理//