$(function() {
    let lg05 = $("#lg05").html()
    let lt05 = $("#lt05").html()
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "正向评价",
            value: lg05
        }, {
            label: "负向评价",
            value: lt05
        }],
        resize: true
    });


});
