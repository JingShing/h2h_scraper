// ==UserScript==
// @name         h2h scraper
// @version      0.1
// @description  try to scrape h2h
// @author       JingShing
// @icon         https://www.google.com/s2/favicons?sz=64&domain=htoh.asia
// @include      https://htoh.asia/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function showData(){
        var dataDict = {};
        var dataList = document.getElementsByClassName("card mb-3 card-updates views rounded-large shadow-large card-border-0");
        for (var data of dataList) {
            var title = data.getElementsByClassName("update-title")[0].innerText;
            console.log(title);
            dataDict[title] = [];

            var files = data.getElementsByClassName("media-wrapper rounded-0 saveclick glightbox");
            for(var file of files){
                var link = file.getAttribute("href");
                if(typeof(link)=="string"){
                    console.log(link);
                    dataDict[title].push(link);
                }
            }
        }
        console.log(dataDict);
        return dataDict;
    }

    function saveDictAsJSON(dictionary, fileName) {
        try {
            var jsonString = JSON.stringify(dictionary);
            var blob = new Blob([jsonString], { type: 'application/json' });
            var a = document.createElement('a');
            var url = window.URL.createObjectURL(blob);

            a.href = url;
            a.download = fileName + '.json';

            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Error saving JSON:', error);
        }
    }


    let btn=document.createElement("button");
    // in the buttom left page
    btn.innerHTML="h2h 爬蟲";
    btn.onclick=function(){
        var dataDict = showData();
        saveDictAsJSON(dataDict, "data");
    }
    document.body.append(btn);

})();