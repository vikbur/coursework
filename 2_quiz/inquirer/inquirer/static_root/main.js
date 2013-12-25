$(function() {
    //var placeholder = $("#placeholder");
    //var arr = $('li').map(function() {
      //  var $item = $(this);
        //  return  [[$item.attr('number'), $item.attr('value')]];}).get();
    //var data = [{label: "Йо-хо-хо, c с Новым годом!", color: "red", data: arr}];    
    var data = $('li').map(function() {
        var $item = $(this);
        var arr = [];
        var number = $item.attr('number')%4;
        if (number == 0) number = 4;
        for (var i = 1; i < 5; i++) {
            if (i==number) {
                arr.push([i, $item.attr('value')]);
            } else {
                arr.push([i, 0]);
            }
        } 
        return {               
            label: $item.attr('question'),
            data: arr
        };
    }).get();
    
    $.plot(placeholder, data, {
        series: {
            stack: true,
                lines: { show: false },
                bars: { show: true, barWidth: 0.2 }
            },       
        legend: { show: true, container: $("#legend") } 
    });
});
